---
name: design-review
description: Review a UX flow or finished interface in one evidence-backed pass covering usability, journey and reference fidelity, UI rules, and accessibility. Use for design QA, UX reviews, and the completion check after creating or revising an interface.
---

# Design review

Review the named flow once. Use its observed states, captures, and source code for three checks: **usability and content**, **journey and reference fidelity**, and **UI rules and accessibility**. Combine the findings in one report. For a single screen or component, check its available states and interactions; mark anything else untested or outside scope.

## Scope and evidence

Identify the audience, entry point, task, stopping point, accepted design direction, and relevant states. Reuse current, comparable captures from the caller when they match the saved version; otherwise inspect the running product and capture visually stable states. For a journey, save ordered screenshots and verify each saved image. Supplied screenshots support visible findings only; mark interaction, device, and date details unknown unless provided. Label observed findings separately from inferences and hypotheses. Record blocked states instead of claiming a complete pass.

If a selected screenshot, mockup, Figma frame, or live reference exists, compare it with the implementation under matched viewport, content, theme, and state. Keep fidelity and usability verdicts separate: matching an inaccessible source does not make the result usable.

## Three lenses on the same evidence

1. **Usability and content.** Read the [usability checklist](references/usability.md) and cover all ten Nielsen Norman heuristics for the affected flow. For headings, instructions, caveats, containers, and actions, ask what would become harder if each disappeared. Flag elements with no distinct contribution; remove them when fixes are authorized. Preserve useful labels, feedback, consent, recovery guidance, product truth, and the accepted visual direction. Keep design rationale and prototype commentary outside apparent product UI. Check repeated motion in context, not only as an isolated animation.
2. **Journey and fidelity.** Inspect entry and exit, sequence, primary action, feedback, validation, empty/error states, persistence, back/close behavior, and the next step. Tie each finding to a numbered state or screenshot. When a reference exists, use [design QA](references/design-qa.md) to compare typography, layout, color, assets, and content. Report mismatches separately from approved deviations and problems in the source design.
3. **Rules and accessibility.** When code is available, inspect affected components, styles, tokens, and interaction states. Read [rule selection](references/rule-selection.md) and applicable [rule definitions](references/selected-rules.md); load [examples](references/selected-examples.md) only when needed. Check the rendered keyboard and focus path, accessible names, contrast, and relevant responsive or touch behavior. For a web accessibility audit or fix, use an available axe or Lighthouse run plus manual keyboard checks, then read [focused accessibility checks](references/accessibility-checks.md). Load [gesture](references/gesture-motion.md), [mobile web](references/mobile-web.md), or [animation performance](references/animation-performance.md) checks only for affected behavior. A screenshot or automated score alone does not establish accessibility or WCAG conformance.

For visual critique involving proof claims, generated media, or expressive motion, read [content and motion checks](references/content-and-motion.md).

For a formal product review, use the [question and assumption framework](references/review-framework.md). Address each question in a full review, or name the coverage of a focused review. Check mode errors where toggles, filters, edit/preview states, or accumulated context change an action's meaning. Ask only for a decision-changing clarification; continue independent work while it is pending.

## One result and confirmation

Combine all three checks into one prioritized findings list. Keep every actionable finding. For material findings, include the state or file/line, evidence, user impact, and smallest useful correction; add a rule ID or heuristic where applicable. A formal report includes the heuristic statuses, material assumptions, evidence paths, untested states, fidelity verdict when relevant, and accessibility limits. Use [before/after guidance](references/before-after-choice.md) only if a comparison would help; a mockup does not prove a fix.

An assessment-only request ends with findings and leaves the artifact unchanged. When creation, revision, or fixes are authorized, make the in-scope corrections in one batch and recheck affected states in the saved render. Use [render verification](references/render-verification.md) for web and SVG mechanics. Exercise changed interactions, keyboard focus, and relevant responsive states; recompare the source where fidelity changed. Reuse the caller's evidence and review budget. Report remaining defects or blocked checks rather than presenting them as passed. Publishing, unrelated redesign, and external writes require their own scope.
