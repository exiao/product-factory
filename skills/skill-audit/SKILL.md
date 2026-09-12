---
name: skill-audit
description: Audit and score a skill's routing, structure, coherence, dependencies, and maintainability. Use for skill reviews and drift checks; behavioral quality claims require execution evidence.
---

# Skill Audit

The user's current instructions take precedence. Preserve existing authorization, scope, and prior decisions; this skill does not authorize additional publishing, deployment, spending, or messages.

Evaluate whether a skill gives useful, reachable, scoped instructions. Distinguish structural quality from actual task performance; use [$skill-improver](../skill-improver/SKILL.md) for empirical optimization.

Read the entrypoint, inventory its resources, and follow relevant references, templates, and scripts. Do not read every vendored manual or binary merely because it exists. State the reviewed scope and any inaccessible resources.

## Audit workflow

For a full audit, read [the checklist and scoring rubric](references/checklist.md). It defines 27 items, their applicability, evidence, and score calculation. Use the relevant subset for a focused review; label its score as partial. Include a scorecard for a full audit unless the user requests findings only.

For codebase drift, reference health, prompt cost, usage, upstream comparisons, capability gaps, or consolidation, also read [maintenance procedures](references/maintenance.md). Read the relevant sections rather than loading unrelated maintenance workflows.

Recommend command tables, smaller operations, schemas or separate playbooks only when they reduce demonstrated ambiguity, review effort or unnecessary workflow. Their absence is not a defect by itself. For multi-mode skills, the checklist also provides an optional bounded behavioral spot-check; keep its execution evidence separate from structural conformance.

Evaluate these dimensions using the checklist:

- **Routing:** name and description identify a concrete job; triggers neither miss it nor attract unrelated tasks. Do not protect an ever-growing trigger list from scrutiny.
- **Scope:** instructions preserve user intent and authorization, distinguish review from mutation, and avoid creating extra tasks or publishing by default.
- **Coherence:** entrypoint, examples, references, and output templates agree. Required constraints are visible where used. A contradictory example is a real defect.
- **Dependencies:** paths resolve in the intended runtime; cross-skill pointers are valid only if the dependency actually exists. Validate promised content, not just a similar filename. Missing optional resources should have a reasonable fallback.
- **Evidence:** real system checks are retained where needed. A source read, rendered output, or observed API response is different from repetitive self-review. Limit success claims to what was tested.
- **Cost and maintenance:** remove duplicate explanations, stale workarounds, unnecessary fixed stages, and rules that only serve past unrelated cases. Brief reminders can be justified near an action. A small skill need not grow. Prefer deleting unnecessary alternatives over naming them in prohibitions: mentioning an option adds context the model must consider. Keep negative instructions only when they address an observed failure relevant to the skill; otherwise state the intended action or omit the rule.
- **Examples and scripts:** inspect entrypoints before running even --help; some scripts have side effects at import. Use safe isolated fixtures for warranted checks and report untested dependencies honestly.
- **Runtime/model fit:** verify current official documentation when a finding depends on product behavior or model-specific advice. Do not assert capabilities from old model names or benchmarks.

Use the installed [$skill-creator](../.system/skill-creator/SKILL.md) validator for format when available. It checks structure, not behavioral usefulness. For link checks, resolve relative paths from the containing file, distinguish local files from URLs and code examples, and inspect cross-skill references against the actual installed set.

## Report and fixes

Report supported findings with file/line or a short quote, consequence, and smallest useful fix. Rank by impact. Keep uncertain concerns separate with the evidence needed to decide. Use the checklist's scorecard: exclude unresolved and inapplicable items from the denominator and disclose both. A high structural score does not establish behavioral quality or cancel a critical defect.

An audit-only request ends with findings. When fixes are requested, make targeted changes, preserve behavior and user choices, and revalidate affected resources. Overlap can justify consolidation, but do not delete a separate skill or broaden the survivor's triggers without scope to do so. Do not create more skills just to repair one.
