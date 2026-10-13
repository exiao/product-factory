---
name: hill-climb
description: Improve a measurable system or artifact through bounded baseline-and-candidate experiments. Use for hill-climbing, autoresearch, or iterative optimization of prompts, skills, code, tool configurations, retrieval, and generated artifacts against an evaluator; not routine edits or eval creation alone.
---

# Hill climb

Keep changes that demonstrate useful improvement while preserving required behavior. Optimize a copy, retain the starting baseline, and return the best supported candidate. Start bounded jobs without a separate confirmation step. A request to optimize does not authorize deployment, publication, or unrelated changes.

## Continue within the authorized goal

Distinguish a user-set overall budget or stop condition from an agent-chosen batch limit. Batch limits bound individual runs; they are not approval gates. When a batch fails, reaches a plateau or exhausts its allowance while the authorized goal remains unmet, diagnose the evidence, declare the next bounded batch and continue without asking for renewed permission. Preserve the original baseline, rejected attempts and cumulative usage across batches. Version measurement repairs and retire consumed holdouts before making further improvement claims.

If the user says to keep going until finished, continue these bounded batches until the outcome is verified, the user stops, an explicit user-set overall limit is reached, or a genuine access or correctness-critical information blocker prevents progress. Do not invent an overall cap and then ask the user to extend it. Failed candidates, missing preferred budgets, evaluator repairs and the need for another round are routine authorized work. Approval is still required where execution permissions or spending rules below require it; continuing optimization does not expand those permissions.

## Define the experiment

Inspect the target and its actual execution path. Identify the outcome to improve, the evaluator and run command, allowed files or settings, fixed conditions, critical regression cases, and finite iteration/time/resource limits. Reuse the user's decisions; choose and state reasonable defaults for unspecified experiment details, then proceed. A missing preferred budget, evaluator, or human rating is not a reason to request run confirmation. Use clearly labeled provisional judgments for a limited pilot when appropriate; never present them as human ratings or established correctness. Ask only when missing information prevents a meaningful experiment, and continue independent work.

Choose an explicit objective and direction, such as higher task success, lower cost per completed task, or lower end-to-end latency. Specify the quality floor and other constraints, the smallest useful gain, candidate selection rule, and stop conditions before running. Keep quality, cost, and time separate rather than hiding tradeoffs in an invented composite. Unknown cost cannot establish a cost reduction. Model migration is a comparison of configurations; record what else changes with the model.

Find an existing evaluator before building one. If none measures the intended outcome, use [build-eval](../build-eval/SKILL.md) to prepare a small runnable evaluation. Resume optimization after its controls and authorized baseline work. A script, fixtures, and inspectable results can be enough. If an evaluator cannot be run, deliver preparation and name the blocker rather than claim improvement. For a behavioral proxy, state its limits and reserve budget to verify the selected candidate on the real outcome.

Use the user's existing subscriptions through the local Claude CLI or Codex CLI for subject execution, analysis, model grading, calibration, retries, and final verification. Follow [build-eval's routing rules](../build-eval/SKILL.md) to verify subscription authentication and exclude API/proxy overrides. API spending, including TypeSafe/Jev, OpenRouter, direct APIs, and paid proxy fallbacks, requires explicit user confirmation; a configured key or a helper's fallback policy is not approval. Reuse confirmation already given for that service and scope. Keep finite call/time limits and usage records even for subscriptions and approved API routes. Do not silently replace a selected model or evaluator when a route is unavailable.

## Establish trustworthy measurements

Read [evaluation readiness](../build-eval/references/evaluation-readiness.md) before relying on a new or inherited evaluator. Reuse valid checks for the same versions. Repair confirmed measurement defects before optimizing the subject; preserve prior records and rerun or regrade affected comparisons under a new version.

Freeze task inputs, success criteria, evaluator version, split membership, and fixed execution conditions. Keep evaluator code, answer keys, hidden fixtures, and selection rules outside the candidate's editable scope and the subject's readable context. Hash material inputs and dependencies. A hash detects changes; it does not enforce access isolation. A legitimate evaluator repair starts a revised comparison, not a candidate win.

