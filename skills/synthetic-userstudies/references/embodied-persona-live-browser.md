# Embodied-persona walkthrough of a live artifact

For visual study delivery, use [persona screenshot annotations](screenshot-annotations.md): preserve the action/evidence record below, and anchor synthetic reactions to the actual captured states.

Use when the user asks to act as a persona through a reachable interactive artifact. Run one consistent persona end-to-end when requested; preserve the task and initial context. The agent's actions are real interface interactions, while its personal reactions are simulated.

## Operate the current surface

Read the current browser tool documentation and follow its entrypoint and surface-selection rules. Use only methods actually exposed for that surface; do not copy methods from a past session. With `mcp__cua_repl`, follow its documented `cua` API. Browser surfaces may differ in accessibility, screenshot, and page-text support.

1. Select the user-scoped tab or open the authorized URL. Read current state and the preceding task context before deciding what to activate.
2. Resolve the target using current accessibility information or a current screenshot, as the surface supports. Disambiguate repeated labels by their surrounding context. Do not reuse stale element references after state changes.
3. Perform the authorized action and capture fresh state. Record what visibly changed, including empty responses, delay, errors, or unchanged state. Do not describe an unperformed tap as an observation.
4. Separately record the persona's synthetic expectation and reaction. Include an escape, retry, or recovery path if relevant to the task.
5. End with concrete observed behavior, hypothesized friction, a plausible alternative explanation, and a proportionate next check. Honor the user's requested transcript format; label requested scores as subjective role-play ratings.

## Long pages and incomplete state

A truncated accessibility snapshot is not evidence that content is absent. Use documented scrolling, fresh screenshots, or supported bounded rendered-text access to inspect the relevant section. Do not assume a DOM/evaluation capability is available. If the surface cannot be inspected sufficiently, state which portion remains unobserved and continue a clearly labeled offline pass where useful.

## Scope and delivery

Keep actions within the user's authorization; do not sign in, submit personal data, spend, or send messages as an implicit part of role-play. If comparison with another concept is requested, inspect that concept separately without inventing its behavior.

Report source location or reproducible state, action, observed response, and simulated interpretation. A screenshot or tool result supports a claim about the interface. A synthetic quote illustrates an interpretation; it is not testimony from a customer or evidence of retention, trust, or conversion.
