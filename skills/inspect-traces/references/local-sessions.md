# Local Claude Code and Codex sessions

Inspect saved files read-only; do not resume a session to inspect it. Start with
the known project, date range, or session ID, and exclude the current audit from
pattern counts. Never read credential files. Storage layouts can change: confirm
the paths and a few record shapes before assuming coverage.

## Discover candidates

Both sources are first-class; check both roots before falling back to a vendor.
Use configured roots, including an explicitly supplied export/storage location:

```sh
claude_root="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
codex_root="${CODEX_HOME:-$HOME/.codex}"
# Run only for directories that exist. Filter filenames by known date/ID first.
rg --files --hidden "$claude_root/projects" -g '*.jsonl'
rg --files --hidden "$codex_root/sessions" "$codex_root/archived_sessions" -g '*.jsonl'
```

Filter results locally rather than dumping every path into the conversation.
Use file times only to shortlist; event timestamps establish chronology. Missing
roots or indexes do not require a CLI install. Permission failures, retention,
disabled persistence, another machine, and cloud-only sessions can limit coverage.

### Claude Code

- Default transcripts: `~/.claude/projects/<project>/<session-id>.jsonl`;
  `CLAUDE_CONFIG_DIR` relocates the root. Discover actual directories instead of
  assuming the project-name encoding. Worktrees can have separate directories.
- If available, `history.jsonl` or project session indexes help locate IDs and
  projects; they are not complete transcripts. Verify index paths against files.
- In transcript metadata, use `sessionId`, `cwd`, `timestamp`, `uuid`, and
  `parentUuid` when present. Inspect top-level `type: user` / `type: assistant`
  records; the conversation is in `message.role` and `message.content`.
- Content may be a string or blocks. Read `text` blocks for conversation.
  A user-role `tool_result` is a tool response, not a human instruction or
  correction. Connect `tool_use` / `tool_result` by their IDs only when needed.
- Preserve `parentUuid` and `isSidechain` where present; discover subagent files
  under the selected session/project when relevant. Do not interleave a child
  agent's conversation with its parent's or count replayed branch history as
  independent cases. Compact summaries are not the full earlier exchange.

Official reference: [Claude Code sessions and transcript storage](https://code.claude.com/docs/en/sessions).
This route covers local Claude Code files, not an assumption that Claude web or
Desktop history is stored in the same place.

### Codex

- Under `${CODEX_HOME:-$HOME/.codex}`, check `session_index.jsonl`, `sessions/`,
  and `archived_sessions/` when present. Indexes are discovery hints, not proof
  that all session messages are indexed. Locate known IDs in filenames first.
- Rollout JSONL commonly starts with `type: session_meta`; its `payload` gives
  the session ID (`id` or `session_id`), `cwd`, timestamp, and source metadata.
  Use `turn_context` for context changes where needed.
- Prefer `type: response_item` with `payload.type: message` and
  `payload.role: user` or `assistant`. Join text-bearing `payload.content`
  blocks (`input_text`, `output_text`, or `text`, depending on the version).
- `event_msg` may duplicate a user/assistant message. Use it to supplement
  missing details rather than counting both forms. Tool calls/results are
  separate response items, matched by call ID when relevant.
- Inspect compaction, fork, and subagent boundaries before treating repetitions
  as new failures. Do not attempt to decode encrypted reasoning content.

The JSONL shapes above are observed formats, not a stable API. Confirm locally.
Official reference: [Codex configuration and CODEX_HOME](https://developers.openai.com/codex/config-advanced/).

## Read a bounded conversation window

After selecting a file and relevant original line range, this Python example
prints only conversational text with its source line. Substitute the path and
line bounds; widen the window when a decision or correction lacks context.
It deliberately omits tool blocks, which must be inspected separately when the
question needs them. A window with no text does not establish an empty session.

```sh
python3 - /absolute/path/to/session.jsonl 1 120 <<'PY'
import json, sys
from pathlib import Path
path = Path(sys.argv[1])
start, end = map(int, sys.argv[2:4])
assert 1 <= start <= end, 'Use a positive, inclusive line range'
with path.open() as stream:
    for line_no, raw in enumerate(stream, 1):
        if line_no > end:
            break
        if line_no < start:
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError:
            print(f'{path}:{line_no} [unreadable JSON; coverage gap]')
            continue
        if not isinstance(record, dict):
            continue
        kind = record.get('type')
        message = (record.get('payload') if kind == 'response_item'
                   else record.get('message') if kind in ('user', 'assistant')
                   else None)
        if not isinstance(message, dict) or message.get('role') not in ('user', 'assistant'):
            continue
        content = message.get('content', [])
        blocks = [{'type': 'text', 'text': content}] if isinstance(content, str) else content
        if not isinstance(blocks, list):
            continue
        text = '\n'.join(b['text'] for b in blocks if isinstance(b, dict) and b.get('type') in ('text', 'input_text', 'output_text') and isinstance(b.get('text'), str))
        if text:
            print(f"{path}:{line_no} [{record.get('timestamp', '')} {message['role']}]")
            print(text[:4000] + ('\n[truncated; read original line]' if len(text) > 4000 else ''))
PY
```

Keep original 1-based line numbers when parsing or filtering. Do not drop an
entire user message because it contains injected environment context: the real
request can follow `## My request:`, with relevant feedback under
`# Browser comments:`. Separate boilerplate and historical instructions from the
user's request without discarding corrections or attached-evidence references.

For findings dependent on tool execution or a visual artifact, inspect those
specific records/files too; conversational extraction alone is not runtime proof.
Report malformed/truncated records and unreadable files as gaps. Deduplicate
using provider IDs and branch context where available, not text equality alone:
a repeated correction may be a real repeated event.
