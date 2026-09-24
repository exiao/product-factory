# Focused web accessibility checks

Use this for the affected flow, not as a claim that the whole product conforms to WCAG. Confirm the applicable [WCAG 2.2 criteria](https://www.w3.org/TR/WCAG22/) against the current standard when making a conformance claim. The pattern examples in [Addy Osmani's accessibility skill](https://github.com/addyosmani/web-quality-skills/tree/main/skills/accessibility) are implementation references, not a substitute for the standard or a rendered check.

## Test the rendered interaction

1. Start from failed Lighthouse or axe nodes when available. Inspect the affected component and its accessible name, role, state, relationship, and visible label. Check landmarks and heading order in the surrounding page.
2. Use only the keyboard to enter, operate, dismiss, and leave the affected control. Verify visible focus, logical order, no trap, and focus return after a dialog or temporary surface closes. Check that a sticky header or footer does not fully obscure the focused control ([2.4.11](https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum)).
3. Measure rendered contrast for text and essential control boundaries; report the actual color pair and ratio. Check at 200% zoom or the relevant reflow size, and try a screen reader on a representative path when available.
4. Fix the source, then repeat the same automated and manual checks. Report the checks run, failures left, and untested input methods or assistive technology. An automated score of 100 does not establish conformance.

## Checks that are easy to miss

- **Target size:** [2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum) sets a 24 by 24 CSS pixel minimum at AA, subject to its stated exceptions. Prefer larger comfortable targets when the platform and layout allow; do not misreport a 40 pixel design heuristic as the WCAG threshold. Check spacing and overlap as well as box size.
- **Dragging:** [2.5.7](https://www.w3.org/TR/WCAG22/#dragging-movements) requires a single-pointer alternative to dragging unless dragging is essential or the behavior is determined by the user agent. A sortable list can offer Move up and Move down buttons. Verify the alternative completes the same task and is keyboard accessible.
- **Pointer cancellation:** Show press feedback on pointer down if useful, but commit a consequential action on release or provide an equivalent way to abort or undo it; check [2.5.2](https://www.w3.org/TR/WCAG22/#pointer-cancellation).
- **Forms:** Associate a visible label with each input. Connect instructions and errors to the field, expose invalid state, and focus or summarize the first actionable error after submission. Check autocomplete for known personal fields and do not require repeated entry of information already supplied in the same process ([3.3.7](https://www.w3.org/TR/WCAG22/#redundant-entry)).
- **Dialogs and tabs:** Prefer native controls where they satisfy the task. For a custom dialog, test focus entry, containment, Escape, and return. For custom tabs, test selected state, panel relationship, and arrow-key behavior against the [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/patterns/).
- **Status:** Make loading, success, error, and changed results perceivable without relying on color or sound alone. Use an appropriate live region for updates that do not move focus, and verify that assistive technology announces the message once at the right time.
