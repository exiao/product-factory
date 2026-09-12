---
name: journey-mapping
description: "Create evidence-labeled journey maps and service blueprints for a specific actor and scenario, or broader experience maps for a defined domain, with prioritized opportunities and optional storyboards."
---

# journey-mapping

A journey map is a shared picture of how a person experiences a process over time, from their point of view, not the org's. Its visual structure should make the journey understandable at a glance. Its job is to (1) create a shared, evidence-labeled understanding a team can inspect, and (2) surface the specific moments where the experience breaks so you know where to invest. For decision work, a map that ends without prioritized opportunities is decoration; a simple map request can stay focused on the artifact.

## Before you map: scope it

A journey map is only meaningful with a fixed viewpoint. Nail these first, or the map will be a vague average of nobody:

- **Persona / actor.** ONE specific person type, with goals and context. "Users" is not a persona. If you have research personas, use one; if not, name a concrete archetype and its motivation.
- **Scenario + goal.** The specific journey and what the person is trying to accomplish ("first-time user setting up the product and reaching first value"). One scenario per journey map or service blueprint. An experience map may cover broader activities within a clearly defined domain. Onboarding and renewal are different journeys.
- **Scope boundaries.** Where does the journey start and end? Widen too far and it's shallow; narrow too far and you miss the handoffs where experiences usually break.
- **Grounding.** Is this current-state (what happens today, from evidence) or future-state (the experience you intend to design)? Say which. Ground current-state claims in interviews, support tickets, session recordings, analytics, or a dogfood pass. If evidence is missing, label the result an assumption map of the current state; unknowns can remain blank. Keep material claims traceable to source IDs and confidence. Use a compact legend, stage-level markers, and a linked evidence ledger rather than repeating caveats in every cell. Distinguish mixed evidence within a stage when necessary. Example evidence types: `[REPORTED: interview-03]`, `[ANALYTICS: funnel-2026-09]`, `[DOGFOOD: build-42]`, or `[ASSUMED]`. Dogfood can establish what the product does and where a task fails; it cannot establish customer prevalence, sentiment, or motivation. Label inferred emotions and simulated quotes explicitly.

Use the right map for the question: a **journey map** follows one actor through one scenario and goal; an **experience map** describes broader activities, needs, and contexts across a domain; a **service blueprint** adds the operational layers that enable a journey. Name the map type and do not use a broad experience map to imply evidence about one product flow.

When gathering a map with a participant, reconstruct one recent episode in their order before imposing proposed stages. Ask them to walk through the sequence, identify anything missing between steps, and clarify handoffs or work outside the product. Keep researcher-proposed additions separate from their account. A recalled episode is reported evidence; only witnessed actions are observed. For group synthesis, preserve individual sequences before combining them so distinct journeys do not become an invented average.

## The anatomy (content, not a compulsory table)

Start with a visible sequence of stages, actions, and transitions. Choose a compact timeline, connected stages, swimlanes, or a matrix according to the question. The following are information dimensions to consider, not mandatory rows to fill:

1. **Stage / phase** — the chunk of the journey (e.g. Discover → Onboard → First use → Habit → Renew). Name them in the user's language, not the funnel's.
2. **Actions** — what the person actually does in this stage, concrete steps.
3. **Thoughts / questions** — what's going through their head; the questions they need answered to continue. Verbatim quotes if you have them.
4. **Emotions** — include supported feelings or explicitly labeled hypotheses when they explain a consequential moment. Omit an unsupported emotion layer; note the evidence gap once. Use emotion as context, not as the priority score.
5. **Touchpoints / channels** — where the interaction happens (app screen, email, support, physical, third party).
6. **Pain points** — friction, confusion, drop-off, unmet need, moments of doubt. Be specific and locate each at a stage.
7. **Opportunities** — for each pain point, what could fix or improve it. This feeds prioritization; attach the relevant evidence IDs.

Show relevant waiting, retry, timeout/error, abandonment, and recovery as connected branches or clearly identified stages. An incidental local test failure belongs in a verification note unless failure/recovery is the scenario being mapped. If a test stops early, mark the observation boundary; distinguish the remaining source-defined or assumed path instead of presenting it as completed observation. For a **service blueprint**, show customer actions, the line of interaction, frontstage staff/system actions, the line of visibility, backstage actions, the line of internal interaction, and support processes. Frontstage belongs above the visibility line; backstage belongs below. Connect actions and dependencies with arrows, include physical/digital evidence at relevant touchpoints, and identify material handoff owners and entry/exit conditions when known. Mark unknown ownership rather than inventing it. Use a blueprint when the fix likely lives in operations or systems the user never sees.

## Use emotion as context, not the ranking

Draw an emotion curve only when comparable evidence or an explicitly requested hypothetical trajectory makes it meaningful. Missing evidence is not a neutral score: never draw a flat line to mean “unknown,” connect across unsupported stages, or invent highs and lows to populate a chart. A measured flat trajectory is valid. Do not treat the deepest trough as a priority by itself. Assess task failure or blocked progress, consequence/severity, reach, and recovery difficulty alongside evidence confidence. Low confidence may raise the priority of investigation; it should not automatically demote a potentially severe problem. Keep effort as a separate estimate so a high-effort fix is not mistaken for a high-impact problem.

