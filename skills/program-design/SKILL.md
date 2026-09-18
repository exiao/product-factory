---
name: program-design
description: Design code structure, interfaces, control flow, and implementable slices before a complex or structurally risky change. Use when the shape of the code needs a decision or material unknowns need mapping, not for routine small edits.
---

# Program Design

The user's current instructions take precedence. Preserve existing authorization, scope, and prior decisions; this skill does not authorize additional publishing, deployment, spending, or messages.

Decide the shape of the code before implementation makes expensive assumptions permanent. This is code-level design: call paths, ownership, interfaces, and coherent increments.

## Choose proportionate depth

Skip a separate design exercise for copy/config edits, dependency pins, straightforward scripts, or a localized bug with an obvious fix. A new module, storage contract, queue, pipeline stage, frequently reworked area, or competing architectural approaches may justify design even for a small diff. Line count and churn are signals, not hard gates or quotas.

Inspect the existing implementation and similar capabilities first. Reuse may eliminate the need for a new module. Read relevant git history when repeated fixes suggest an unresolved structural problem; do not launch a whole-repository audit by default.

## Optional uncertainty mapping

When ambiguous requirements, unfamiliar code, a reference port, or a risky assumption could change the design, use [uncertainty mapping](references/uncertainty-mapping.md). Record established facts, open questions, tacit assumptions, and discovered risks in the existing design note. Resolve what the evidence can answer, ask only for material missing decisions, and continue authorized work without mandatory stages or quizzes. Skip this mode when the change is already understood.

Use [$domain-modeling](../domain-modeling/SKILL.md) when the uncertainty concerns business terminology, concept boundaries, or domain rules rather than code structure. Use grilling (optional, when installed) for an explicitly requested interview.

## Draft the useful artifacts

Use one short design note, selecting only artifacts that clarify the change:

1. **Call-tree diff:** show new/removed branches and the control path for orchestration, retry, queue, or lifecycle changes.
2. **File-tree diff:** show code ownership, new files, and touched modules.
3. **Types and signatures:** specify important inputs, outputs, error contracts, persistence effects, and invariants. Use pseudocode where implementation syntax would distract.
4. **Vertical slices:** define independently inspectable behavior and the evidence for each increment. Respect dependency and compatibility constraints rather than mechanically implementing database, API, then UI layers.

For example:

```text
consume_jobs
  claim_job
  classify_failure(job) -> retryable | fatal
    retryable -> mark_retry(job_id, attempt)
    fatal -> preserve_failure(job_id, reason)
```

Keep slices usable and reviewable; do not defer security, data integrity, or essential failure handling to a later slice that leaves an unsafe intermediate state. Label mocked behavior explicitly.

## Handoff

Keep intent, agreed criteria, exclusions, structural choices, and verification together in one accessible plan. Preserve repository conventions and use the requested path. Avoid a chain of summaries that loses the original requirement. Resolve material choices with the user when necessary; do not force approval of routine implementation details already authorized.

A builder should be able to tell which interfaces change, where the call path changes, and what the first slice proves. An independent review can help for substantial uncertainty, but no permanent role or separate card is required. Keep plans editable as evidence changes; record a significant departure instead of silently treating the old design as implemented.
