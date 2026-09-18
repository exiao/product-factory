# Runnable review starter

Use `python3 scripts/create_review.py /absolute/review-directory`. It copies the template and shared assets without overwriting an existing review. Preserve an established site's content, versions and feedback keys when migrating.

Edit `artifacts.json` and supply real artifact files. Fields:

- Root: `id`, `title`, optional persistent `storageKey`, `artifacts`.
- Artifact: stable `id`, `version`, `type`, `title`, and a short `question`.
- Image: `image`, `alt`. Display the image inline without a separate Expand image control. `prototype` adds a separate-tab Open prototype link, never an iframe.
- Text: `content` paragraph array (strings or `{text,references:[{label,url}]}` objects) and optional `points` list; use actual work, not repeated process explanations.
- `limitation`: optional decision-critical qualification not already communicated by the artifact. Omit generic scenario captions and implementation-verification status.
- `options`: `{id,label}` array. Multiple selection by default; set `singleSelection` only for an actual exclusive decision. Custom intent always remains possible in Notes.
- `selected`, `settled`, `status`: carry explicit or delegated choices; never invent user approvals.
- Put source links in the paragraph they support using `references`. Do not add a separate links dump or More menu.
- Use Notes + Request revision for research, alternatives, and corrections.
- `history` may retain prior version metadata for the host; it is not rendered in the default UI. Feedback remains versioned.

Serve with `python3 server.py --port 8873 --thread ORIGINATING_TASK_UUID`. The server binds localhost, fixes the destination on startup, and refuses task rebinding. No browser-supplied thread or shell command is accepted. Confirm `codex queue --help` exists before promising submission. Without `--thread`, the UI says Save feedback and reports local-only persistence after use.

Submission saves an immutable content-addressed snapshot and attempts `codex queue --thread ... --message ...` with an argv array. Only a parsed acknowledgment for that task produces Sent. Duplicate snapshots reuse their receipt; uncertain delivery is not automatically retried. The queued message tells the agent to read artifact IDs/versions, preserve all selected options and distinguish drafts from explicit decisions. A receipt is not proof the requested revisions happened.

The template uses native controls and textContent for supplied data. Only http(s) and local relative media/link URLs are accepted. Theme `--review-font`, `--review-bg`, `--review-text`, `--review-muted`, `--review-accent`, `--review-border`, and `--review-selected`. Do not override each button's font independently.

Navigation is supplied by `assets/review-desk.js`: desktop queue, mobile horizontal navigation and immediately visible artifact. `mountReviewDesk(root,{getItems,renderArtifact,initialId,onNavigate})` remains available for custom existing hosts. The host persists input before navigation. `select(id)`, `advance()`, `refresh()` and `destroy()` are supported; `showQueue()` is a compatibility alias for opening the next artifact, not a mobile list landing page.

Run `NODE_PATH=<playwright-packages> node scripts/check-desk.cjs` (set `PLAYWRIGHT_CHANNEL=chrome` if using installed Chrome), plus the server handoff tests. Inspect the integrated artifacts at desktop and mobile widths. End-to-end submission proof requires one marked verification snapshot acknowledged by the actual originating task; fixture tests alone do not establish the live bridge.
