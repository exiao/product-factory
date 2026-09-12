# Audit checklist and scoring

## Contents

- Scope and evidence
- Structure: S1–S4
- Content: C1–C6
- Design: D1–D2
- Execution: E1
- Budget: B1–B2
- Instruction placement: P1–P3
- Maintenance and prompting: DP1–DP5
- Runtime fit: M1–M4
- Optional behavioral spot-check
- Scoring and report

## Scope and evidence

Inventory the entrypoint and resources. Identify the consuming runtime, relevant dependencies, and requested audit scope. Follow references needed to assess that scope; list inaccessible or unreviewed material.

Each item has one disposition: **Pass**, **Fail**, **Unknown**, **N/A**, **Out of scope**, or **Shared → primary ID**. Pass requires an actual check; absence of a discovered problem after skipping the check is Unknown. Use N/A when the stated applicability condition is absent, Unknown when applicability or evidence cannot be established, and Out of scope when the requested review excludes it. Give a reason for every exclusion. Prose-only skills, for example, receive N/A for E1 rather than free execution points.

A failure needs a file/line or short quote, evidence of the defect, its consequence, and the smallest useful fix. Separate observed behavior, source-backed conclusions, and hypotheses. Where an item has multiple applicable checks, a confirmed defect makes it Fail; without a defect, unresolved checks make it Unknown.

Use one primary item per root cause. Mention overlapping dimensions without deducting twice. If an item has independent checks, assess those normally; if its only finding is already counted elsewhere, mark it **Shared → primary ID** and exclude it from the denominator. Report material issues outside this taxonomy unscored rather than stretching a category to fit.

## Structure: S1–S4

### S1 — Frontmatter and routing (all skills)

Check supported frontmatter fields, name, and description against the installed runtime contract. The description should identify a concrete job and when it applies. Consider both missed triggers and attraction of unrelated tasks.

- Pass: a discriminating task description with valid runtime metadata.
- Fail: malformed metadata or wording that demonstrably routes an unrelated task into the skill.
- Evidence: validator output, runtime schema, or a concrete ambiguous trigger. Do not treat another runtime's unsupported field as a defect without checking the intended runtime.

### S2 — Progressive disclosure (all skills)

Keep shared decisions in the entrypoint and conditional detail in reachable references. Check whether the agent can find a needed resource without reading unrelated manuals. Use navigation aids for long references when they improve retrieval.

- Pass: entrypoint and reference links expose the relevant path clearly.
- Fail: essential steps are hidden in an unlinked resource or repetitive inline detail obscures the workflow.
- A file's length alone is not a failure; explain what navigation or context cost it causes.

### S3 — Resource purpose (all skills)

Check that shipped files support execution, examples, evaluation, packaging, or required documentation. Flag obsolete scaffolds and duplicates that create confusion. A README or extra directory is not inherently wrong; identify its actual cost or conflict.

### S4 — Organization and portability (all skills)

Check directory naming and paths against the intended installation. Preserve runtime-supported metadata directories. Fail required machine-specific paths that cannot resolve in the target environment; do not rename deliberate local configuration merely to enforce a preferred tree shape.

## Content: C1–C6

### C1 — Useful failure guidance (when known non-obvious pitfalls matter)

Check whether consequential known traps have a condition, consequence, and recovery or prevention. Pass when the guidance changes an action usefully. Fail an omitted trap only with evidence that it matters to this workflow. A dedicated Gotchas heading is optional.

### C2 — Signal relative to cost (all skills)

Look for generic tutorials, abandoned approaches, or explanations that add no decision-relevant information. Quote the removable passage and show why the remaining guidance suffices. Short reminders near an action can be useful. A small skill need not grow to earn points.

### C3 — Specificity and workflow control (all skills)

Match constraints to fragility: exact ordering for dependent operations, flexibility for judgment. Check for redundant approval pauses on authorized work, premature stopping after a plan, forced serialization of independent calls, or steps that hide blockers. Preserve user requirements and real dependencies.

- Pass: outcomes and checks are clear, and fragile actions have sufficient detail.
- Fail: a required sequence blocks an otherwise authorized task, or a fragile operation lacks the detail needed to execute safely.

