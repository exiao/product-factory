---
name: interaction-design
description: "Design product navigation, information grouping, action placement, and interaction behavior. Use for unresolved flows or confusing navigation and settings, translating accepted stories into wireflows or clickable prototypes; visual polish alone uses impeccable."
---

# Interaction Design

Bridge an accepted human story to a product experience that can be tried, evaluated, and designed at high fidelity. Own the interaction decisions and their handoff; use the existing design skills for rendering, visual direction, and implementation.

## Focused modes and routing

The exact mode names below are conversational requests, not shell commands or standalone skills. Use the narrow mode when the request explicitly names it or clearly asks for that operation. A broader request already authorized by the user may continue beyond the mode; otherwise keep the work local and do not require the software-factory workflow.

| Conversational mode | Target | Default output |
|---|---|---|
| `interaction-design inspect` | Effort in a named task path, including hidden decisions, waiting, and correction | Local effort annotation or before/after for the affected path, with evidence labels |
| `interaction-design critique` | Labels, hierarchy, action meaning, feedback, and next-state understanding | Review lenses and a local annotation or before/after for the affected surface |
| `interaction-design audit` | Error, interruption, cancel, back, undo, retry, and work preservation | Recovery-state annotations, with a local before/after proposal when useful |

For a bare `$interaction-design` invocation with no actionable surrounding request, use the available context only to offer 2–3 relevant mode suggestions with a short reason for each, then stop. When the surrounding conversation already supplies an actionable request, follow that request's scope instead of stopping for the menu. Do not start discovery or create a full wireflow or prototype for a local review; produce a scoped working artifact when explicitly requested. A review-only request is read-only. A natural request to fix a named interaction authorizes the smallest local fix and its relevant verification; it does not authorize a broader redesign. Read [focused modes](references/focused-modes.md) only after selecting one of these modes.

## Start from what is settled

Read the supplied storyboard, outcome criteria, and relevant current product surfaces. Inspect images when the storyboard or incumbent interface is visual. Reuse the person, situation, selected intervention, platform, constraints, and evidence labels. A believed-in outcome remains a hypothesis until observed; approval settles direction, not effectiveness.

Do not restart discovery or ask the user to repeat settled choices. If no storyboard exists, an accepted scenario can suffice; use [$storyboards](../storyboards/SKILL.md) when an illustrated story is requested or the human sequence itself is unclear. Ask only when a missing choice would materially change the experience. Continue with stated assumptions for routine details.

Match the deliverable to the request: assessment or planning can stop at a wireflow and brief; a request to prototype needs a working artifact. Reuse approved interaction work and resolve only the open portion. Do not impose new exploration or low fidelity on a settled design.

For an existing navigation, toolbar, or settings problem, start from that surface and the task it supports. A storyboard is not a prerequisite. Inspect actual destinations and action effects when access permits; a screenshot establishes appearance, not what a control does. Keep changes local unless the problem requires broader restructuring.

If the user rejects the usefulness of the idea, or the proposed intervention only names a desired result without explaining how it helps, return to the mechanism comparison in [$software-factory](../software-factory/SKILL.md) before designing dependent flows. Reuse the agreed problem and existing evidence; do not restart the entire discovery process. When output quality is the disputed issue, carry a worked result and its limitations into the interaction brief. A clickable simulation can test control and clarity, but cannot establish that the underlying assistance produces a useful result. Explicit UI-only requests and settled directions still proceed within their stated scope.

## Define the core loop and remove work

Before designing a prototype path, reuse or state its starting material, product contribution, useful result, and how the person accepts or revises it. Keep each alternative focused on that loop. A list of domain tasks is not a list of required features. For an existing product, apply this to the affected task without removing unrelated established capabilities.

For each proposed feature or step, ask what essential outcome, control, or recovery fails without it. Omit unsupported additions before arranging the interface; disclosure is for secondary capabilities that have earned their place. Keep the useful transformation intact, not just an input box and an empty result area. Record the loop and meaningful exclusions briefly in the existing brief; no separate artifact or approval is required.

## Translate the story into behavior

Identify the moment that creates the promised benefit and what must happen before and after it. Separate events in the person's life from product interactions: one storyboard panel is not necessarily one screen, and several states may live on one screen.

Use the user's vocabulary to identify the things they act on, their meaningful states, and who controls each change. Clarify what the system knows, what the person must supply, and what is saved or temporary. Inspect existing behavior before inventing capabilities. Distinguish a system response from an external outcome it cannot guarantee.

