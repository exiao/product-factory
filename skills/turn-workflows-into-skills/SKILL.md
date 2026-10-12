---
name: turn-workflows-into-skills
description: Recommend skills to use, install, create, or update based on the user's role, active projects, and recurring work. Use for skill planning and turning workflows into skills, with the runtime's skill creator and installer when available.
---

# Turn workflows into skills

Help the user choose useful skills for their work. Reuse a suitable existing skill, install one that fits, or capture their own method in a new skill. A named workflow can go straight to the relevant step.

## Understand the work

Read the user's role, goals, and active projects from the current conversation, project instructions, and supplied briefs. Ask about missing context that would change the recommendations. Use [get-to-know-me](../get-to-know-me/SKILL.md) when an introduction is requested; a clear task needs no separate interview.

Look for recurring work with recognizable inputs and a useful result, such as reviewing PRDs, analyzing usage, or preparing interviews. Prioritize tasks relevant to the user's current goals and explain why each is worth capturing. Keep current project facts and priorities in project context; a skill captures the method agents can reuse.

## Recommend what to use, install, or make

Inspect the runtime's installed skills and the requested repository before recommending new ones. For gaps, use the available skill installer's catalog or inspect a relevant source repository. Check the actual instructions, dependencies, and fit; a matching name or search result is not enough.

Present a short table with the task, recommended skill, action, and reason. Use these actions:

- **Use:** an installed skill already covers the task.
- **Install:** an existing skill fits but is not installed. Link its source and name any required tools or access.
- **Update:** an existing skill needs a focused change to capture the user's method.
- **Create:** no suitable skill covers the workflow.

If recommendations are all the user asked for, stop here. Otherwise proceed with the named or selected skills within the existing authorization. Ask about unresolved choices that would change what gets installed or edited; do not ask again for choices already made or delegated.

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

Put the skill in the requested repository or agreed location. Keep the steps clear, preserve the user's decisions and permissions, and include only references, templates, or scripts the workflow needs. Use portable source pointers; keep credentials and private examples out of a shared skill. A request to create a skill does not by itself authorize installation or publication.

## Install the selected skills

When installation is requested, use the runtime's built-in skill installer for existing skills. The skill creator handles authoring; the installer handles installation. Newly created local skills can be copied as complete folders into the runtime's supported skill directory when its installer does not support local sources.

Inspect the destination before installing. Preserve existing customizations and unrelated skills; resolve a name collision before replacing a copy. Follow the installer and runtime instructions for the destination and discovery. If no installer is available, use the runtime's documented installation method. Copy references, scripts, and assets with the entrypoint, then check that the installed files and relative links resolve.

Report the source, version or revision when available, destination, and any remaining setup. Distinguish files installed from a skill actually discovered and executed; report activation requirements from the runtime rather than promising immediate availability.

## Try it on real work

Run the available format and link checks. When a useful trial is possible within the request's scope, give an agent the skill and a representative task, then inspect the actual result against the user's criteria. Keep the answer key and prior critique out of the executing agent's inputs. Use a safe copy of the inputs for work that changes files or state.

Fix problems shown by that trial and recheck the affected result. If tools, access, or user input prevent a trial, finish the skill and report what remains untested. Valid formatting alone does not prove the skill works well.

Show each selected skill's location, what it does, and a concrete invocation, such as `$review-prd path/to/PRD.md`. Report which skills were reused, installed, created, or updated, what was checked, and what remains blocked or untested. Stop at the requested set; repeated optimization or a full benchmark is separate work. For measured comparisons, use an available evaluation workflow.
