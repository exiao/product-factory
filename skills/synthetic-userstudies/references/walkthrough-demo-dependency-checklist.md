# Dependency checks for agent-executed tutorials

Use when an artifact asks a learner's coding agent to execute demonstrations. Trace each relevant step from the learner's actual starting state. A mental trace identifies a risk; verify with tools before reporting an objective failure.

Check the dependencies that matter to the supplied artifact:

- **Workspace and permissions:** does the step use a reachable, authorized location? Prefer in-project examples when appropriate, but verify actual access rather than assuming every external path fails.
- **Tools and capabilities:** was the required browser, screenshot, connector, or execution capability established? Read the current tool inventory/documentation where available. If unavailable, state the unknown; do not substitute an invented "standard" tool list.
- **Files and inputs:** did the learner create or receive each file? Check order, optional branches, and supplied repositories. Verify existence before declaring a missing file.
- **Fallbacks:** can the proposed fallback run from the learner's current state, or does it depend on another unavailable file, tool, account, or download?
- **Authentication:** do the instructions match the provider's actual supported flow? Verify current instructions when the flow matters; do not assume API tokens and OAuth are interchangeable.
- **State and timing:** when does the particular tool reload configuration? Verify rather than imposing a universal restart rule.
- **Product-specific paths:** validate rules, skills, and command locations against the stated product and version. Avoid requiring unrelated product variants.
- **Handoffs:** does the end state of one section satisfy the next section's prerequisites, including state carried across delegated slices?

Per consequential risk, report the step/source, prerequisite, suspected failure, verification performed and result, and a fix sized to the intended audience. Missing tools or access mean "unverified," not "broken."

Calibrate to the real audience's competence and access needs. Preserve essential dependencies while improving recoverability. A synthetic novice reaction is a hypothesis, not real learner data; do not dismiss an accessibility or prerequisite barrier just because only one persona surfaced it. Validate the barrier and choose a response that supports the intended audience without unnecessary instruction.
