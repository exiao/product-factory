---
name: people-problems
description: Frame or critique human, solution-agnostic problem statements from research, feature requests, business goals, or symptoms. Use to define the difficulty worth addressing, its evidence, and what solved would mean; not a full product vision or delivery plan.
---

# People Problems

Describe what people want to accomplish and what makes it difficult before choosing a solution. Preserve the user's audience, scope, and agreed decisions. For a framing-only request, deliver problem statements and evidence gaps. Maps, prototypes, development, and additional approval steps are outside that request. For a review-only request, report findings without changing the supplied artifact.

## Focused modes and routing

The exact mode names below are conversational requests, not shell commands or standalone skills. Use the narrow mode when the request explicitly names it or clearly asks for that operation. A broader request already authorized by the user may continue beyond the mode; otherwise keep the work local.

| Conversational mode | Target | Default output |
|---|---|---|
| `people-problems question` | Assumptions behind a named problem or decision | Assumption list with source/evidence labels, uncertainty when useful, and what would change the decision |
| `people-problems check` | Whether a named problem is established by the supplied evidence | Evidence trace with stable source IDs, observed/reported/synthetic/inferred labels, gaps, and untested checks |
| `people-problems reframe` | Wording of a named problem statement | Local annotation plus a before/after statement that preserves audience, scope, source, and certainty |

For a bare `$people-problems` invocation with no actionable surrounding request, use the available context only to offer 2–3 relevant mode suggestions with a short reason for each, then stop. When the surrounding conversation already supplies an actionable request, follow that request's scope instead of stopping for the menu. Do not create a full artifact for a local request. A review-only request is read-only: report findings and proposed local wording, but do not edit the supplied source. Read [focused modes](references/focused-modes.md) only after selecting one of these modes.

## Frame the problem

Read the supplied context and available evidence. Separate explicit user choices from interpretations of documents. For each distinct situation, identify the person, their goal, what they do now, where it breaks down, and the consequence. Explain which needs depend on or conflict with others. Keep different user types separate and select the problems that matter to the decision.

Before promoting an account into a problem, check what it actually establishes: the task, current approach, reported or observed breakdown, and consequence. A self-report remains reported evidence even when quoted exactly. Using a workaround, manual process, or several tools does not by itself establish dissatisfaction or failure; preserve evidence that the current approach works and label any proposed problem as unverified. Keep accounts about different tasks separate unless evidence supports a shared breakdown. State which parts of an inferred problem still need checking.

## Statement standard

Adapted from the user-supplied *People Problems* guide, pages 1–2. The standard below is self-contained. Keep each statement short; put the audience, situation, evidence, and measures alongside it.

Check each statement against all five principles:

- **Human, simple and straightforward:** use everyday language from the person's point of view, usually first person. Label a first-person statement you compose as a synthesis or hypothesis. Use quotation marks for customer testimony only when the words are exact and attributed.
- **Solution-agnostic:** describe the need without prescribing a feature, interface or technology. For a dashboard, feed, or AI request, explain the underlying need.
- **Company-win-agnostic:** describe the person's progress, not the company's engagement, revenue or competitive ambition. Keep business objectives separate and explain their relationship when relevant.
- **Explains why:** look behind observed behavior or a metric change to the difficulty that could explain it. Do not invent motivation or causality; label an unverified explanation as a hypothesis and state how to test it.
- **Functional, emotional or social:** identify the task, feeling or social progress that matters. One may suffice; do not force every statement to cover all three.

## Evidence and solved state

For each priority problem, answer:

1. **What people problem are we solving?** State the problem, who faces it and when, and its proposed priority.
2. **How do we know it is real?** Provide available qualitative or quantitative evidence and concrete use cases. Where evidence is absent, give a verifiable hypothesis and the observation that would support or challenge it. Keep synthetic reactions and analyst inference separate from customer evidence.
3. **How will we know it is solved?** Define the desired change in the person's experience and measures that track it, with the relevant population, baseline, target and timeframe when known. Mark unknowns and proposed targets explicitly. Explain the limits of proxy metrics; increased activity alone does not prove the underlying need was met.

When the task continues into idea selection, storyboards, prototypes, or verification, carry the statements and their evidence forward. Revisit them when evidence changes; do not rewrite the problem to fit a chosen feature.

## Deliver and hand off

Deliver the statements with answers to the three questions above and the unknowns that could change the decision. Ask only for missing choices that would change the framing. Keep competing interpretations visible when evidence does not resolve them. Preserve attribution, source context, and the distinction between observed behavior, reported experience, interpretation, and simulation.

Reuse an existing project record when one exists. Read and use the relevant skill only when that work is in scope:

- [$empathy-maps](../empathy-maps/SKILL.md) to organize what is known about people into a map.
- [$product-vision](../product-vision/SKILL.md) to choose the promise and priorities.
- [$acceptance-criteria](../acceptance-criteria/SKILL.md) to define testable success for an agreed outcome.
