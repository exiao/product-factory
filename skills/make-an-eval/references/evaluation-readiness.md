# Evaluation readiness

Use before trusting a new or inherited evaluation for comparison or optimization. Inspect the runner, actual inputs, saved outputs, and scoring path. Reuse verified checks for unchanged versions. Run only the controls and model calls covered by the agreed plan; read-only inspection and fixture preparation can proceed independently.

## Outcome and coverage

Confirm that success measures the requested outcome. A proxy needs an explicit limitation and a final check against the real outcome when feasible. Identify whether the task is meant to test an outcome or a particular mechanism; tool use is not automatically required when a valid answer can be produced another way.

Include ordinary successes and legitimate no-action cases as well as failures. Check duplicates, related incidents across splits, class imbalance, missing inputs, stale keys, and label provenance. At scale, inspect all rows programmatically and closely read a representative sample. Use human-verified keys where available and allow defensible alternatives. Generated labels remain provisional. Do not give the subject investigative hints it would not normally receive.

For detection or classification, inspect the confusion matrix and report relevant precision, recall, and false-positive rates with class counts. Undefined ratios remain undefined. Include cases where an action is warranted and where it is unnecessary so an always-act or never-act policy cannot win by construction. Compare against a meaningful simple baseline. A deliberately balanced diagnostic suite does not estimate production accuracy without a justified population weighting.

## Model-judge calibration

Hide candidate identity and prestige labels such as "human" or "reference" from comparative judges. Check sensitivity to presentation order and length with matched examples where these should not change the verdict. Record possible self-preference when the judge is also a subject model; propose an independent check for close decisions without silently replacing the chosen judge.

Validate against independently reviewed labels when available and inspect disagreements, including grader false positives and false negatives. Agreement with synthetic labels is provisional, and a different model family alone does not validate a judge. Choose any acceptance threshold for the actual decision rather than importing a universal agreement percentage. Freeze pairwise references; changing them requires a new grading condition. If variation across outputs is a task requirement, assess it across the set because isolated pairwise judgments cannot establish diversity.

## Runtime and evidence

Exercise the actual subject entry point or explain adapter differences. Probe the relevant tool, memory, retrieval source, skill, or setting through the same path the eval uses. Verify effective configuration and nested-agent settings where applicable. A config file alone does not prove activation.

Check fresh state and fixture isolation. Run meaningful positive and negative controls through the runner and grader, including an explicit negative answer versus missing output when "none" is valid. Inspect baseline passes and failures for incorrect keys, grading shortcuts, inaccessible artifacts, or mismatched evidence. Verify score, output, trace, usage, and timing belong to the same attempt.

Keep requested and returned model identities. Explain documented alias resolution; unexpected substitution invalidates that condition. When identity cannot be verified, report the limit. Keep hidden keys and grading artifacts outside subject access, including tools and filesystem mounts. Hash checks alone do not isolate them.

## Failures, retries, and resume

Declare attempt and retry semantics before the run. Record transient service failures separately, cap retries with backoff, and apply a total task timeout. A case that eventually passes after extra attempts must not look like first-attempt success. If production retries are part of the tested behavior, grade that complete policy and include its resource use.

Separate evaluator errors and invalid environments from subject failures. Do not automatically exclude refusals, malformed answers, truncation, or exhausted task budgets: determine whether they violate the task contract or expose a setup defect. Preserve both the planned denominator and usable observations. Differential missingness can invalidate a comparison even when every remaining grade is correct.

Persist completed attempts incrementally. Key results by configuration, case, repetition, and attempt; version grades separately. Resume only verified completed work with matching configuration and input hashes. Keep failed attempts and charges. A grader retry should reuse the saved subject output. For long or costly runs, verify interruption recovery without duplicate execution or lost records using local controls.

## Measurement and sensitivity

Recompute aggregates from per-case records and declared weights. Check units, denominator, missing values, and implausible constants. Distinguish real zero values from missing-field defaults. Retain end-to-end subject timing including tools and retries; optional model-call latency is a separate measure. Keep judge and simulator overhead separate.

For cost or latency comparisons, declare cold-start versus warmed execution, concurrency, and cache policy. Balance or randomize candidate run order when feasible, and record cache usage and service conditions. Unexplained warm-cache or time-of-day differences limit attribution to the candidate. Preserve the setup that represents intended use rather than clearing every cache by default.

Before hill-climbing, compare available headroom, the smallest useful change, and observed variability. Repeat at the source of uncertainty: new subject executions for generation noise, new builds for generated artifacts, or new judgments for grader noise. Repeated scoring of one build cannot reveal build variance. With insufficient observations, report unresolved sensitivity instead of inventing a confidence interval. More repetitions do not replace independent cases or fix a saturated metric.

Report concrete findings with evidence and their effect on the decision. Classify each relevant check as verified, failed, or untested. Block claims that depend on failed checks, repair the responsible component within scope, and preserve old grades. A rubric or fixture repair is a new measurement version, not improved subject performance.

Sources and adaptation choices are recorded in [source notes](source-notes.md).