Separate development cases used for diagnosis from validation cases used for selection. Group related incidents and near-duplicates in one split. Reserve an unseen final test set when available, and open it only after selection. Repeatedly consulting validation scores adapts to that set even without reading its traces. If validation details guide an edit, treat those cases as development data thereafter and version the experiment. With too few cases, run an explicitly labeled pilot and limit claims to the observed cases.

Snapshot and run the unchanged baseline before editing. Save outputs or produced artifacts, action traces, grades, usage, and timing from the same executions. Estimate variability at the level that actually changes between runs. Repeated grading of one output does not measure generation variance; repeated reads of one generated index do not measure rebuild variance. If noise or a metric ceiling obscures the smallest useful gain, propose an affordable measurement change or report that the current experiment cannot resolve it.

## Iterate within the budget

1. Inspect development failures and successes, including actual artifacts and action traces. Identify a supported cause. Separate subject mistakes from missing context, environment defects, evaluator errors, and unresolved preferences.
2. Propose one interpretable change with a predicted effect on the objective and constraints. Explain why it should help the intended workload beyond the inspected cases. Reject rules tied only to benchmark wording, paths, or answers; distinguish real deployment requirements from fixture accidents. Prefer a smaller correction or deletion when sufficient. Keep a candidate snapshot and diff separate from the current best. Several coordinated edits can test one hypothesis; unrelated changes form a bundled comparison.
3. Run matched cases with fresh contexts and equivalent starting state. Give subjects normal inputs and the candidate, without diagnosis notes or expected answers. Verify the changed artifact or setting actually reaches the running system, including nested agents when relevant.
4. Compare against the current best on the predeclared validation schedule, and retain the original baseline for the final comparison. Check each critical gate and the objective in its declared direction. Reject a known critical regression. Treat missing, noisy, or incompatible evidence as inconclusive; never relax the gate or remove hard cases to create a win.
5. Record the hypothesis, parent, diff, per-case results, resource use, keep/reject/inconclusive decision, and reason. Preserve rejected candidates. Checkpoint completed run keys and remaining budget so a restart neither loses evidence nor spends the same allowance twice.
6. Continue from the best supported candidate until the target is met, the batch budget is exhausted, the batch plateau rule applies, a dependency blocks execution, or the user stops. Existing authorization covers routine iterations and subsequent bounded batches within scope. At a batch boundary with an unmet goal, diagnose remaining failures and start the next useful batch under the continuation rules above.

When progress stalls, make no candidate edit while grouping remaining development failures by supported cause: missing capability, available instructions not followed, missing context, evaluator or environment defects, or unresolved noise. Link each group to evidence and choose the next action within the remaining batch budget, or declare the next bounded batch before running it. Do not read sealed cases for this diagnosis, quietly remove failures, or change a completed batch's stop rule after seeing its results. Evaluator repairs require versioned regrading; gains from those repairs are not candidate improvements.

Independent analysis or candidate branches can help when delegation is authorized. Give each worker a separate output directory, development evidence only, a concrete hypothesis or deliverable, and a share of the total budget. Measure a merged candidate as a new artifact; do not average its parents' scores. Keep writes to shared experiment state under one owner.

Use the project's runner and result format. For checkpoint fields and comparisons, read [experiment records](references/experiment-records.md). Keep long runs observable and give concise updates with measured progress, decisions, and remaining budget.

## Verify and deliver

After selection, evaluate the original baseline and selected candidate on the sealed final set once under matched conditions. Repetitions may be predeclared; selecting another candidate or tuning from these results consumes the holdout. Report regressions and retain the baseline when the acceptance rule fails. If no sealed set exists, say the result is a development or validation improvement, not independent evidence of generalization.

Deliver the selected artifact or unchanged baseline, the meaningful diff, measured quality/cost/time comparison, critical-case results, evidence paths, and remaining failures. Report absolute values alongside deltas and separate descriptive results from statistical claims. Preserve a resumable record of rejected attempts and measurement changes. Apply or install the selected result only within the user's authorization; do not silently replace a live system.

For source influences and deliberate differences, see [source notes](references/source-notes.md).