For prescribed artifacts or stages, identify the uncertainty, decision or required evidence they serve. Flag a stage that adds work without serving the requested outcome. Permit justified smaller substitutes when they address the same uncertainty while preserving explicit deliverables, real dependencies, decision boundaries and evidence requirements.

### C4 — Coherence and duplication (all skills)

Compare the entrypoint, references, examples, and templates. Flag contradictory instructions and duplicate explanations that can drift. A one-line reminder is not equivalent to copying a full procedure. Select one canonical explanation and preserve constraints where they are used.

### C5 — Actionable instructions (all skills)

Check operational directives for identifiable actions, conditions, and success criteria. Flag vague commands such as “handle failures appropriately” when the workflow requires a specific recovery. Check unjustified absolutes and prohibitions; retain a restriction when its reason or relevant failure is clear. Prefer stating the intended action over enumerating unnecessary alternatives.

For a bounded operation, check that its target, contribution, reviewable result and stopping point are understandable. Distinguish inspection that reveals a gap from revision that changes the artifact. A broad promise such as “improve the result” needs a concrete operation when the user would otherwise have to invent the method.

Word counts, capital letters, and keyword matches are inspection aids, not evidence that a sentence fails. Read each hit in context.

### C6 — Comprehensibility (all skills)

Check whether a competent reader can follow the instruction without reconstructing missing context. Define non-obvious local terms; resolve ambiguous actors and pronouns; split passages that bury the action under qualifications. Quote the unclear passage and identify the missing information. Do not deduct again for a duplication already assigned to C4.

## Design: D1–D2

### D1 — Job and scope boundaries (all skills)

Check that the workflow serves a recognizable task and preserves user choices. Useful types include API reference, verification, analysis, automation, and scaffolding; these are examples, not an exhaustive taxonomy. Fail workflow expansion such as treating a review as authorization to delete sibling skills or publish results.

Where a useful narrow task falls within the skill’s remit, check that it can finish without triggering the full workflow. Conversely, a focused intermediate operation must preserve an already-authorized larger task and its finish line. Assess the actual request and dependencies; do not require every skill to support arbitrary fragments.

### D2 — Configuration, state, and composition (when these are used)

Check that required configuration is discoverable, persistent state survives expected upgrades, and dependencies exist in the consuming environment. For continuation summaries, preserve the goal, decisions, authorization, completed work, unresolved work, and identifiers needed to resume. Fail lost state or a mandatory missing dependency. Stateless prose without configuration, state or composition is N/A.

When outputs feed another operation, check that the handoff preserves original source references, evidence labels, stable identifiers where needed, constraints and unresolved assumptions. Flag hypotheses silently becoming facts, approvals becoming validation, or a narrow check becoming proof of the full promise. This applies to prose handoffs as well as persisted state; stateless prose without composition remains N/A.

## Execution: E1

### E1 — Executable artifacts and claims (when runnable instructions are shipped)

Inspect script entrypoints before running them, including imports and argument handling. Identify side effects and use isolated fixtures within existing authorization for checks of documented commands, expected outputs, and relevant failure paths. Audit scope does not authorize external writes. `--help` may have side effects and proves only startup/help behavior, not the task itself.

- Pass: checked commands and relevant safe fixture paths work, with the verification boundary stated.
- Fail: a documented flag, path, import, or expected result demonstrably fails.
- Unknown: required credentials, dependencies, or permitted execution are unavailable. Report what was read versus executed.
- N/A: no runnable artifacts or instructions. Do not require a script for a judgment task.

## Budget: B1–B2

### B1 — Discovery cost (when metadata is loaded during skill discovery)

Inspect what the runtime actually indexes. Measure that text, then assess redundant trigger enumerations and volatile detail. Fail supported waste or a runtime limit violation, not a universal byte threshold. If indexing behavior is unknown, keep the cost claim Unknown; routing can still be assessed under S1.

### B2 — Loaded context cost (all skills)

Measure the entrypoint and references actually required by the workflow. Check repeated explanations and mandatory irrelevant reads. Moving a file to references saves no context when the entrypoint still requires reading it every time. Report bytes or an explicitly labeled token estimate; assess the cause once if S2 or C2 already captures it.

