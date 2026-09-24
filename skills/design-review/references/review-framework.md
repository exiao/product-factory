# Review framework

## Questions and assumption check

For a full design review, address every question below. Reuse the brief, prior user answers, research, and observed product behavior. Do not silently fill gaps with plausible stories. For a focused review, identify the questions covered and explicitly mark the rest outside scope; do not imply a complete review.

Record a compact matrix: `Question | Status | Answer and source | Gap or inconsistency and decision affected`. Use ANSWERED for an explicit answer with its source, ASSUMED for an inference, UNKNOWN for a missing answer, CONFLICTING for incompatible answers or evidence, and N/A with a reason. Distinguish a user decision from empirical evidence: an explicit intended audience can be ANSWERED while demand from that audience remains UNKNOWN. A screenshot cannot establish motivation, affection, or retention.

### Customer context

1. What is the objective of the initiative, and why does it matter?
2. Who is this for?
3. When and why do they use it?
4. What is on their mind at that moment?
5. What job are they trying to get done?
6. How did they get here?
7. How does this fit into their life or existing workflow?
8. How important is this screen, and what are the scope, timeline, and team capacity? Match scrutiny to consequences, frequency, and recovery difficulty; settings are not automatically low stakes.
9. What problem lies behind their proposed solution? Understand it without disregarding explicit user direction.

### Solution quality

10. What should users feel and achieve?
11. Why would they love it, and what evidence supports that belief?
12. What do they do now, on this screen?
13. Where do they go next?

### Alternatives

14. What would they do without this product, including workarounds or doing nothing?
15. What supports confidence that this is better than existing alternatives?
16. What can be removed while preserving the useful outcome?
17. Without the current constraints, would we still design it this way? Separate real constraints from assumed ones; this thought experiment does not authorize ignoring the brief.

### Focus and learning

The supplied list skips 18; retain its numbering for traceability.

19. Are we helping users experience the core value before adding more? Is there evidence they reach that value or request more after experiencing it?
20. Which choices come from intuition, and what observations or data would validate or change them?
21. Where can we do less, and what are we deliberately saying no to?
22. Does this primarily serve growth, value, or retention, and how would we know it succeeds?

## Highlight and clarify

Lead the user-facing review with material UNKNOWN, ASSUMED, and CONFLICTING items, including any inconsistency between the stated objective, audience, journey, proposed solution, and success measure. Explain the sources in tension and which design decision depends on resolving them. If none are material, say so; do not invent uncertainty.

When a missing answer or inconsistency would change the recommendation or revision, use the available Ask user question tool. Prefer `functions.request_user_input_async` when available; use `functions.request_user_input` only in a mode where it is permitted. Ask concise, targeted questions, batching related gaps and offering concrete choices when helpful. Do not send the whole checklist as a questionnaire or ask again for settled answers. If no question tool is available, state that limitation and ask directly. Continue independent review while answers are pending; do not treat silence as an answer or mark dependent conclusions settled. User clarification resolves intent, not missing empirical proof; retain evidence gaps with a proposed observation or test.

Use the [usability checklist](usability.md) for the heuristic coverage in this same review. Do not create a second scorecard from the question matrix.
