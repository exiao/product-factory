# Optional uncertainty mapping

Use when unfamiliar code, ambiguous requirements, a reference port, or a risky assumption could materially change the design. A narrow, understood change does not need a map. For an explicitly requested interview, use grilling; this mode is primarily evidence gathering and concise synthesis, not a mandatory questionnaire.

Keep the map inside the existing design note. Organize only the useful entries around four lenses:

- **Established facts:** what the brief, code, tests, or observed behavior actually establishes, with sources.
- **Open questions:** decisions or facts that matter but are unresolved, including their consequence and what would resolve them.
- **Tacit assumptions:** conventions, expectations, consumers, environments, or taste that have not been made explicit. Label assumptions until checked.
- **Discovered risks:** edge cases, hidden dependencies, prior failed approaches, and contradictions found during investigation. Do not claim to enumerate everything that remains unknown.

These are lenses, not sequential stages. Do not manufacture an entry in every quadrant. Disclose a material finding when discovered rather than waiting for its category's turn.

## Investigate and resolve

Inspect the relevant implementation and analogous behavior first. Use history or prior attempts when they could explain a constraint. State the inspected scope and important gaps; avoid a broad repository sweep merely to fill the map.

When preferences are unclear, provide the smallest concrete example that helps: a sample response, decisions table, sketch, or focused prototype. Use real supplied content where available and label simulated data. Do not require four visual directions, ten alternatives, a clickable artifact, or a user response for every task.

Prioritize uncertainties by their potential to change scope, interfaces, data integrity, or expensive commitments. For each material open item, record the evidence or assumption, its impact, the proposed resolution or experiment, and whether it blocks the next step. Distinguish an observed fact, a user decision, and an agent's working assumption.

Resolve routine facts and reversible implementation choices autonomously within the user's authorization. Ask only for a material preference, business rule, or authorization that cannot be inferred. Continue unaffected work while that answer is pending; time passing does not resolve a required decision. Use a small feasibility experiment when investigation cannot establish a critical technical assumption, within the task's scope.

## Carry it into the design

Turn resolved items into concise decisions with reasons and relevant evidence. Leave unresolved items visibly open with the next check or needed input. A useful map does not require eliminating every implementation choice or obtaining sign-off on every fact.

Proceed into already-requested design or implementation once its material blockers are resolved. An uncertainty-only request ends with the map; it does not authorize building. No stage approvals, merge quiz, or separate task are required by this mode.

When new evidence changes the design, record the old assumption, what was learned, and the resulting decision in the same note. Reopen only affected choices. Before handoff, summarize the consequential behavior and remaining risks for the reader rather than testing whether the user memorized the design.
