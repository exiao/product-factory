---
name: improve-workflow
description: Improve an existing coding-agent workflow through trace-grounded diagnosis and bounded baseline-versus-candidate checks. Use for requested improvement loops; trace inspection alone does not authorize edits or repeated paid experiments.
---

# Improve a workflow

Find a consequential recurring miss, make the smallest supported change, and check whether it improves the work the user cares about. Reuse the existing workflow and evaluation system when available.

## Diagnose before changing

Use [inspect-traces](../inspect-traces/SKILL.md) to reconstruct the request, context, agent choice, tool results, outcome, and correction. Seek counterevidence before naming a recurring pattern. A targeted failure sample can explain a mechanism but cannot establish its frequency.

Distinguish missing context, incorrect task understanding, skill instructions, execution environment, tool behavior, and output quality. Current instructions may already contain a fix for an older failure; verify that the agent found and followed them before adding more text. Keep project decisions in the project record and reusable guidance in the owning skill.

An inspection-only request returns findings. A request to improve authorizes scoped local changes, but does not authorize external publishing, new services, production writes, or unbounded experiments.

## Define the comparison

Choose representative tasks with observable outcomes and the user's quality criteria. Use [acceptance-criteria](../acceptance-criteria/SKILL.md) for an unresolved finish line. Include relevant failure and recovery paths; separate usefulness, factual quality, cost, latency, and repeat corrections rather than treating one metric as the whole outcome.

For a simple reversible improvement, one baseline and one candidate may suffice. Before repeated or costly runs, establish the permitted resources, run limit, success criterion, and stop condition from the user's task; ask about consequential gaps. Do not infer a paid budget or create an automation from the phrase "improve over time."

Preserve the starting version, inputs, environment, output, and observed failures. A historical trace is diagnosis evidence, not a reproducible baseline unless its relevant state can be recreated. If the baseline cannot run, report that limit instead of manufacturing a gain.

Cases derived from the diagnosed traces are development or regression cases. Use a separate held-out sample for a generalization claim and keep expected answers and diagnosis out of executor inputs. If no independent sample exists, limit the verdict to the exercised cases.

## Make and evaluate one candidate

Change the context, skill, tool, model, or environment that the evidence implicates. Keep other conditions comparable where possible. Use [build-skill](../build-skill/SKILL.md) for a supported skill revision and the existing verification workflow for executable changes.

Run the agreed tasks through the actual agent or tool workflow when the question concerns agent behavior. Metadata validation or an agent reciting the new instruction cannot prove better execution. Have the evaluator use the criteria and actual outputs rather than the candidate's claimed improvement. Inspect disagreements and failures, including retries and integration work.

Keep a candidate only when the observed tradeoff meets the user's goal. Revert task-owned changes for a rejected candidate while preserving unrelated work. A failed candidate can still narrow the diagnosis; stop when the agreed limit is reached rather than repeatedly strengthening adjectives or adding rules.

## Deliver the evidence and next action

Use the existing project record for baseline and candidate versions, source cases, changes, comparison results, and the keep/revert decision. Distinguish structural checks, exercised behavior, and untested generalization. Report failures and actual resource use when available; do not claim saved cost or time from model prices alone.

Publish, deploy, or install the accepted change only within the user's existing authorization. New runs or recurring collection require their own scope. The result is an evaluated workflow change or a grounded inconclusive result, not a claim of automatic learning.
