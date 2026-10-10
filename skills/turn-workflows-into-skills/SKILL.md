---
name: turn-workflows-into-skills
description: Help a user turn a recurring work process into a reusable coding-agent skill. Use to choose a workflow, capture how it is done, and create or revise the skill with an available skill creator.
---

# Turn workflows into skills

Pick a piece of work you want an agent to repeat, then teach it how you do that work. Start with one workflow, such as reviewing a PRD, analyzing usage, or preparing a customer interview.

## Choose the workflow

Reuse the workflow named in the request. If none is named, ask what the user does repeatedly and which task they would like to delegate. Help them choose a concrete starting point with recognizable inputs and a useful result.

Inspect the available skills before creating another. If one already covers the job, propose a focused update rather than a duplicate. Keep current project facts and priorities in project context; a skill captures the method agents can reuse.

## Capture how you do it

Use an actual example, existing instructions, and feedback when available. Ask the user to walk through missing decisions, rather than asking them to write the whole instruction manual.

Find out:

- What starts the work, and what inputs or sources it needs.
- What the user actually does, including choices that depend on the situation.
- What makes the result useful, and what common mistakes matter.
- What the agent can decide, when it should ask, and where it should stop.

Batch related questions and reuse answers already given. A clear workflow needs no extra interview. Keep examples grounded in supplied work; label invented examples and proposed quality criteria.

## Build the skill

Summarize the method and resolve important gaps before writing instructions that depend on them. Use the coding agent's available skill creator to create or revise the skill. If none is available, write a small skill folder containing `SKILL.md` with a lowercase hyphenated `name`, a description of when to use it, and the instructions.

Put the skill in the requested repository or agreed location. Keep the steps clear, preserve the user's decisions and permissions, and include only references, templates, or scripts the workflow needs. Use portable source pointers; keep credentials and private examples out of a shared skill. Installation or publication needs its own authorization.

## Try it on real work

Run the available format and link checks. When a useful trial is possible within the request's scope, give an agent the skill and a representative task, then inspect the actual result against the user's criteria. Keep the answer key and prior critique out of the executing agent's inputs. Use a safe copy of the inputs for work that changes files or state.

Fix problems shown by that trial and recheck the affected result. If tools, access, or user input prevent a trial, finish the skill and report what remains untested. Valid formatting alone does not prove the skill works well.

Show the skill's location, what it does, and a concrete invocation, such as `$review-prd path/to/PRD.md`. Explain what was checked and how the user can edit and share it. Stop at the requested skill; repeated optimization or a full benchmark is separate work. For measured comparisons, use an available evaluation workflow.
