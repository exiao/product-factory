---
name: ads-diagnostics
description: "Diagnose ad delivery, conversion attribution, destination, and optimization-signal failures across paid channels. Use when active ads have no impressions, spend collapses, reports are empty, ROAS is missing, or an optimization event is not converting."
---

# Ads diagnostics

Find the first broken layer before recommending a fix. An ad can be active while account policy, spend caps, auction eligibility, budget dilution, targeting, destination behavior, event instrumentation, or attribution prevents useful delivery. A zero row in a performance report may mean zero delivery, not a weak ad.

## Default workflow

1. Establish scope: platform, account, campaign/ad set, date window, objective, destination, and the exact symptom.
2. Check account and policy eligibility, spend caps, billing state, review state, and destination health.
3. Separate delivery-dead, budget-starved, spend-capped, policy-limited, objective-mismatched, and bid-target-throttled states.
4. If clicks exist but conversions do not, walk click capture → user/install match → postback/handler → dataset event → attributed spend. Investigate the first verified break; missing instrumentation or unavailable data is not a measured zero.
5. Check that the metric is instrumented and that its denominator, scope, and source are valid before calculating a drop-off or calling it normal.
6. Report evidence, likely cause, uncertainty, owner, and the smallest reversible next step.

Read-only diagnosis is the default. Inspect current provider schemas, API versions, field names, and account semantics before querying. Credentials belong in the approved runtime and never in URLs, argv, logs, source, or reports.

Read [references/delivery-ladder.md](references/delivery-ladder.md) for account, policy, delivery, budget, bid, objective, and review checks. Read [references/attribution-ladder.md](references/attribution-ladder.md) for instrumentation and the first-zero funnel. Read [references/destinations-and-objectives.md](references/destinations-and-objectives.md) for redirects, click-to-message mechanisms, optimization-event mismatches, and canary interpretation. Read [references/evidence-and-reporting.md](references/evidence-and-reporting.md) for metric scope, product-side joins, and safe recommendations.

## Actions and fixes

Pausing, recreating, changing budgets/bids/objectives, changing tracking, editing destinations, or uploading creative requires authorization for that exact operation. Preserve existing authorization and perform requested fixes within that scope; do not repeatedly ask for an already-authorized action. Use a dry run where supported, then re-query state. On an ambiguous response, inspect the object and change history before retrying; retry only when the first request is known to have failed before mutation or the provider documents idempotency. Never run an automatic kill, repair, or reallocation loop.

## Output

Separate **served**, **sent**, **received**, **matched**, **attributed**, and **paid**. Use tables when comparing campaigns or stages. State the date window, filters, event definitions, and missing data. A recommended change must name the evidence it addresses and a validation query or observation window.
