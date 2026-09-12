# Trigger evaluation and description improvement

Use this for a skill that loads on unrelated requests or fails to load for its intended job. This is routing evaluation, separate from task quality after invocation. Native skill creation stays with skill-creator; this reference owns measured routing optimization.

## Build a discriminating case set

Collect natural user requests that should invoke the skill, requests for neighboring skills that should not, ambiguous cases requiring context, and direct invocations as controls. Include paraphrases from real usage rather than only the exact trigger phrases in the description. Preserve the available skill catalog and relevant conversation context. Label uncertain intent separately rather than forcing a positive or negative answer.

Separate training requests used to edit the description from held-out validation requests. A directly named skill tests explicit invocation; it does not establish automatic discovery recall. Include positive and negative controls whose runtime behavior is known. If both fail, investigate the harness before changing descriptions.

## Observe the actual runtime

Use fresh execution contexts with the same candidate catalog, tool access, user request, and configuration. Present the request without naming the target skill when testing automatic discovery. Observe an actual skill-loading event or a trace showing the target entrypoint read. The agent saying “I would use skill X” is not invocation evidence. Record target skill path/name, loaded event, runtime/model configuration, run ID, and raw trace reference.

If the runtime cannot expose loading, mark the case unknown or run a clearly labeled simulated routing exercise. A simulated choice is useful for diagnosing wording but cannot pass a live-trigger gate. Do not use a Claude `.claude/skills` registration probe to claim Codex discovery works. Do not mutate global installed catalogs to isolate an experiment; use a supported sandbox/workspace mechanism or report that isolation is unavailable.

## Score and diagnose

Add `should_trigger: true/false` to case records and `triggered: true/false` to observed successful runs in the [experiment schema](experiment-toolkit.md). Missing observations stay unknown. The analyzer reports TP, FP, TN, FN, precision, and recall, excluding sealed test cases. Undefined precision/recall is null, not perfect performance. Separate explicit invocation controls from automatic routing cases in the report.

Inspect false positives for broad overlapping job descriptions and false negatives for missing intent categories or hidden dependencies. Change the smallest category-level wording that addresses the failure. Avoid appending one phrase per missed query. Evaluate both routing directions and downstream task quality: a description can improve recall by loading everywhere while making the system worse.

## Blind comparison and benchmark review

For content-quality comparisons, anonymize and randomize candidate labels before judging when practical. Give judges the task, rubric, and outputs with necessary evidence, not the optimizer's preferred answer. Retain mapping and RNG seed outside judge inputs. Use deterministic checks for concrete requirements and calibrated human/LLM review for subjective criteria. Report disagreement, excluded cases, and workload changes.

Record per-case scores and critical-case verdicts before aggregate means. Show paired differences, repeated-run variability, failures, latency, and measured cost. Do not combine unrelated datasets into a single apparent win or treat reportless/canceled runs as passes. The local review page helps inspect results; it does not replace raw artifacts or a human decision.

After selecting a description, freeze it and run the sealed final cases once if available. Deliver the artifact diff, before/after confusion counts, exact runtime tested, task-quality regressions, and evidence limits. Install only under the user's existing authorization.
