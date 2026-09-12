# Trend triangulation and parsing

## Raw-first workflow

Save each provider response before parsing when the task calls for a durable report. Keep a source-status table with query, date window, result count, extraction status, and missing/partial/low-signal notes. This makes a failed or shell-only source visible instead of silently treating it as “no trend.”

## Platform-specific caveats

- X/search CLI responses may use camelCase fields such as `createdAt`, `replyCount`, `retweetCount`, `likeCount`, and `author.username`; parsers should accept the current schema rather than assume snake_case.
- YouTube search is relevance-ranked. `yt-dlp --dump-json` can provide useful title, uploader, views, likes, comments, upload date, URL, and thumbnail fields when installed, but `ytsearch` is not proof of freshness. Avoid flat-playlist mode when engagement metadata matters.
- Dynamic TikTok, Instagram, LinkedIn, Lemon8, and RedNote pages may return a generic shell or incomplete cards. A shell is low signal, not evidence that the niche is absent. Prefer a connected research provider when it exposes structured results, and disclose which fields were unavailable.
- Prometheus/mcporter tools may return JavaScript-like output with unquoted keys, single-quoted strings, string concatenation, and truncation markers. Save raw output; parse `content[].text` for synthesis and targeted numeric fields with a schema-aware parser. Do not send it blindly to `json.load` or `jq`. Ranking tools may be strict JSON, but inspect the first response.

## Scoring and synthesis

Use engagement rate `(likes + comments + shares) / views` only when denominators and time windows are comparable. A single observation yields only average views per hour since publication, not recent acceleration. Measure velocity changes from repeated observations with reliable timestamps. Treat views/follower count as a descriptive breakout proxy, not an account-normalized causal measure. Treat saves/bookmarks as a strong signal for repeatable or instructional formats. Normalize or rank within platform before making a cross-platform table.

Call a theme a cross-platform signal only when independent sources support it. Call one-source findings opportunities or observations. For app rankings, count actual positive movers; if fewer than five moved up, say so and fill the report with strategically relevant high-ranking apps rather than labeling decliners as climbers.

For editorial or consumer-finance creative, translate capability claims into a human problem or desired outcome, then make the product capability the proof beat. Keep this as a domain-specific example, not a universal hook formula.

## Report shape

1. Executive summary with the strongest confirmed signals.
2. Platform/source status and limitations.
3. Ranked items with evidence and direct links.
4. Hook, format, reveal order, audience, and why-now analysis.
5. Cross-platform themes versus single-source opportunities.
6. Remixable briefs and contrarian “avoid” notes.
7. Raw-data index when files were saved.