## Instruction placement: P1–P3

Apply these to behavioral instructions and output templates; pure factual catalogs without behavioral rules are N/A.

### P1 — Constraints at the point of use

Check that templates and action instructions expose the constraints needed to use them correctly. A sample output violating a stated rule is direct evidence of a defect. Position alone, including an arbitrary percentage of the document, does not establish failure.

### P2 — Compatible behavioral rules

Check near-synonymous instructions for conflicting interpretations or needless repetition. Consolidate only when no distinct requirement is lost. Count the same duplication under C4 or P2, not both.

### P3 — Enforceable behavior

Check that hard requirements describe observable behavior or have a usable tool/state mechanism. “Track progress across sessions” needs persistent state or runtime support. Aspirational tone guidance may be legitimate; fail only when it is presented as an operational guarantee the skill cannot fulfill.

## Maintenance and prompting: DP1–DP5

DP1–DP4 apply to behavioral instructions. DP5 applies to every skill. Model-dependent conclusions also require the evidence rules under Runtime fit below.

### DP1 — Calibrated emphasis

Check whether emphasis communicates a real priority or creates conflicts through blanket urgency. Examine routing separately from behavior: trigger text is neither automatically defective nor exempt. Fail demonstrated conflicting or indiscriminate priority claims; uppercase words alone are not a defect.

### DP2 — Reasoning and API scaffolds

Inspect imposed reasoning formats, planning rituals, and API parameters against the actual task and runtime. Keep formats required by a consumer and sequences required by dependencies. Remove a scaffold only when evidence establishes redundancy, incompatibility, or harm; do not assume a newer model replaces every planning instruction.

### DP3 — Owned, applicable mitigations

Check whether workarounds still address an applicable failure. Use current source or execution evidence for claims about progress updates, formatting, tool support, or model behavior. An older model name or dated example is a lead to investigate, not a failure by itself. Preserve explicit user preferences.

### DP4 — Outcomes and justified bounds

Check arbitrary choreography, output floors, and caps against the requested task. Preserve user limits, schema constraints, rate limits, and method controls such as changing one variable at a time. Fail a bound when a concrete required outcome cannot fit it. Unknown purpose or harm remains unscored.

### DP5 — Factual and dependency drift

Verify required paths, command flags, configuration facts, and referenced content against the target environment. History may explain a rule, but cannot prove current validity. Resolve relative links from the containing file; a same-named file elsewhere does not repair a missing target. Use the maintenance reference for broader drift work.

## Runtime fit: M1–M4

Record the consuming model and runtime, including relevant fallbacks. For claims about capabilities or tendencies, verify current official guidance for that model and cite the URL, section, check date, and applicability. A local observation needs reproducible conditions; a third-party prompt snapshot is an example, not proof of model-wide behavior. If evidence is unavailable, use Unknown instead of deleting guidance based on intuition.

### M1 — Verification proportional to evidence (when checks are prescribed)

Distinguish self-rereading from observing the real system and confirming required artifacts exist. Preserve runtime tests, readbacks, and independent review gates. Fail unconditional repeated checking only when the work is redundant under the actual contract; a required test remains required. Do not assume a model automatically verifies correctly.

### M2 — Delegation fit (when delegation is prescribed)

Check whether work is independently assignable, whether workers can act without mutable-state conflicts, and whether coordination cost is appropriate to the task. Respect the user's delegation preferences. Fail unsupported fan-out or contradictory coordination requirements with concrete evidence; do not impose a universal agent count or model-specific rule.

### M3 — Finding coverage (for review, audit, and critique skills)

Check whether severity filters or numeric caps suppress findings the user requested. A top-three summary can be correct when that is the request; a complete audit should retain required findings even when its summary is brief. Evidence thresholds are legitimate. Constraints on method do not inherently limit reported findings.

### M4 — Deliverable proportionality (when output shape or length is prescribed)

Check whether mandatory sections force empty boilerplate or whether output limits omit required evidence. Prefer task-sized reporting and omit empty sections. The absence of a word ceiling is not automatically a defect. Assign output-bound root causes to DP4 or M4 once.

