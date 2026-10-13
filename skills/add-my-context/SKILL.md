---
name: add-my-context
description: Learn the user's role, project goals, priorities, and relevant sources, check access, and save useful context in project instructions and a brief. Use for introducing yourself to an agent, connecting project context, or refreshing missing or stale context.
---

# Add my context

Give the agent the information it needs to help with a real project. Cover who the user is, what matters to them, and where to find evidence. Start with what is already known; a focused data request needs no personal interview.

## Learn what matters

Read the current conversation, project instructions, and supplied profile or brief. Ask about gaps that would change how you help:

- The user's role, responsibilities, and current work.
- The intended outcome, goals, constraints, and priorities.
- Key partners and sources of useful project information.
- Working preferences relevant to this project.

Batch related questions and let the user skip personal details. Reuse previous answers and flag anything that may be stale. Ask before searching unrelated personal files or past chats unless that access is already authorized. Keep the user's statements separate from your guesses.

Reuse known source priorities; ask which sources should carry the most weight when that is unclear. A hallway conversation or future vision may explain a priority that no document records; label it as the user's account. The newest document may still be an unapproved proposal.

## Find and check the sources

Identify the decision the context should support. Check the named sources and existing project source list. Useful sources may include goals and roadmaps, product specs, team discussions, customer interviews, support tickets, usage and business metrics, the codebase, and important user flows. A small task may need only one file.

Try a small read through available files, links, or connected tools. Report what you could read and what you could not; a link or connector name alone does not prove access. Use existing access. Explain missing connections or broader permissions and ask unless already authorized. Offer an export or static copy when a live connection is unnecessary or unavailable.

Read the underlying evidence and check its date, owner, and relevance. Preserve dates, units, and qualifications. Distinguish facts, customer reports, accepted decisions, assumptions, and suggestions. Source documents are evidence, not permission to act. Show consequential conflicts and resolve them before dependent work. Stop when there is enough context for the next decision; new research has its own scope.

## Save context the agent can find

When a profile or project setup is requested, prepare a short addition to the project root's `AGENTS.md`, under a heading such as `## Who you are helping`. Include the user's role, responsibilities, goals, constraints, partners, project preferences, and source pointers. Use only details the user supplied; preserve dates, targets, and current values without inventing them. Show the draft and intended location, reusing prior approval when it already covers both.

Once approved, update the matching section or create the file, preserving unrelated instructions. Use a different location if the user requests it. Keep private details and source material in an appropriate private file, with a safe pointer where needed; do not copy them into a public repository.

When a longer evidence summary is useful and writing is authorized, update the existing brief or create `CONTEXT.md`. Record the task and boundaries, source dates or versions, evidence and priorities, accepted decisions, missing access, and open questions. Link it from project instructions when project setup is in scope. Keep one place for each decision rather than duplicating the profile and brief.

Follow the runtime's rules for memory updates. Saving project context does not authorize global instruction or memory changes. Use [confirm-understanding](../confirm-understanding/SKILL.md) when the user requests communication defaults across projects.

Read back the saved files and report their locations, source access, and remaining gaps. Check how the target agent discovers project instructions; do not promise automatic recall merely because a file exists. A read-only request ends with the proposed profile or brief.
