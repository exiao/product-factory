# Evaluation readiness

Use before trusting a new or inherited evaluation for comparison or optimization. Inspect the runner, actual inputs, saved outputs, and scoring path. Reuse verified checks for unchanged versions. Run only the controls and model calls covered by the agreed plan; read-only inspection and fixture preparation can proceed independently.

## Load the real suite before model calls

Run the actual loader on the maintained case file, not only a toy fixture. Inventory each declared case as executable, manual, skipped with a reason, or blocked on a named adapter/capability. Verify unique IDs, complete prompts and multiline criteria, expected inclusion, and preservation of legitimate skips. Unsupported endpoint, memory, or multi-turn cases must not silently disappear or masquerade as ordinary single-turn chat. A parse failure blocks the claimed suite run; it does not prevent a separately declared subset from being evaluated honestly.

When CI is in scope, confirm its command loads this same source and that relevant runtime/prompt/model changes trigger the intended checks. A green loader unit test or a maintained Markdown document alone does not establish coverage. Save the loaded inventory and case version with the run.

## Outcome and coverage

Confirm that success measures the requested outcome. A proxy needs an explicit limitation and a final check against the real outcome when feasible. Identify whether the task is meant to test an outcome or a particular mechanism; tool use is not automatically required when a valid answer can be produced another way.

Include ordinary successes and legitimate no-action cases as well as failures. Check duplicates, related incidents across splits, class imbalance, missing inputs, stale keys, and label provenance. At scale, inspect all rows programmatically and closely read a representative sample. Use human-verified keys where available and allow defensible alternatives. Generated labels remain provisional. Do not give the subject investigative hints it would not normally receive.

For detection or classification, inspect the confusion matrix and report relevant precision, recall, and false-positive rates with class counts. Undefined ratios remain undefined. Include cases where an action is warranted and where it is unnecessary so an always-act or never-act policy cannot win by construction. Compare against a meaningful simple baseline. A deliberately balanced diagnostic suite does not estimate production accuracy without a justified population weighting.

## Model-judge calibration

Hide candidate identity and prestige labels such as "human" or "reference" from comparative judges. Check sensitivity to presentation order and length with matched examples where these should not change the verdict. Record possible self-preference when the judge is also a subject model; propose an independent check for close decisions without silently replacing the chosen judge.

Validate against independently reviewed labels when available and inspect disagreements, including grader false positives and false negatives. Agreement with synthetic labels is provisional, and a different model family alone does not validate a judge. Choose any acceptance threshold for the actual decision rather than importing a universal agreement percentage. Freeze pairwise references; changing them requires a new grading condition. If variation across outputs is a task requirement, assess it across the set because isolated pairwise judgments cannot establish diversity.

## Runtime and evidence

Exercise the actual subject entry point or explain adapter differences. Probe the relevant tool, memory, retrieval source, skill, or setting through the same path the eval uses. Verify effective configuration and nested-agent settings where applicable. A config file alone does not prove activation.

Check capabilities required by the selected cases before expanding the run. Verify credential presence without printing secrets, and use the smallest authorized probe through the actual retrieval/tool path to distinguish working access from a plausible empty response. Check the effective database/data source, intended read/write boundary, provider route, and relevant feature/context injection. Do not require unrelated credentials or repair an intentionally unavailable dependency in a failure scenario. Record intentional degraded modes separately from unexpected setup defects.

Inspect the assembled evaluator input, not just the runner's saved files. It must contain the evidence needed for each claim: actual tool arguments and results, source URLs/dates, context, and outputs from every escalation round. Resolve offloaded content into durable artifacts before temporary files disappear. For large traces, select relevant evidence with pointers to the preserved full record and expose truncation; never silently treat a preview as complete evidence. Apply the same check to parent-assistant review and paid judges.

For recorded-evidence comparisons, exercise both the initial retrieval and escalation paths to confirm they remain frozen. A second round that reaches live services breaks that condition. Verify replay rows cannot enter live-success or live-latency aggregates. Confirm the selected configuration through live execution when the intended claim depends on retrieval, writes, or integration behavior.

Check fresh state and fixture isolation. Run meaningful positive and negative controls through the runner and grader, including an explicit negative answer versus missing output when "none" is valid. Inspect baseline passes and failures for incorrect keys, grading shortcuts, inaccessible artifacts, or mismatched evidence. Verify score, output, trace, usage, and timing belong to the same attempt.

