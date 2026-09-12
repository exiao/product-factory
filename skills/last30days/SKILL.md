---
name: last30days
description: Research what people, communities, and credible sources discussed in a topic's recent time window, usually the last 30 days. Use for recent recommendations, news, debates, techniques, or prompt practices; ongoing trend scouting belongs to trend-research.
---

# Recent cross-source research

Use this skill for a bounded recent snapshot. Parse the request before searching:

- **Topic:** the exact subject and terminology the user supplied.
- **Target tool:** where a resulting prompt or recommendation will be used, if specified.
- **Query type:** recommendations, news/updates, prompting/how-to, or general understanding.
- **Window:** default 30 days, or the explicit number of days/date range.

Do not ask for a target tool before research when it was not specified. Search first, then ask only if a tailored follow-up prompt needs it. State the interpreted topic, query type, window, and sources before beginning when the workflow is substantial. Use the currently available web/search/connectors; do not assume a bundled script, API key, CLI, MCP server, or browser session exists.

For broad discourse research, seek at least two independent source classes when available: community conversation (Reddit, X, forums), video/transcript evidence, and web reporting/docs. Verify every item's publication date against the cutoff. A source returned by a relevance-ranked search is not automatically recent. Supplement a missing or weak class rather than silently treating it as corroboration. For technical or exact product claims, prioritize primary documentation and announcements; community popularity cannot establish correctness.

Read source content before synthesizing. Weight engagement and transcript evidence as signals of attention, not truth. Separate repeated cross-source patterns from single-source observations, record contradictions, and distinguish current facts from opinion. For recommendations, extract specific names and count mentions; generic advice is not a substitute for the requested list. For prompting requests, extract the format, constraints, examples, and failure modes the sources actually recommend.

Read [references/evidence-and-output.md](references/evidence-and-output.md) for cutoff checks, source weighting, citation practice, and compact output templates. Include follow-up directions only when useful to the requested outcome. Reuse gathered evidence for follow-ups when sufficient; refresh sources when facts may have changed, evidence is missing, or the user asks for fresh research.

This skill researches and drafts. It does not post, publish, schedule, like, or modify content. Preserve raw source notes when the task needs an auditable artifact, but do not store credentials or private account data.
