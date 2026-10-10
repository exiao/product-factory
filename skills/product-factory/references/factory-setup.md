# Set up the six-part workflow

Use this guide when the user asks to establish or improve how their coding-agent coworkers operate. It sets up working practices; the separate [product workflow](product-workflow.md) develops a particular product initiative. Reuse completed setup and run only the steps the task needs.

| Step | Workflow or tool | Result carried forward |
| --- | --- | --- |
| Tell your agent about you | [get-to-know-me](../../get-to-know-me/SKILL.md) | A user-reviewed profile of their role, work, goals, and preferences. |
| Connect agents to your data | [connect-your-data](../../connect-your-data/SKILL.md) | Checked source access, relevant context, and a brief with explicit gaps. |
| Turn workflows into skills | [turn-workflows-into-skills](../../turn-workflows-into-skills/SKILL.md), using the available skill creator | A recurring workflow captured as editable instructions, with verification limits. |
| Change how agents communicate | [Product Factory's clarification step](../SKILL.md#clarify-before-dependent-work) and [review-with-me](../../review-with-me/SKILL.md) | Questions that resolve important gaps and actual work the user can judge. |
| Delegate to coworkers | Product Factory for product judgment; [make-it-work](../../make-it-work/SKILL.md) for delivery; native delegation tools for workers. | Bounded assignment and an inspected result, with its pending or unverified boundaries. |
| Build improvement loops | [inspect-traces](../../inspect-traces/SKILL.md), existing evaluation and hill-climbing tools as needed. | Diagnosed failure, scoped correction, and a supported keep/reject decision. |

Start at the requested step or earliest material gap. A new project may need a source-backed brief; a recurring failure may begin with trace inspection. Reuse existing context records, decisions, skills, and worker results.

Use Get To Know Me for an introduction or a change in role or goals. Reuse an existing profile for ordinary tasks. It learns about the person; Connect Your Data checks access to project evidence. Default to a short section in the project's `AGENTS.md`, preserving existing instructions. Save profile changes only after the user reviews the content and agrees to its location.

## Capture a working practice

Use [turn-workflows-into-skills](../../turn-workflows-into-skills/SKILL.md) to choose a recurring task, capture the user's method from examples and questions, and create or revise a skill with the available authoring workflow. Inspect existing skills first and keep project-specific decisions in the brief. For a separate creation, audit, or optimization toolkit, link to [meta-skills](https://github.com/exiao/meta-skills). These external skills are not included in this bundle; inspect their current instructions and prerequisites before use, and install only within the user's requested scope.

## Delegate an outcome

Choose the role before assigning work: a thinking partner evaluates or challenges a decision, a task executor produces an artifact or change, and a proactive coworker responds to an explicitly requested trigger or schedule. Native subagent support executes delegation; these role descriptions do not create new tools or schedules.

Give a worker the deliverable, relevant source evidence, settled decisions, edit boundaries, completion check, and when to escalate. Separate concurrent writers and coordinate shared browsers, ports, databases, and deployment targets. Keep trivial or tightly coupled critical work with the task owner. Workers inherit the user's scope and permissions.

Inspect worker artifacts and reproduce disputed findings before integrating them. Reuse Make It Work's reviews and runtime checks for agreed implementation. A worker's completion prose is not evidence that the integrated result works. Use the runtime's scheduling tools only for an explicitly requested recurring task, with its notification intent and stop condition.

## Learn, then measure where it matters

Trace inspection identifies the supported divergence between intent and execution. A missing source may require a context update; a simple defect may need a scoped fix and recheck. Inspection alone does not authorize editing, publication, or repeated experiments.

For repeated work with a measurable goal, reuse a runnable evaluator and available hill-climbing workflow. Hold conditions comparable, run an unchanged baseline, preserve required behavior, keep supported candidates, and stop within the agreed resource limits. For skill optimization, [meta-skills skill-improver](https://github.com/exiao/meta-skills/tree/main/skill-improver) provides a dedicated evaluated loop. A general hill-climbing workflow can also compare models, tools, environments, or other artifacts when available; it is not bundled here.

Keep diagnosis cases distinct from independent evaluation cases. Report what was exercised and what remains untested; cleaner instructions or metadata checks alone do not prove better behavior. Apply or publish an accepted result only within existing authorization.

Use `$connect-your-data` when context is missing or scattered, then `$product-factory` for a product initiative or factory setup. Product Factory handles clarification, design specialists, and artifact review, then hands agreed delivery to Make It Work. Inspect traces afterward when there is a failure or a useful learning question. A setup handoff links the source, scope, result, uncertainty, and next action in the existing project record. Skill names are not shell commands.
