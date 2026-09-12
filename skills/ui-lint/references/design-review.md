# Structured design review

Review the named feature, local app, or URL as a first-time user. Capture enough of the real surface to support claims, record the user journey, and answer applicable questions from [review-framework.md](review-framework.md). State assumptions when context is missing; do not ask the user to answer the framework questions. If only supplied screenshots are available, limit findings to visible evidence and mark interactions untested.

For a formal review or full scorecard, evaluate all ten Nielsen Norman heuristics with a factual observation and PASS, FAIL, WATCH, or UNTESTED. A focused question needs only the applicable heuristics. Walk persistent toggles, filters, edit/preview states, multi-input screens, and accumulated context for mode errors: can the user forget the mode, is its indicator at the locus of attention, and does the same action change meaning? Tie findings to matching `modes-*` definitions in [selected-rules.md](selected-rules.md) when applicable.

Rank findings after collecting evidence. Give up to three highest-impact findings a concrete fix, supporting evidence, violated heuristic or design question, and expected user impact; retain the rest as concise findings. Separate observed problems from hypotheses. Use [before-after-choice.md](before-after-choice.md) when choosing evidence or proposing comparisons; a mockup does not prove a fix.

Return the review in the requested format and location; use the conversation when no separate artifact is requested. Include method, evidence paths or screen references, assumptions, untested surfaces, findings, limitations, and a scorecard when requested or performing a formal review. Review alone does not authorize implementation or publishing.
