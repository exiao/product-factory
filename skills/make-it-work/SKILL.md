---
name: make-it-work
description: Own delivery of an agreed outcome through implementation, scoped reviews, fixes and runtime verification. Use for make-it-work requests and Software Factory delivery handoffs; unresolved product direction stays with Software Factory.
---

# Make it work

Build the full agreed outcome, prove it works, and fix it until it passes.

## Build

Reuse the agreed outcome, original and detailed criteria, evidence plan, current artifacts, exclusions and authorization from the request or Software Factory handoff. Own implementation, integration, review selection, fixes and completion reporting in the same task. Map each requirement to evidence from the actual configured workflow and its downstream result. Use [$program-design](../program-design/SKILL.md) only when code structure needs a decision. Build coherent slices and run the implementation checks.

If evidence or feedback reopens the audience, problem, mechanism or agreed scope, return that specific decision to [$software-factory](../software-factory/SKILL.md), then resume delivery from its updated agreement. Do not repeat settled discovery or treat missing evidence as approval. A new product's prototype does not prove the implemented outcome.

Use goal tracking only when available and explicitly requested under the runtime's rules; reuse a matching goal. Otherwise track criteria and completion in the existing task record. Do not create another task, board or automation as a side effect of delivery.

## Review

Select reviews from the changed behavior and original criteria, not a fixed quota. State the selected coverage briefly in the existing record. Reuse still-applicable evidence and combine overlapping checks; changes or unresolved failures require affected-path rechecks.

| Change | Required coverage |
|---|---|
| Contained code, CLI, backend or configuration change | [$code-review](../code-review/SKILL.md), relevant repository checks, and [$verify-feature](../verify-feature/SKILL.md) on the actual affected workflow, including a realistic failure or recovery path. |
| Interface or interaction change | The coverage above plus relevant usability, accessibility and visual checks through [$ui-lint](../ui-lint/SKILL.md) or [$impeccable](../impeccable/SKILL.md). Inspect the changed states and exercise their controls; a backend-only fix does not need a visual review. |
| New user-facing product or substantially new user journey | Applicable coverage above plus a representative end-to-end task and [$synthetic-userstudies](../synthetic-userstudies/SKILL.md) for comprehension and usefulness hypotheses. Reuse a sufficient walkthrough of the current version; preserve an explicitly requested alternative method and report its limits. |

Use independent reviewers for selected reviews when subagents are available and delegation is authorized. Give them the original request, criteria, artifact version and execution setup without coaching a verdict. Delegate bounded independent work in parallel; reviewers sharing a browser or computer session take turns. If independent review is unavailable, perform the applicable checks directly and disclose the limit instead of blocking unrelated work or claiming an independent pass.

Use deterministic checks for fixed contracts, browser automation for repeatable interactions, and agents for exploration and judgment. Synthetic reactions remain hypotheses, not customer evidence. Preserve approved design choices while fixing observed obstacles. Use [$ci-slopgate](../ci-slopgate/SKILL.md) only if a quality gate needs repair. Unit tests alone do not prove the configured workflow; record screenshots or logs from actual execution. Do not count an unrun review as a pass.

## Fix and recheck

For each review, record what passed, what failed, and the evidence. Reproduce disputed findings.

For consequential or recurring failures, have verification preserve a replayable regression case using the [failure-to-eval handoff](../verify-feature/references/failure-to-eval.md) when practical. Give reviewers the task, safe starting environment, and evidence needed to run it; keep expected answers and prior diagnoses separate from executors. Reuse relevant cases on the final version. Do not create a suite for every small fix or start a skill-optimization loop unless that work is in scope.

Keep ownership of authorized fixes when invoking other skills: their review reports feed this fix-and-recheck loop. Fix failures that prevent the agreed outcome, including pre-existing defects in that path, then have reviewers recheck the fixes and anything else they affect. Keep repeating until every relevant review passes on the final version. Don't lower the success criteria to get a pass.

If something blocks a review, explain what is missing and keep working on what you can.

When waiting for a PR, inspect checks within the active task and fix authorized failures. Schedule recurring checks only when the user explicitly requests follow-up and the runtime supports it; follow that cadence and stop condition. A pending CI run remains pending, not passed.

For improvement claims, compare equivalent workloads over the requested scope, including failures and retries; distinguish component gains from whole-job results.

Finish when the agreed outcome is delivered and all applicable reviews pass on the final version; complete an active matching goal only under the runtime's rules. Deployment is required only when it is part of the agreed finish line; verify it with [$verify-deploy](../verify-deploy/SKILL.md). Report criterion status, evidence links or artifact paths, and remaining limitations. Existing tests and CI count for what they demonstrate; do not require production deployment for a local change.
