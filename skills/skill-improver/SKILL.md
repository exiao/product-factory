---
name: skill-improver
description: Improve an existing skill through a bounded baseline-and-candidate evaluation loop. Use for measured skill optimization or autoresearch, not an ordinary wording edit or structural audit.
---

# Skill Improver

The user's current instructions take precedence. Preserve existing authorization, scope, and prior decisions; this skill does not authorize additional publishing, deployment, spending, or messages.

Keep changes that improve observed task performance while preserving required behavior. Start from the existing skill and optimize a copy.

## Establish an experiment

Read the skill and relevant resources. Use [$skill-audit](../skill-audit/SKILL.md) for structural problems when helpful. Distinguish obvious format repairs from hypotheses about better behavior.

Identify the target task, representative inputs, scoring criteria, execution model/configuration, critical regression cases, and a finite run/time/cost budget. Reuse supplied decisions. If an evaluator is missing, propose a small concrete set from real tasks and explain what it measures; do not demand a questionnaire or run an unbounded experiment. Obtain missing authorization for paid/external execution before dependent work.

Prefer observable pass/fail checks for factual requirements. For subjective output quality, use an anchored rubric or blinded comparison and disclose judge uncertainty; binary labels alone do not make taste objective.

Use separate training and validation inputs and, when enough examples exist, a sealed final test set. Record which inputs belong to each split. With few inputs, report a pilot and avoid generalization claims. Do not select a model merely because a historical skill named it.

Before the baseline, fix the rubric, critical regression gates, candidate selection rule, and stopping conditions. If these change, record why and rerun affected comparisons.

For a consequential or recurring observed failure, use [failure-to-eval.md](references/failure-to-eval.md) to build a replayable case before changing instructions. Reuse the project's case library and harness when available. A missing fixture or uncertain diagnosis is a limitation, not a reason to invent evidence.

## Run the bounded loop

Run each baseline and candidate case in a fresh context with equivalent starting artifacts and tool access. Record any differences you cannot control.

1. Snapshot the unchanged skill, its relevant resources, and the execution and evaluator configuration. Run the baseline before editing and save outputs, scores, relevant tool traces, and resource cost.
2. Diagnose concrete failures from the request, artifacts, and actual execution. Identify where behavior diverged; a score alone is not a diagnosis.
3. Propose one interpretable change. Consider deleting or narrowing a rule before adding another. Keep the candidate in a separate workspace copy.
4. Run the same training cases under comparable conditions. Give executors the request, skill, and raw artifacts, not the expected failure or optimization hypothesis.
5. Compare baseline and candidate on held-out validation. Preserve critical regression cases. Reject a known critical regression; label noisy or insufficient evidence inconclusive rather than lowering the gate to get a win.
6. Log the edit, hypothesis, scores, failures, decision, and cost. Keep rejected edits to avoid repeating them. Save a checkpoint after each completed comparison.
7. Continue within the agreed budget until progress plateaus, evidence is insufficient, a dependency blocks work, or the user stops. Existing authorization does not require approval after every iteration.

Repeated validation selection can overfit. Use paired cases and enough repetitions to understand variability. Do not claim statistical significance from a tiny run. Advanced candidate pools, statistical gates, or dashboards are optional when the scale justifies them; reuse a verified project harness rather than rebuilding one.

## Optional evaluation resources

- For multiple candidates, paired result analysis, checkpoints, or a local review page, read [experiment toolkit](references/experiment-toolkit.md). Its bundled analyzer checks recorded runs without launching models or promoting a candidate.
- For missed or excessive skill invocation, description optimization, or blind benchmark review, read [trigger evaluation](references/trigger-evaluation.md). Measure real runtime loading separately from a simulated routing choice.

## Final check and delivery

If a candidate is selected, evaluate it and the baseline on the sealed test set once after selection. Do not tune on final test results. If no test split exists, report that limitation. If results regress, report it rather than declaring improvement.

Deliver the accepted candidate, or retain the baseline if no candidate demonstrates improvement. Report the measured baseline/candidate comparison, critical-case results, meaningful changes, remaining failure modes, and evidence limits. Keep a concise experiment log and resumable configuration with the run artifacts; a live dashboard is not required.

Never silently replace the installed skill. Promotion requires the user's request or authorization to install the accepted result. A normal request to edit a skill does not require this experimental loop; use [$skill-creator](../.system/skill-creator/SKILL.md) for that smaller task.
