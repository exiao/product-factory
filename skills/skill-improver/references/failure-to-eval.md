# Turn an observed failure into an eval

Use this when a consequential or recurring failure is worth replaying. Reuse the project's existing dataset or test format; the fields below are a portable handoff, not a required framework. A Markdown case and a command can be enough.

## Case handoff

- **Identity and provenance:** stable case ID, task family, source run/date, and a short redacted trace excerpt or approved local evidence pointer. Distinguish observed failures from synthetic variants.
- **Executor input:** original request and only the artifacts/context the agent would actually receive. Keep expected answers, grading notes, and the suspected failure out of this package.
- **Environment:** relevant file/data snapshot, tool behavior and versions, clock or randomness where material, permitted actions, setup and reset instructions. Record simulation boundaries and missing dependencies.
- **Verifier:** criterion IDs, observable final state/artifacts, forbidden behavior where relevant, and the check command or anchored rubric, with known-good and plausible-but-bad calibration outputs and their reasons. Score only criteria the fixture and observable output actually exercise; mark others untested or add a separately labeled synthetic variant. Do not require a new output format unless the task or evaluation contract calls for it. Keep factual correctness, subjective quality, and critical constraints separate so an average cannot hide a critical failure.
- **Evaluation record:** baseline/candidate skill and model/configuration identifiers, evaluator version, outputs, relevant action trace, verdict, time/cost when available, and train/validation/test membership. Preserve unknowns rather than treating missing evidence as pass.

## Extract and diagnose

1. Inspect the request, result, and relevant action trace. Locate the first supported divergence. Distinguish tool/service failure, missing or stale context, instruction/routing error, model behavior, and verifier error; mark competing explanations unresolved.
2. Extract the smallest fixture that preserves the failure mechanism. Redact secrets and personal/customer data before copying traces. Use safe local targets, dry runs, or recorded responses for external writes; reset must not delete real user data. Do not replay live sends, trades, or purchases to make a case reproducible.
3. Replay the baseline and confirm the case captures the observed defect. If reproduction is unavailable or intermittent, record that limit and observed frequency; do not call the case a proven regression test. Preserve enough context to avoid simplifying the bug away.
4. Check the verifier against known-good and plausible-but-bad outcomes. Use trusted/reference labels when available; provisional labels remain provisional. An error-free tool trace is not proof that the requested outcome happened.
5. Deduplicate by failure mechanism, preserving variants only when they exercise materially different behavior. Include representative successful cases so the suite does not reward avoiding the task. Cases used to diagnose or tune a change belong in training or regression coverage, never a sealed test set. A newly discovered failure from held-out data is no longer sealed once inspected for tuning.
6. Try the smallest change supported by the diagnosis: repair context, tool contracts, routing, or instructions before escalating complexity. Model changes remain candidates to measure; do not add infrastructure or fine-tuning without evidence and scope. Continue with the bounded baseline/candidate loop in the parent skill.

## Example: stale evidence in a research answer

**Request:** Summarize the latest filing available as of a specified date. **Fixture:** A local tool stub serves two clearly dated filings plus the original stale answer; only the request and source-access tool are exposed to the executor. **Verifier:** Check which filing was selected and whether cited figures match it; judge clarity separately. A fluent answer using the older filing is a negative calibration example. Reset restores the same source snapshot before each run. This checks source selection against the fixture, not the reliability of live retrieval.