Keep requested and returned model identities. Explain documented alias resolution; unexpected substitution invalidates that condition. When identity cannot be verified, report the limit. Keep hidden keys and grading artifacts outside subject access, including tools and filesystem mounts. Hash checks alone do not isolate them.

## Calibrate checks against meaningful errors

Use code for unambiguous constraints and retain the exact counting/parsing convention. Reuse existing checks when they protect the same contract. Sentence segmentation, natural-language arithmetic, and whether a number is a key metric can be ambiguous; define their treatment before generation instead of inventing a rule to rescue one answer.

Run relevant controls through the same evaluator path: a supported answer, a plausible contradiction, an unsupported citation, and missing or malformed evidence. Adapt these to the domain; no fixed control count is required. For numeric tasks, a correct table with a reversed conclusion should fail factual support. A URL present in evidence but unrelated to the claim should not pass attribution. For action tasks, a claimed action without the required persisted state should fail completion. Include a defensible alternative conclusion so the grader does not merely prefer the reference wording.

If evidence is present in storage but missing from the judge request, repair delivery and regrade the saved answer under a new version. If the source itself is absent, mark the affected criterion unverified or classify the limitation under the case contract. Do not ask a judge to infer the missing evidence. Parent-assistant labels are provisional; disclose candidate authorship and identity visibility. Preserve criterion results so a format miss and a critical factual error remain distinguishable even when both make overall success false.

## Failures, retries, and resume

Declare attempt and retry semantics before the run. Record transient service failures separately, cap retries with backoff, and apply a total task timeout. A case that eventually passes after extra attempts must not look like first-attempt success. If production retries are part of the tested behavior, grade that complete policy and include its resource use.

Separate evaluator errors and invalid environments from subject failures. Do not automatically exclude refusals, malformed answers, truncation, or exhausted task budgets: determine whether they violate the task contract or expose a setup defect. Preserve both the planned denominator and usable observations. Differential missingness can invalidate a comparison even when every remaining grade is correct.

Persist each completed attempt before the batch ends using atomic records or an equivalent recoverable format. Key executions by configuration, case, repetition, and attempt; version grades and reporting-subset membership separately. Resume only completed records with matching configuration and input hashes. Retain failed attempts and charges, and reuse saved outputs after judge errors. For a new or materially changed runner, or a long/costly run, use a small local interruption/resume control to verify records survive without duplicate execution and changed inputs invalidate reuse. A triage result reused in a full regression set is still one execution.

Check where timeouts actually apply, including inner application deadlines and blocking/nested work. A larger outer timeout does not override an earlier inner deadline. Keep retrieval failures, application timeouts, malformed answers, and evaluator failures distinct. Preserve end-to-end user failures even when a conditional answer-quality score excludes unusable runs; show both denominators and exclusions.

Verify limits with local controls before costly execution: refuse the next call before crossing a hard cap, include nested calls and retries, and retain unknown/canceled usage conservatively. Report reservations separately from billed or estimated cost. Reuse the cumulative ledger after restarts. Document adjustable batch sizes and hard limits separately; unused authorization does not extend a declared hard limit.

## Measurement and sensitivity

Recompute aggregates from per-case records and declared weights. Check units, denominator, missing values, and implausible constants. Distinguish real zero values from missing-field defaults. Retain end-to-end subject timing including tools and retries; optional model-call latency is a separate measure. Keep judge and simulator overhead separate.

For cost or latency comparisons, declare cold-start versus warmed execution, concurrency, and cache policy. Balance or randomize candidate run order when feasible, and record cache usage and service conditions. Unexplained warm-cache or time-of-day differences limit attribution to the candidate. Preserve the setup that represents intended use rather than clearing every cache by default.

Before hill-climbing, compare available headroom, the smallest useful change, and observed variability. Repeat at the source of uncertainty: new subject executions for generation noise, new builds for generated artifacts, or new judgments for grader noise. Repeated scoring of one build cannot reveal build variance. With insufficient observations, report unresolved sensitivity instead of inventing a confidence interval. More repetitions do not replace independent cases or fix a saturated metric.

Report concrete findings with evidence and their effect on the decision. Classify each relevant check as verified, failed, or untested. Block claims that depend on failed checks, repair the responsible component within scope, and preserve old grades. A rubric or fixture repair is a new measurement version, not improved subject performance.

Sources and adaptation choices are recorded in [source notes](source-notes.md).