For consequential moments, capture a compact mapping; combine entries when they describe the same interaction:

| Story beat / outcome | User intent and information needed | Action or trigger | Visible response and next state | Open assumption |
|---|---|---|---|---|

Expose hidden work: decisions, memory, setup, waiting, coordination, and correction. A shorter click path can still demand more effort. Keep information needed for a decision near the action, and defer unrelated detail. Preserve familiar product patterns unless a specific task benefit justifies changing them.

## Organize information and navigation

Make deliberate decisions about what belongs together, where it lives, and how people find and leave it. Scale this work to the surface: a small panel may need only annotated grouping and placement decisions; a multi-area product may need a compact destination hierarchy.

- Group content by the user's tasks and concepts, rather than internal implementation or provider boundaries. Separate global, workspace, object, and temporary-view settings when their scope affects expectations. Use labels that predict the destination or effect; flag ambiguous labels such as “Clear” until the affected content is known.
- Distinguish navigation to a destination from actions on the current content, view dismissal, and save or commit. Make current location, available next steps, and the return path understandable. Specify whether Back, Close, and Done navigate, dismiss, or save, including what happens to unfinished work.
- Give headers and toolbars a clear hierarchy. Check each item's role and scope: title/location, navigation, primary action, contextual action, or secondary destination. Keep controls near the content they affect. Move unrelated or infrequent destinations into a relevant group when that improves findability; do not hide useful actions in overflow solely to achieve a cleaner screenshot.
- Review competing navigation systems, duplicated destinations, and excessive depth where they affect the task. Prioritize by task importance, frequency, and consequence, preserving familiar placement unless the benefit of a change justifies relearning. Use progressive disclosure for genuinely secondary detail, not to conceal the core task.
- Specify semantic priority before polishing appearance: what should be noticed first, what is secondary, and why. Pass that hierarchy to design-mode and Impeccable for spacing, alignment, typography, and emphasis. A functional click path does not by itself establish good organization.

Treat interface copy as part of the interaction. Before adding a label, eyebrow, subtitle, or helper sentence, identify the distinct question it answers at this moment that the existing content and controls do not answer. For example, “Upload a file to get started” adds little beside a clearly labeled upload control, while a required file format or size limit may prevent a failed attempt. Prefer clearer grouping, control wording, or feedback over explanatory prose that compensates for a confusing structure. Preserve instructions needed for unfamiliar actions, accessibility, consequences, and recovery; do not replace useful text with cryptic icons. Carry only necessary product copy into the wireflow and keep design rationale in its annotations or brief.

For example, a header containing “Settings,” “Done,” and “Manage access” deserves a role check. If Done dismisses the panel and Manage access opens a separate permissions area, a plausible structure is a title and dismissal control in the header with an Access row in the panel. Confirm the functions and platform conventions before applying that structure; it is not a universal rule that headers may contain only two items.

When terminology or hierarchy is the central uncertainty and a research plan or test is in scope, read [navigation testing](references/navigation-testing.md). Use this focused method without requiring a design sprint or rebuilding the interface.

## Simplify the current state before polishing

For every affected path, inspect the decisions and controls before changing spacing or wording, even when the screen is not crowded. Identify what the person needs to do now, what information makes that possible, and which controls belong to a later state. Remove unnecessary features and steps first; then group related work or defer justified secondary options within the requested scope. Prefer one clearly dominant next action where the task has a natural sequence; do not turn this into a universal one-button rule for editors, comparison tools, or expert workflows.

Challenge setup, preview, submit, and confirmation steps between input and benefit. Remove a step when it adds no meaningful choice; show the result in place when that serves the task. Retain explicit triggers when they control cost, external effects, consent, or whether input is ready. Keep editing optional for a result that can already be used, and preserve required review before consequential commitment.

When input methods are alternatives, consider showing one at a time with an obvious way to switch. Keep them together when people need to combine or compare inputs. Specify what switching preserves, what invalidates generated results, and which inputs are submitted; never silently send hidden inputs or discard edits merely to simplify the screen.

Decide whether an unavailable action helps people understand the next step. Reveal it after prerequisites when its early presence adds clutter; retain a disabled action with a clear reason when discoverability or a stable layout matters. Preserve accessible labels, essential instructions, consequences, and recovery. Fewer visible words or clicks alone is not evidence of lower effort.

