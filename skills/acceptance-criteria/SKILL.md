---
name: acceptance-criteria
description: Write testable acceptance criteria and evidence plans for an agreed outcome. Use for defining done, acceptance tests, requirements handoffs, or explicitly requested goal-tool setup.
---

# Acceptance Criteria

The user's current instructions take precedence. Preserve existing authorization, scope, and prior decisions; this skill does not authorize additional publishing, deployment, spending, or messages.

Describe what must be true, not how to code it. Read the request, current behavior, approved scope, and exclusions first. Use [$product-vision](../product-vision/SKILL.md) clarification only if missing intent materially prevents defining done.

## Focused modes and routing

The exact mode names below are conversational requests, not shell commands or standalone skills. Use the narrow mode when the request explicitly names it or clearly asks for that operation. A broader request already authorized by the user may continue beyond the mode; otherwise keep the work local.

| Conversational mode | Target | Default output |
|---|---|---|
| `acceptance-criteria sharpen` | A named criterion or requirement that is vague, broad, or hard to test | Local annotation plus a before/after criterion, preserving its stable ID and source; a materially changed expectation is proposed until agreed |
| `acceptance-criteria assess` | Supplied evidence for a named criterion | Evidence-to-criterion assessment using supplied evidence only; mark missing or unobserved checks untested or blocked |
| `acceptance-criteria define` | The outcome that should count as done | Criteria for the agreed outcome, with evidence, status, and unknown or proposed thresholds clearly labeled |

When the user asks generally to define acceptance criteria, use `define` as the default mode. For a bare `$acceptance-criteria` invocation with no actionable surrounding request, use the available context only to offer 2–3 relevant mode suggestions with a short reason for each, then stop. When the surrounding conversation already supplies an actionable request, follow that request's scope instead of stopping for the menu. A review-only request is read-only. `assess` never invents an approved threshold, converts missing evidence into a pass, or treats an untested condition as satisfied. Read [focused modes](references/focused-modes.md) only after selecting one of these modes.

First distinguish the kind of success being defined, where the work calls for it:

- **Learning criteria** state the hypothesis, interpretable evidence, and decision it enables, including changing direction or stopping. Passing one does not establish the promised user outcome or authorize release.
- **User-outcome criteria** state what must be true for the agreed user promise to be delivered.
- **Release criteria** state the additional evidence or conditions required before release, such as operational readiness or risk controls.

Keep a learning milestone separate from an agreed delivery outcome; do not weaken a delivery criterion to make an experiment pass. If evaluating results without prior criteria, distinguish the learning supported by the evidence from proposed criteria for the next decision; do not retroactively invent a pass threshold. A diagnostic constraint, such as buying readiness, becomes a milestone requirement only when it is part of the agreed outcome.

For each promised behavior, write:

| Field | Content |
|---|---|
| Criterion | Stable identifier, starting condition, action, and independently observable expected result |
| Source | The request, agreement, or requirement it implements |
| Evidence | The input, surface, action, observation, and failure condition |
| Status | Proposed, agreed but untested, passed, failed, or blocked |

Given/When/Then is optional. Cover relevant normal, empty, invalid, permission, privacy, failure, and recovery cases; do not impose every category on every task.

For a user-facing everyday task, make care observable: can the intended user infer the available action without coaching, understand the feedback after acting, and identify the next step or completed state? Define the supporting observation where relevant; do not invent a delight score or treat a reviewer's intuition as measured comprehension.

Carry material situational constraints from the brief or empathy map into starting conditions and evidence plans. Check the decisive action and recovery under the relevant conditions, such as interruption or poor connectivity. Preserve evidence and hypothesis labels, propose unresolved conditions explicitly, and avoid a universal device or context matrix.

Replace vague adjectives with observable expectations. Mark missing thresholds, data contracts, or unresolved behavior as unknown and draft the rest. Never manufacture an approved latency target or file limit.

When a criterion depends on a metric, specify its unit and denominator, relevant population, observation window, data source, baseline or unknown, and what meeting the target means. Explain how the metric relates to the user outcome and whether that relationship is established or assumed. Include a guardrail when optimizing the metric could harm another important outcome, and label proposed thresholds explicitly. Do not require new instrumentation when existing evidence is sufficient.

Map all requested behavior to criteria. Preserve exclusions and exact conditions. Do not broaden “exclude hidden notes” into “exclude all notes.” Do not add production instrumentation solely to make verification convenient; existing test hooks or controlled fixtures may suffice.

When a milestone includes optional work, mark which agreed criteria are essential and which items are explicitly deferred. An unresolved essential criterion prevents declaring that milestone complete. A deferred item is not passed; moving an agreed requirement out of scope requires an actual scope decision.

Check whether the criteria can all hold simultaneously. Identify contradictory requirements, explain the consequence, and recommend a resolution. Keep unresolved criteria distinct from approved requirements.

Evidence must match the promise. An end-to-end user promise needs evidence across that path; unit tests support narrower components. For forbidden behavior, include an appropriate controlled negative check. Never contact real recipients or mutate production merely to prove a criterion.

When acceptance depends on an automated evaluator, check its suitability with representative cases, meaningful failure cases, and reference or human comparisons where available. Distinguish the evaluator's score from actual task success, and disclose unresolved validity limits. Keep evaluator implementation in specialist tooling; this skill defines what evidence is adequate.

For an automated evaluation, map each scored criterion to its observable evidence and verifier. Use deterministic checks for facts or state and anchored judgment for subjective quality. Calibrate with a known-good example and a plausible-but-bad example that exposes a meaningful failure; add a borderline case when the distinction matters. Explain the labels, record false passes, false failures, and unresolved disagreements, and keep calibration examples separate from held-out performance cases. Without trusted labels, mark calibration provisional. Never silently adjust a rubric to favor the current output.

Writing a criterion does not pass it. Record observed evidence for pass claims and access/setup limitations as blocked or untested. Do not weaken criteria to match an implementation unless the user changes the agreement.

Save the requested artifact using the project's documentation convention when needed. Hand off approved wording intact. Use [$verify-feature](../verify-feature/SKILL.md) to execute checks when verification is requested; defining criteria alone does not authorize building.

## Goal tool

Only when the user explicitly requests a goal or goal-backed work, turn the agreed criteria into one concise objective: outcome, scope, verification method, and measurable or binary completion threshold. Resolve material unknowns first; do not invent targets or create a goal for ordinary implementation work.

Call `get_goal` before `create_goal`. Reuse a matching unfinished goal; if it conflicts with the request, clarify rather than replacing it or marking it complete prematurely. Include the evidence standard and scope boundaries in the objective itself. Set `token_budget` only when explicitly requested.

When executing goal-backed work, mark completion with `update_goal` only after the criteria pass with observed evidence. Follow the tool's current rules for blocked goals; an unanswered question or exhausted budget does not mean completion. Do not create extra tracking files solely for goal setup.

Adapted from OpenAI's [$define-goal](https://github.com/openai/skills/blob/main/skills/.curated/define-goal/SKILL.md).
