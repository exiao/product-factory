# Set up the five-step workflow

Use this guide when the user asks to establish or improve how their coding-agent coworkers operate. It sets up working practices; the separate [product workflow](product-workflow.md) develops a particular product initiative. Reuse completed setup and run only the steps the task needs.

| Step | Workflow or tool | Result carried forward |
| --- | --- | --- |
| 1. Give agents your context | [add-my-context](../../add-my-context/SKILL.md) | A reviewed profile and source pointers in project instructions, with checked access and a useful brief. |
| 2. Confirm their understanding | [confirm-understanding](../../confirm-understanding/SKILL.md) | Shared intent, visible assumptions, questions, and appropriate visual explanations. |
| 3. Build shareable skills | [build-skills](../../build-skills/SKILL.md) | Reused, installed, or created skills for the user's recurring work. |
| 4. Delegate your work | [review-with-me](../../review-with-me/SKILL.md), Product Factory, [make-it-work](../../make-it-work/SKILL.md), and native delegation tools | Bounded assignments, inspected work, and feedback applied to revisions. |
| 5. Build improvement loops | [inspect-traces](../../inspect-traces/SKILL.md), [build-eval](../../build-eval/SKILL.md), and [hill-climb](../../hill-climb/SKILL.md) | Diagnosed failures, replayable evaluation, and supported changes. |

Start at the requested step or earliest material gap. Reuse profiles, source lists, briefs, and settled decisions. Add My Context combines learning about the person with access to project evidence; a focused request needs only its relevant portion. Save profile changes after review of their content and location, and preserve existing project instructions.

## Confirm understanding

Use Confirm Understanding on the current task before dependent decisions. Ask only about consequential gaps and continue independent authorized work while waiting. When the user requests lasting defaults, its [communication setup](../../confirm-understanding/references/communication-defaults.md) updates the selected tools' global instructions. Task clarification alone does not authorize those edits.

## Capture a working practice

Use [build-skills](../../build-skills/SKILL.md) to recommend skills based on the user's role and projects. Inspect existing skills first, install suitable ones when requested, and capture missing methods from examples and questions with the available skill creator. Keep project-specific decisions in the brief. For a separate creation, audit, or optimization toolkit, link to [meta-skills](https://github.com/exiao/meta-skills). These external skills are not included in this bundle; inspect their current instructions and prerequisites before use, and install only within the user's requested scope.

## Delegate an outcome

Use [review-with-me](../../review-with-me/SKILL.md) to present actual work and comparable alternatives, capture the user's judgment, and apply feedback to the next version. The assignment owner retains responsibility for research, generation, implementation, and completion. Review UI does not itself run workers or schedule future work.

Choose the role before assigning work: a thinking partner evaluates or challenges a decision, a task executor produces an artifact or change, and a proactive coworker responds to an explicitly requested trigger or schedule. Native subagent support executes delegation; these role descriptions do not create new tools or schedules.

Give a worker the deliverable, relevant source evidence, settled decisions, edit boundaries, completion check, and when to escalate. Separate concurrent writers and coordinate shared browsers, ports, databases, and deployment targets. Keep trivial or tightly coupled critical work with the task owner. Workers inherit the user's scope and permissions.

Inspect worker artifacts and reproduce disputed findings before integrating them. Reuse Make It Work's reviews and runtime checks for agreed implementation. A worker's completion prose is not evidence that the integrated result works. Use the runtime's scheduling tools only for an explicitly requested recurring task, with its notification intent and stop condition.

## Learn, then measure where it matters

Trace inspection identifies the supported divergence between intent and execution. A missing source may require a context update; a simple defect may need a scoped fix and recheck. Inspection alone does not authorize editing, publication, or repeated experiments.

For repeated work with a measurable goal, use [build-eval](../../build-eval/SKILL.md) to build or reuse replayable cases, check the grading, and report quality, cost, and time. It supports local agent runs and Harbor tasks when repeatable tool access or isolation helps. Evaluation measures behavior; optimization chooses changes using those measurements.

Reuse the runnable evaluator with [hill-climb](../../hill-climb/SKILL.md). Hold conditions comparable, run an unchanged baseline, preserve required behavior, keep supported candidates, and stop within the agreed resource limits. For skill optimization, [meta-skills skill-improver](https://github.com/exiao/meta-skills/tree/main/skill-improver) provides a dedicated evaluated loop. Hill Climb can also compare models, tools, environments, and other artifacts against the agreed evaluator.

Keep diagnosis cases distinct from independent evaluation cases. Report what was exercised and what remains untested; cleaner instructions or metadata checks alone do not prove better behavior. Apply or publish an accepted result only within existing authorization.

Use `$add-my-context` when context is missing or scattered, then `$product-factory` for a product initiative or factory setup. Product Factory handles clarification, design specialists, and artifact review, then hands agreed delivery to Make It Work. Inspect traces afterward when there is a failure or a useful learning question. A setup handoff links the source, scope, result, uncertainty, and next action in the existing project record. Skill names are not shell commands.
