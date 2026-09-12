# Evidence and output for recent research

## Source and time discipline

Record for each item: source class, title or first line, author/creator, direct source link when available, published timestamp, retrieved timestamp, engagement fields exposed by the source, and the claim it supports. Use inclusive UTC or an explicitly stated local cutoff. If a platform's date filter is unreliable, verify individual `published_at`/`upload_date` values and label older items as evergreen context.

Use source classes deliberately:

1. Community posts reveal language, objections, recommendations, and lived experience.
2. Video/transcript sources reveal demonstrations, repeated techniques, and audience response.
3. Web reporting, docs, and primary announcements provide context and exact facts.

Engagement ranks attention, not accuracy. Prefer a claim confirmed across independent classes. A single highly engaged post is a lead, not a consensus. Report missing, partial, zero-result, or low-signal sources explicitly.

## Query-specific synthesis

- **Recommendations:** list concrete products, tools, methods, or names; count independent mentions; show the strongest supporting sources and what each is used for.
- **News:** order by confirmed event date, separate reported fact from reaction, and state what remains uncertain.
- **Prompting/how-to:** identify the prompt format, useful constraints, examples, and recurring failure modes; produce one prompt only when requested.
- **General:** summarize the main conversations, practical implications, disagreements, and durable versus time-bound signals.

Lead with “What I learned,” then key patterns, caveats/contradictions, and a compact source-status block. Cite claims near the claim with a readable source name and link where available; do not hide evidence behind an uncheckable source count. Keep the report length proportional to usable evidence.

## Failure handling

Partial research remains usable if the completed source records are clear. Do not present a search timeout as a complete scan. If a parser fails, preserve raw output and extract only fields that can be verified. Do not retry a paid or rate-limited query blindly; inspect whether the first request returned data before retrying.
