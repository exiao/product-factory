# Loop design and examples

A useful loop definition answers:

- What outcome does it protect, and who uses the result?
- What exact sources, accounts, filters, timezone, and window does it inspect?
- How often does it check, and what constitutes a new actionable condition?
- What steps run, with what bounds on cost, items, and duration?
- How does it detect stale tracking, sparse samples, seasonality, or mismatched denominators?
- What state survives retries and restarts?
- What can it do under existing authorization, and what must remain a proposal?
- Where does the evidence/output go, and when should it notify?
- What makes it skip, stop, require input, or be disabled?

Select one useful loop before assembling a large catalog:

| Job | Evidence and trigger | Output and relevant skills |
|---|---|---|
| Creative fatigue review | Comparable placement/cohort metrics, enough delivery, sustained deterioration against a stated baseline | Diagnose and draft a new concept slate with ad-creative and ads-diagnostics; no automatic budget changes |
| Search opportunity review | Matched keyword/page snapshots, verified indexing state, relevant buyer intent | Prioritized refresh/page brief using seo-research |
| Activation watch | Eligible signup cohort, lag-aware activation events, tracking freshness | Investigated friction and experiment proposal using growth |
| Churn or payment recovery review | Separate voluntary churn and payment failures, confirm current subscription state | Recovery proposal with growth; sending or subscription changes only within authorization |
| Content performance review | Published items and comparable distribution windows, source-defined downstream metrics | Next-batch briefs using content-strategy, with evidence limitations |
| Creator pilot review | Agreed deliverables, total cost, mature conversion window, usage rights | Continue/revise/end recommendation using influencer-marketing |

These are adaptable examples, not fixed cadences or universal thresholds. Missing data is not a measured zero. Views and a platform rating alone do not establish profit or causal lift.

For a first run, use a bounded baseline or dry run that performs no external writes. Report what was actually fetched and checked. For external actions, verify the object and action scope before execution and read back state afterward. If a paid request times out, reconcile it before resubmission. Do not describe a scheduled job as tested merely because the scheduler accepted it.

A saved prompt should name the job, sources, filters, evidence checks, maximum scope, state path, output, action boundaries, and notification rule in ordinary prose. Let the scheduling tool handle recurrence configuration. Maintain a clear disable path using the actual automation identity.