For targeted reviews and revisions, check whether findings stay adjacent to the affected passage, control or criterion and whether changes remain inspectable. Prefer local annotations or before/after excerpts when whole-artifact regeneration would obscure the result; preserve full deliverables when requested or needed by the consumer.

## Optional behavioral spot-check

For a multi-mode skill, a bounded execution check can resolve uncertainty about scope or evidence handling. Use it when useful within the audit’s authorization; it is not required for a structural score. Select relevant cases rather than imposing a fixed suite:

- A narrow review request.
- A narrow edit request.
- A delegated outcome containing a focused intermediate operation.
- A claim supported only by insufficient or synthetic evidence.

Give the executor the request, skill and minimum raw artifacts, without the intended answer or suspected failure. Use a fresh context and isolated artifacts for each independent case so evidence and assumptions cannot leak between cases. Preserve context within the delegated-outcome case. Keep side effects within authorization.

Inspect actual outputs and actions for scope, authorized continuation and preservation of uncertainty. Record the inputs, runtime/model, observed results and execution limits. Attribute supported findings to the existing checklist items without adding points or double deductions. Source inspection establishes what instructions say; a spot-check establishes only the behavior observed in those cases, not general improvement or automatic discovery reliability.

## Scoring and report

There are **27 possible items**: S 4, C 6, D 2, E 1, B 2, P 3, DP 5, M 4. Use equal weights for checklist coverage, then rank defects separately by impact.

- Earned points = number of Pass items.
- Assessed denominator = Pass + Fail items. Exclude Unknown, N/A, Out of scope, and secondary failures already counted under another item.
- Score = earned / assessed; optional normalized score = 10 × earned / assessed, rounded to one decimal. If assessed is zero, report “Not scored.”
- Account for all 27 IDs in a full audit. Use **Shared → ID** for a secondary item whose only finding was already deducted elsewhere; exclude it from the denominator. If it has an independent defect, score that defect normally.
- Disclose Unknown, N/A, Shared, and Out of scope IDs and reasons. A short report may group passing IDs. Never present a focused score as full coverage.
- Show the number of Unknown items beside the score. For example, 9/10 with 8 unknowns communicates a much narrower review than 24/25 with no unknowns.

Illustrative arithmetic: 18 Pass + 3 Fail + 2 Unknown + 4 N/A = 27 items. Report **18/21 (8.6/10), 2 unknown, 4 N/A**. The score is checklist conformance, not a probability of success or a production-readiness grade. One critical failure can outweigh a high total.

Use this report shape, adapting detail to the request:

```text
Skill audit: <name>
Scope: <files/resources and runtime; relevant exclusions>
Score: <Pass>/<Pass + Fail> (<optional normalized>/10); <N> unknown
Verification: <source inspection, commands/fixtures run, untested boundaries>

Findings, ranked by impact
- <severity; ID; file:line or quote>: <defect and consequence>. Fix: <smallest change>.

Score accounting
- Pass: <IDs, grouped with short evidence descriptions>
- Fail: <IDs referring to findings>
- Unknown: <IDs; missing evidence and how to obtain it>
- N/A / Shared / Out of scope: <IDs; reason or primary finding>
```

Omit empty sections. Surface critical or task-blocking findings immediately beside the score as blockers regardless of the total. Severity reflects consequence: critical authorization or destructive-action defects first, task-blocking errors next, then material reliability and clarity issues. Do not rank by the number of checklist items a defect touches.

For authorized fixes, preserve a before/after account of affected findings and rerun the affected checks. Audit-only requests end with findings. Behavioral improvement claims require execution evidence beyond this structural score.

## Reference

[Maggie Appleton — Squish Meets Structure: Designing with Language Models](https://maggieappleton.com/squish-structure) (2023 talk; transcript and illustrated slides). Informs the checks for bounded operations, inspectable inputs and outputs, task-appropriate structure, and reduced user cognitive burden. The audit applications above are adaptations, not requirements prescribed by the article. Use it as design rationale, not evidence of current model capabilities or a mandatory read for every audit.
