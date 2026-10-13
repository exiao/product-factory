# Experiment records

Use existing project formats. Store records alongside the project eval, not inside an installed skill. A compact manifest, result ledger, and candidate directories are sufficient.

## Preserve enough to replay the comparison

- Task and outcome, objective metric/unit/direction, useful gain, quality floor, critical gates, selection schedule, and batch plateau rule. Record user-set overall limits separately from agent-chosen batch limits; retain cumulative usage and the reason for each subsequent batch.
- Allowed changes and fixed conditions; artifact, fixture, evaluator, dependency, and runtime versions or hashes; effective model/provider/authentication metadata without secrets.
- Case IDs, provenance, incident groups, split membership, planned repetitions, and exposure history. Record whether an optimizer has read each split's traces or consulted its scores.
- Immutable original baseline and candidate snapshots, parent IDs, hypotheses, diffs, outputs/artifacts, full relevant traces, per-criterion grades and judge evidence.
- Attempts, completion status, failure cause, resource receipts, and timing. Keep subject, simulator, evaluator, and analysis costs separate. Null means unknown, not zero.
- Current best, rejected changes and reasons, completed and pending run keys, consumed resources, remaining allowance, and exact resume commands.

Write durable results as each attempt completes. A run key should distinguish configuration, case, repetition, and attempt; grades additionally identify evaluator version. Resume only after checking artifact/configuration hashes and recorded completion. Reuse a saved output for regrading; do not regenerate it merely because its grader failed. Preserve incomplete attempts and their resource use. Parallel workers must not overwrite each other's artifacts or append conflicting checkpoint state.

## Compare the observations that answer the question

Pair the same cases under compatible versions and conditions. Report missing pairs and error counts alongside the scored denominator. Show per-case changes and critical regressions before the average. Compare cost or time only over a clearly defined denominator, including failed attempts and retries when measuring cost per completed task.

For stochastic work, distinguish variation across cases, repeated executions, artifact builds, and judges. Repeats of one case are not new task coverage. Use case- or incident-level uncertainty estimates when those are the independent units; do not claim significance by counting correlated repeats as independent samples. Repeated adaptive selection also affects inference. Descriptive paired results are preferable to an unsupported statistical guarantee.

For subjective judgments, use anchored rubrics or blinded comparisons with randomized presentation order. Freeze reference outputs before a round and retain their identities. A change in judge, rubric, or reference creates a new grading condition; regrade saved outputs where valid.

A compact result table can show candidate, objective, quality gates, cost, time, valid/planned cases, decision, and evidence links. Recompute it from the saved per-case records. Preserve rendered artifacts where appearance matters. A dashboard is optional.
