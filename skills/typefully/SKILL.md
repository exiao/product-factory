---
name: typefully
description: Draft, inspect, schedule, publish, and analyze social posts through the Typefully API CLI for X, LinkedIn, Threads, Bluesky, and Mastodon. Use for social content workflows; drafting does not authorize publishing.
---

# Typefully CLI

The bundled zero-dependency Node CLI is [scripts/typefully.js](scripts/typefully.js). It requires Node.js 18+ and uses `TYPEFULLY_API_KEY` or the CLI's interactive setup. Do not search for keys in `.env`, keychains, or unrelated config files. Use `config:show` and `social-sets:list` to identify the target social set; ask when multiple sets exist and no default is configured.

Common commands:

```bash
node scripts/typefully.js config:show
node scripts/typefully.js social-sets:list
node scripts/typefully.js drafts:create --platform x --text "Draft text"
node scripts/typefully.js drafts:create --platform x,linkedin --text "Same post"
node scripts/typefully.js drafts:list --status scheduled
node scripts/typefully.js queue:get --start-date YYYY-MM-DD --end-date YYYY-MM-DD
node scripts/typefully.js analytics:posts:list --start-date YYYY-MM-DD --end-date YYYY-MM-DD
node scripts/typefully.js social-sets:get
```

Use one draft for multi-platform publishing. If content differs, create it for one platform and update the same draft for the second. Draft creation is reversible and distinct from publication: `drafts:create` leaves content in Typefully, while `--schedule now` and `drafts:publish` publish immediately, and a future `--schedule` commits a scheduled post. Perform scheduling or publication only when that action is authorized; do not ask again when authorization already covers the exact target. On a timeout or ambiguous response, fetch the draft by ID and list the queue first; only retry when the first request is established to have failed before creation, or when the API documents idempotency. Otherwise stop and report the ambiguous state to avoid duplicate posts.

Before creating tags, list existing tags; tags are scoped to social sets. Resolve a LinkedIn organization URL before inserting a mention. Preserve `<typ:comment-thread>` anchors in draft text and never resolve/delete comments without explicit instruction. Read [references/platforms-and-comments.md](references/platforms-and-comments.md) for these format-specific rules.
