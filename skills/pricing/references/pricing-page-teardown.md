# Pricing page teardown

Score two axes separately: human buyer experience and AI-agent readiness. Use the rendered text/HTML where possible, then run a paste test asking for the plans and prices. A failed paste test is evidence of extractability trouble, not proof that every browser or agent fails.

## Human buyer experience

Score value-proposition clarity, plan differentiation, cognitive load, trust signals, pricing psychology, and transparency. Passing means the buyer can identify who each plan is for, what changes between tiers, what the price includes, and what happens at limits or cancellation.

## AI-agent readiness

Score machine-readable prices, extractable FAQ and objections, per-tier limits in text, and structured data/semantic HTML with appropriate crawler access. Prices hidden in images, JS-only interactions, auth walls, or universal “contact us” tiers are hard to quote. `Offer` schema and AI-search access should be handed to the relevant implementation workflow; they do not guarantee citations.

## Method

1. Load the product’s audience and positioning context.
2. Fetch rendered text/HTML and record whether prices and limits appear in text.
3. Run the paste test and preserve what the model omitted or misread.
4. Score each dimension Pass, Partial, or Gap with one evidence line.
5. Prioritize fixes by impact and effort, separating content, design, schema, crawlability, and CRO work.

```markdown
# Pricing Page Teardown — [url] — [date]

## Scores
- Human buyer experience: [passing dimensions]
- AI-agent readiness: [passing dimensions]

## Paste test
[What was extracted and what was missed]

| Dimension | Verdict | Evidence |
|---|---|---|
| Value clarity | Pass/Partial/Gap | ... |
| Plan differentiation | Pass/Partial/Gap | ... |

## Prioritized fixes
1. [impact/effort] — [fix] — [reason/owner]
```