For the affected states, verify that the next action is understandable without narration and that deferred options remain findable. Check empty, populated, switched-input, and recovery states where relevant. Record the structural decision briefly in the existing interaction brief rather than creating another mandatory artifact.

## Resolve the open interaction choice

When the way it works is materially open, sketch two or three genuinely different approaches to the decisive interaction. Change the organization of work, control, or sequence—not just color and layout decoration. For example, compare a guided sequence, direct editing, and reviewing an editable proposal when those fit the task. Keep actor, scenario, content, and intended outcome constant.

When several people or agents are exploring an open choice, collect independent sketches before discussion; an initially anonymous artifact review can reduce influence from the author's pitch. Preserve rationale and provenance for follow-up. Team votes select a direction to investigate, not evidence of customer preference. Use this only when alternatives are genuinely open.

Compare user effort, clarity of consequences, recoverability, fit with repeated use, and feasibility. Explain what each approach removes and what burden it adds. Recommend one and identify the uncertainty that could reverse the recommendation. Do not manufacture alternatives for a fixed brief. Reuse an existing selection; when the user has delegated the choice, state the choice and proceed. Request a decision only when a consequential preference remains unresolved.

## Make the interaction visible and testable

Show a wireflow: rough screen or region layouts connected from the actual triggering control to the resulting visible state. Include on-screen information and feedback, not only boxes naming pages. Show only changing regions when repeating the full screen obscures the sequence. A simple flow can live in the prototype with concise annotations; do not maintain duplicate diagrams just for completeness.

Use [$design-mode](../design-mode/SKILL.md) for structural prototypes and its low-fidelity rendering and verification guidance. Choose fidelity around the unresolved question; follow requested native formats. Retain the established design system and realistic content ranges. A static image can communicate a direction but cannot demonstrate interaction.

Build the smallest coherent path through the value moment, with the branch most likely to break it. Include loading, empty, invalid, permission, interruption, error, or recovery states only where they affect this task. Specify whether retry, back, cancel, undo, or returning later preserves work. Make asynchronous progress and completion distinguishable. For consequential actions, make effects and available recovery clear before commitment. Preserve keyboard and assistive access to the relevant controls and state feedback.

Label synthetic content and simulated integrations outside the apparent product UI where practical. Provide repeatable starting states and a reset for a demonstrable prototype. Keep shared state coherent across views; do not make every action jump to a predetermined success screen.

Exercise the actual artifact from its declared entry point through the decisive action and relevant recovery path. Inspect the rendered result and fix observed defects, then recheck affected behavior. Report unavailable checks. Never substitute a prompt, screenshot, or state specification for a requested working prototype.

For navigation or grouping changes, also check finding the target from the normal entry point and returning without losing expected context or edits. Inspect header priority and grouping at the relevant narrow width and with realistic labels. Distinguish observed navigation behavior from a findability hypothesis; when terminology or grouping remains disputed, a focused first-click or tree test with representative users can provide evidence without rebuilding the entire product.

## Hand off to high-fidelity design

Deliver one compact interaction brief alongside the artifact:

- Accepted scenario, outcome criteria, chosen interaction approach, and rationale.
- Linked wireflow or prototype with entry point, decisive action, and completion condition.
- Content grouping, navigation hierarchy and labels, action placement and priority, material states and transitions, persistence/recovery rules, and constraints the visual designer must preserve.
- Verified behavior, simulations, unresolved hypotheses, and the next useful validation.

Judge readiness by whether the artifact demonstrates the action-to-response chain without narration filling gaps. Explain which part of the human outcome remains outside the prototype. A successful agent walkthrough verifies behavior; it does not establish human usability or demand. Use real user observations when available; label simulated persona feedback as hypotheses.

Pass this brief to [$design-mode](../design-mode/SKILL.md) and [$impeccable](../impeccable/SKILL.md) for visual direction and high-fidelity execution. Carry forward settled interaction decisions instead of restarting their discovery. For visual comparisons, use the same decisive screen and a consequential follow-up state so beautiful isolated screens cannot conceal a broken flow. Use [$design-iteration](../design-iteration/SKILL.md) when incorporating critique, and [$acceptance-criteria](../acceptance-criteria/SKILL.md) when formalizing detailed behavioral checks. Continue into these steps when already requested; otherwise deliver the reviewable handoff.

For the research basis or deeper method selection, see [sources](references/sources.md). These sources inform the approach; their organization-specific procedures are not universal requirements.