Pay special attention to:
- **Task failure and recovery** — what happens when the person is blocked, waits, retries, abandons, or returns later. Record whether recovery is self-serve, assisted, or unavailable.
- **Transitions and handoffs** between stages, channels, or teams. Check where information, responsibility, or context can be lost.
- **Moments of truth** — the few interactions that disproportionately shape the overall impression.

## Storyboarding the key moment

When a storyboard would clarify a critical moment, show it as a short sequence. A storyboard is a small sequence of frames (sketches or described panels) showing a specific user moving through a specific moment, step by step, in context. It turns an abstract stage into a concrete scene a team can react to and a designer can build against.

For each key moment, produce a short panel sequence:

```
Panel 1: <who, where, what they want> — the setup and trigger
Panel 2: <the action they take>
Panel 3: <what the system/product does in response>
Panel 4: <the outcome and how they feel> — resolution or friction
```

Keep it to 3-6 panels per moment. Show the pain-point version and, if proposing a fix, the improved version beside it so the delta is visible. Storyboards are useful for consequential moments and uncertain transitions — don't storyboard the whole journey, storyboard the moments that decide it.

## Deliverable

Prefer a visual artifact over a wall of text. Options, in order of preference:
- An SVG or HTML map with a clear reading direction, concise stage labels, concrete actions, and visible transitions or branches. Add a few anchored friction/opportunity callouts. Use legible real text; include an emotion layer only when it adds supported meaning.
- If a diagramming tool is available (Excalidraw, a design tool, d3), use it.
- A matrix when comparing the same meaningful dimensions across stages is the task, or a structured table for text-only delivery. HTML does not turn a dense spreadsheet into a useful visual map.

Keep the primary map readable without opening the evidence ledger. Prefer short action phrases and specific obstacles over paragraphs of methodological qualifications. Put scope and grounding in one compact note; put detailed confidence, sources, alternatives, and limitations in progressive detail. Omit empty or repetitive lanes rather than filling them with “Unknown.” A reader should be able to point to where the person starts, what they do, where progress changes or breaks, and what happens next.

Render the artifact at its intended reading size. Check that stage order and branches are apparent, labels are legible, and the key obstacle is visible without navigating a wall of text. On narrow screens, provide a coherent vertical sequence or an intentional scrollable map with orientation; do not shrink a wide matrix until it is unreadable. These are quality checks, not a required aesthetic or fixed panel count.

When the map informs a decision, end with a short **prioritized opportunities** list. Rank action opportunities by task failure/blocked progress, severity, reach, and recovery difficulty. Record evidence confidence separately; when a potentially severe issue is weakly evidenced, prioritize its investigation rather than automatically demoting it. Keep estimated effort separate. Keep the visible list focused on stage, problem, proposed direction, and why it matters. Preserve suspected cause, source IDs/confidence, next validation, plausible alternatives, and what would change the recommendation in linked or expandable detail when material; do not force every field into every visible item. Use provisional qualitative priorities when measurements are missing. For a simple map request, keep this to a compact note rather than creating a separate research plan.

## How to run this skill

1. **Scope** (persona, scenario+goal, boundaries, current vs future, grounding source). Reuse the brief and ask only for material missing context.
2. **Gather evidence** if current-state: pull from interviews, tickets, analytics, recordings, or run a dogfood pass. Label each material assumption or inference and preserve source IDs.
3. **Lay out the stages** in the user's language.
4. **Compose the journey** around actions and transitions, adding only useful dimensions and clearly separating failure branches from the main path. Keep evidence traceable without dominating the narrative.
5. **Mark consequential moments** and supported emotion where useful; omit empty charts. Use task failure and recovery evidence for prioritization.
6. **Storyboard** decisive moments when requested or useful; avoid expanding a simple map request into a separate production workflow.
7. **Verify readability and rank opportunities**, keeping detailed evidence and alternatives accessible separately from the main map.

## Pitfalls

- **Inside-out mapping.** Writing the map from the company's process instead of the person's experience. If your stages are your internal funnel names, you're mapping your org, not their journey.
- **The average user.** A map for "everyone" describes no one. Fix the persona.
- **No evidence.** A confidently-drawn current-state map built entirely from assumption is worse than no map, because it launders guesses into shared "truth." Label assumptions; validate the high-stakes ones.
- **Dogfood as customer research.** A dogfood pass can expose product behavior and recovery gaps, but cannot prove customer prevalence, sentiment, or motivation.
- **Emotional prioritization.** A dramatic trough can be low-reach or easy to recover from; rank task failure, severity, reach, and recovery; track confidence and investigation priority separately from impact and effort.
- **Stopping at the picture.** For a decision-oriented map, explain which opportunity deserves action or further investigation and why.
- **Mapping everything.** Too broad a scope yields a shallow map. One persona, one scenario, real depth.

- **Evidence theater.** A dashed line of unknowns, repeated caveats, or source tags in every sentence adds visual weight without understanding. State gaps once and retain traceability in detail.
- **Template completion.** Filling seven rows is not the goal. The map must reveal the person’s sequence, transitions, and obstacles; remove dimensions that contribute nothing.
