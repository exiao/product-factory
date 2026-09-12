# Experimentation

## Hypothesis

```text
Because [observed evidence],
we believe [specific change]
will change [primary outcome]
for [eligible audience]
because [mechanism].
We will call it WIN, FAIL, or INCONCLUSIVE using [decision rule].
```

Choose one primary metric before launch. Add secondary metrics to explain the mechanism and guardrails for user trust, errors, support, cancellation, revenue quality, or retention. Define the numerator, denominator, attribution window, eligibility, exposure event, and unit of randomization.

## Design

- Randomize at a unit that prevents contamination, usually user or account, and keep assignment stable.
- Record allocation, exclusions, experiment start, planned end, sample target, minimum detectable effect, and analysis method before looking at results.
- Verify that both variants render and emit the same required events. Check sample ratio, missing events, duplicate exposures, bots, and rollout or platform changes.
- Plan segment reads in advance. Treat unplanned segment differences as exploratory unless separately powered and corrected.
- Use a holdout or staged rollout when a randomized test is impractical, and state the causal limitation.

## Sample and analysis

Estimate sample from the baseline for the exact metric, a meaningful minimum detectable effect, desired power, significance approach, and number of variants. More variants and repeated looks require adjustment. Run through relevant weekly or business cycles, but do not keep a test running indefinitely to obtain a preferred answer.

Do not stop at the first promising fluctuation. If sequential analysis is required, use a method that accounts for repeated looks. A statistically detectable lift can still be too small to justify implementation; judge practical significance and guardrails.

## Verdict

- **WIN:** the predeclared primary metric supports the change and no material guardrail fails.
- **FAIL:** the predeclared decision rule establishes a materially adverse primary outcome or a material guardrail failure.
- **INCONCLUSIVE:** evidence is too noisy, underpowered, contaminated, or mixed to choose, or instrumentation invalidates the comparison.

Explain what happened, plausible mechanism, limitations, and the next test. Do not convert a result into a rollout without the user's existing implementation authorization.
