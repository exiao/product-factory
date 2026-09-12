---
name: design-review
description: Run a structured product design review with 13 product questions, Nielsen Norman heuristics, mode-error analysis, evidence-backed findings, and prioritized recommendations. Use for a formal design review or UX scorecard; use ui-lint or impeccable for a screenshot-first flow audit.
---

# Design review

Review the named feature, local app, or URL as a first-time user. Capture enough of the real surface to support claims, record the user journey, and use the applicable questions from the 13-question framework in [review-framework.md](references/review-framework.md). Make assumptions explicit when context is missing; do not ask the user to answer the review questions.

Evaluate all ten Nielsen Norman heuristics with a factual observation and a status such as PASS, FAIL, WATCH, or UNTESTED. Walk persistent toggles, filters, edit/preview states, multi-input screens, and accumulated context as mode errors: can the user forget the mode, is the indicator at the locus of attention, and does the same action change meaning? Tie each mode finding to a named [$ui-lint](../ui-lint/SKILL.md) rule when applicable.

Rank findings after collecting them. Give up to three highest-impact findings a concrete fix, evidence, violated heuristic or design question, and expected user impact; retain the rest as concise findings. A mature third-party surface that cannot be faithfully rebuilt should use dogfood evidence and prose annotations instead of invented before/after mockups. A local or owned surface may use an in-context before/after only when the real chrome, styles, content, and behavior are available.

Return a review artifact or report in the requested location. Include method, evidence paths, assumptions, untested surfaces, scorecard, findings, and limitations. Publishing a shareable report or changing product code requires explicit scope; this review does not authorize either. Read [before-after-choice.md](references/before-after-choice.md) for choosing evidence format.
