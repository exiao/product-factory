# Evidence, joins, and recommendations

## Use the right denominator

Record time window, cohort start, eligibility, attribution window, currency, filters, and whether the metric is campaign-goal scoped or all-event. Do not call a percentage “normal” without a source or a comparable baseline. If the emitter is absent, report “not instrumented,” not a funnel loss.

## Join to product outcomes

When platform attribution is incomplete, join spend and clicks to first-party outcomes where permitted: signups, reached users, first messages, qualified leads, paid subscriptions, or retained users. Report both arrival and depth (for example, completed first action and repeated use). A cheaper click can be a more expensive outcome. State which joins are deterministic, probabilistic, or unavailable.

## Confidence-ranked report

```markdown
## Symptom and scope
[platform, objects, window, objective, destination]

## First confirmed break
[layer, query/evidence, confidence]

## What is healthy
[upstream/downstream checks that passed]

## Likely cause and alternatives
[owner, uncertainty, missing evidence]

## Recommended next step
[read-only validation or smallest reversible authorized change]

## Mutation status
[none, authorized and verified, or ambiguous; include no secrets]
```

Never recommend pausing, scaling, reallocating, changing budgets/objectives, or replacing creative solely from a proxy metric when a preceding delivery or attribution layer is unverified.
