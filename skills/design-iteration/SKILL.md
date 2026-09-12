---
name: design-iteration
description: "Revise existing designs from critique or user feedback, preserving the design system and tracing keep/change/kill decisions to evidence. Use for design iteration, incorporating reviews, or an explicitly requested test-revise-retest loop."
---

# Design Iteration

The loop step between **testing** a design and **re-testing** it. Something else generated the feedback (a design critique, an independent review, a [$synthetic-userstudies](../synthetic-userstudies/SKILL.md) run, a [$ui-lint](../ui-lint/SKILL.md) report, or the user's own notes). Your job is to turn that feedback into a **revised version** without losing the plot: every change is traceable to the critique that drove it, so the next test can measure improvement instead of just noticing the design changed.

## Choose the scope

When critique exists, start with what can be removed from the affected core loop, then triage, revise, verify, and deliver a compact change log. Try removal, simplification, and repair before adding capabilities; retain the product contribution, necessary control, accessibility, and recovery. Do not remove explicit requirements or unrelated established behavior. Reuse the user's audience, constraints, and accepted direction. Preserve whether the requested artifact is a prototype or a working product; interface iteration does not itself expand implementation scope.

When feedback disputes the underlying need, audience, or promised outcome, read and use [$people-problems](../people-problems/SKILL.md) to clarify only the disputed framing: the person’s task, breakdown, evidence, and what solved would mean. Reuse agreed statements; a clear layout or copy correction does not need renewed discovery.

First identify what the feedback rejects: the value of the concept, its interaction behavior, or its presentation. If the idea does not solve the problem, pause dependent cosmetic revisions and return to the mechanism comparison in [$software-factory](../software-factory/SKILL.md), reusing settled research and problem framing. Compare a materially different intervention and, where output quality matters, a concrete result sample. Record why the old mechanism failed and what the new test must establish. A user rejecting the concept is not asking for another layout of that concept; preserve existing files while reconsidering it. Resume interface iteration when a direction is selected or delegated. This route can end in a revised concept and test rather than a modified screen. Resolve disputed problem framing or demonstrated mechanism failure before using desirability reactions to judge the revised direction.

When an unresolved question about perceived qualities, personal relevance, or willingness to adopt would change the revision, read and use [$desirability-study](../desirability-study/SKILL.md) as the feedback or retest method. Keep appearance, relevance, and conditional adoption separate; a visual improvement cannot close an unresolved value objection. Preserve its word-association visual and comparable vocabulary and exposure conditions for retests. Use supplied responses or prepare collection; simulate only when requested or established in context, with fresh isolated participant sessions. Apply an explicit user preference directly when the requested change is clear; a study is not an extra approval gate.

When critique is missing, inspect the artifact and obtain a focused review with an available design skill such as [$impeccable](../impeccable/SKILL.md) or [$ui-lint](../ui-lint/SKILL.md). Do not automatically expand a small revision into a council, persona study, or deployment.

For an explicitly requested full test-revise-retest loop:

1. Inspect the artifact and its existing design system before review; preserve an unchanged baseline.
2. Gather relevant critique. Independent review tasks can use available subagents when delegation is authorized; otherwise run the scoped reviews sequentially. Seek independent perspectives for a disputed decision when useful; a council is not mandatory for every mockup.
3. Triage combined feedback, revise the real source, and log the decisions.
4. Use [$synthetic-userstudies](../synthetic-userstudies/SKILL.md) when a simulated persona panel is requested or appropriate to the agreed loop. Label simulated reactions as hypotheses and distinguish them from real user observations. Repeated persona complaints help prioritize questions but do not prove frequency or demand; a single reproducible blocker can justify a fix.
5. Re-test the changed interactions and assess regressions against the baseline. Use an independent reviewer when useful for subjective judgments, and stop when the requested issues are resolved or remaining questions require new evidence. Do not create an indefinite optimization loop.
6. Check relevant usability and accessibility details with measured evidence and applicable project requirements. Do not label an arbitrary target size as a universal standard.
7. Deliver the revised artifact and findings. Deploy only when the user has requested or authorized deployment; then verify the actual live surface.

Use the actual tools exposed in the session and their schemas. Do not assume Hermes toolset names or a particular browser API. A reviewer who could not access the artifact must report that gap. Verify claims such as broken buttons, failed requests, and missing screens in the real product before reporting them as reproduced bugs. Preserve alternative variants unless their modification or removal is in scope; KILL retires the named feature, step, or concept within scope; it is not permission to delete unrelated files.

## Why traceability is the whole game

Design iteration fails in a specific way: someone reads a pile of critique, rewrites the mockups "better," and now nobody can say which fix answered which problem. Re-testing then can't attribute a win or a regression to anything. The fix is boring and reliable: **triage every piece of feedback, decide what you're doing about it, and record the mapping.** The record explains why changes were made. When several changes are tested together, report the result for the revision as a whole; isolating a cause requires an appropriate comparison.

## Inputs you accept (any subset)

- A design artifact: live URL (Surge/localhost), an HTML/JSX/component file, a Figma-style spec, or a set of image mockups.
- One or more feedback sources. They arrive in different shapes:
  - **design-review** → 13-question answers + Nielsen heuristic findings + before/after fixes.
  - **marketing-psychology / persuasion review** → framing / urgency / anchoring / risk-reversal critique of copy and offers.
  - **another-perspective** → a council synthesis (Skeptic, User Advocate, Pragmatist, etc.) about the *decision*, not the pixels.
  - **synthetic-userstudies** → per-persona reactions and separately observed task behavior.
  - **desirability-study** → word associations, personal relevance, and conditional adoption findings.
  - **people-problems** → disputed problem framing, supporting evidence, and the desired outcome.
  - **UI lint pass** → file:line findings tied to named rules (motion, typography, spacing).
  - **raw user notes** → freeform, often terse.

If the artifact is a live URL or on-disk file, open and read it first. You cannot iterate on a design you haven't actually looked at.

## The loop

### 1. Read the artifact and the feedback

Load the current design and every feedback source. If multiple sources disagree (a council says "too much friction," a user study says "not enough guidance"), name the tension explicitly rather than silently picking a side.

### 2. Triage into keep / change / kill

Go through every distinct feedback item and label it. Not all critique deserves a change: some is noise, some contradicts higher-priority signal, some is a taste difference you'll consciously reject.

- **KEEP** — the design already handles this; no change, note why so it doesn't get re-raised.
- **CHANGE** — a necessary part of the core loop needs simplification or repair. Add a capability only when removal or revision cannot resolve the named failure.
- **KILL** — remove a feature, step, explanation, or variant that does not justify its burden on the core loop. It can work correctly and still be unnecessary; a serious concept flaw is not required.

Prioritize reproduced blockers and failures of the core outcome before polish; claim prevalence only when supported. Judge evidence against the claim: observed task behavior for usability, measured checks for accessibility, and participant explanations for perceived qualities or relevance. A stated preference does not override a reproduced failure. Keep user decisions distinct from research evidence, and record unresolved conflicts.

### 3. Reach for a design system (if one exists)

For an existing-product enhancement, inspect the current product’s navigation, shared shell, and comparable flow as well as its visual tokens. Match action placement and behavior to that context; report any access gap.

Before inventing spacing, colors, type, or components, look for the project's existing design language so your revision looks native instead of bolted-on. Search in this order, stop at the first hit:

1. A design-system skill for this project (if one exists), or a visual-identity doc (your visual-identity doc if you have one, or `VISUAL-IDENTITY.md`, `DESIGN.md`, `STYLEGUIDE.md` at repo root).
2. Design tokens in the repo: use `rg --files` to locate theme, token, and Tailwind files, then search relevant CSS/TS/JS/JSON with `rg`.
3. The artifact's own existing styles: reuse the classes/variables already on the page.

If you find one, conform to it and say which one you used. If you find nothing, that's fine: iterate on the artifact's own internal consistency and note that no system was available. **A missing design system is never a reason to stop.**

### 4. Apply the revision

Produce the new version in the **same medium as the input** unless the user requests a conversion (edit the HTML/component, edit image mockups using available image-editing tools, or update the spec). Preserve supplied brand assets and requested native formats. Change only what the triage justifies. Resist the urge to redesign untouched areas: scope creep destroys the ability to attribute the next test's result.

When feedback concerns too many screens, inputs, or explanations, revise the work the person must do, not just its layout. Identify the interaction rule behind the correction and inspect sibling states in the affected loop for the same problem. For example, a redundant preview step warrants checking other preview steps in that loop; it does not authorize removing meaningful review or confirmation elsewhere. Tie these changes to the same feedback item so the user need not report each instance. Use [$interaction-design](../interaction-design/SKILL.md) for an unresolved flow. Keep prototype limitations in the handoff or study brief; include them in the product UI when they help the person make a meaningful decision.

### 5. Emit the change log

Alongside the revised artifact, output a compact table mapping each decision back to its source. This is what makes the next test meaningful:

```
## Iteration <N> change log

Design system: <name of system used, or "none found — iterated on internal consistency">

| Feedback (source) | Verdict | What changed |
|---|---|---|
| Persona 2 predicts leaving because the next action is unclear (synthetic hypothesis) | CHANGE | Replaced slide 1 with a tappable ticker that returns a live verdict |
| Promo reads as a nag (marketing-psychology review) | CHANGE | Moved promo to post-value reward framing |
| Weekly plan splits attention (another-perspective, Skeptic) | KILL | Dropped the weekly-plan variant entirely |
| CTA contrast is fine | KEEP | Already meets contrast; no change |

Unresolved tensions: <any conflicting feedback you had to arbitrate, and how>
Open for next test: <what the next round should specifically measure>
```

### 6. Hand back for re-testing

Verify the changed artifact: render or open it, exercise affected interactions when possible, and check for regressions. For subjective improvement claims, use the agreed next review or an independent reviewer when useful. Give reviewers the task, audience, and artifact without coaching them toward the desired verdict. Report what was actually tested and what remains unverified.

## Where this sits in a design pipeline

A typical loop, with this skill as the recurring node:

```
design-mode + design-system  →  ui-lint + independent critique
      →  DESIGN-ITERATION  →  synthetic-userstudies  →  DESIGN-ITERATION  →  UI-polish pass
```

Keep the reviewed baseline stable during feedback collection, then record the revised version used for retesting.

## What this skill is NOT

- **Not a standalone review method.** It consumes feedback and invokes an appropriate review skill when feedback is missing.
- **Not from-scratch design.** For exploring new layout paradigms use a UI-prototype-exploration workflow; for building a fresh interface use the [$impeccable](../impeccable/SKILL.md) skill or your usual UI-building workflow.
- **Not final polish.** The last-mile motion/typography/spacing sweep belongs to a dedicated UI lint/polish pass. This skill makes the substantive revisions between tests; that pass makes the shipped version feel finished.

## Gotchas

- **Silent scope creep is the main failure.** "Improve the mockups" tempts you to touch untouched areas. Every edit not traceable to a triaged feedback item destroys the next test's ability to attribute a win or regression, which is the entire point of this node. If you can't name the critique a change answers, don't make the change.
- **Conflicting sources need arbitration, not averaging.** When a council says "too much friction" and a user study says "not enough guidance," don't split the difference into mush. Name the tension, weigh evidence relevant to the disputed claim, and record that you made the call in the change log's "Unresolved tensions" line.
- **Separate verification from preference.** Run technical checks on your changes. Treat your own taste judgment and simulated reactions as hypotheses; seek independent evidence when claiming improved user outcomes.
- **A missing design system is never a reason to stall.** If the search in step 3 finds nothing, iterate on the artifact's own internal consistency and note it. Don't invent a system or block on one.

Every substantive revision should answer a named feedback item or observed defect. A change log supports review; it does not by itself prove improved user outcomes.
