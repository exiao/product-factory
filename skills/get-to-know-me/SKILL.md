---
name: get-to-know-me
description: Learn the user's role, current work, goals, and working preferences through a short conversation. Use when the user asks to introduce themselves to an agent or create or refresh their personal working profile.
---

# Get to know me

Learn enough about the person to help with their work. Use this for an introduction or a meaningful change in their role or goals. Everyday requests can use the context already available.

## Start with what you know

Read the current conversation and any profile or project instructions the user has provided. Reuse their answers and flag anything that may be out of date. Ask before looking through other personal files or past chats unless that access is already authorized.

A job title tells you some things, but it does not tell you their priorities or how they want to work. Keep the user's statements separate from your guesses.

## Have a short conversation

Ask about the gaps that would change how you help. Useful questions include:

- What is your role, and what are you responsible for?
- What are you working on now? What would a good outcome look like?
- Which goals and constraints matter most?
- How do you want the agent to communicate, make decisions, and involve you?

Adapt the questions to what is missing. Batch related questions using the available question tool or ask them together in chat. Let the user skip a question. Ask a follow-up when an answer needs clarification, and stop when you have enough context to support their work.

Collect only information useful for this purpose. The user can share relevant experience or preferences without giving private details. Connecting company data belongs to [connect-your-data](../connect-your-data/SKILL.md).

## Show the profile before saving it

Return a short draft in plain language. Include the role, current work, goals, constraints, and preferences the user actually shared. Mark unanswered questions or uncertain interpretations. Ask what they would change and where they want it saved.

When the user agrees to the content and location, update the existing profile or project instructions. Preserve unrelated content and customizations. If no suitable record exists, propose a small profile file in the user's chosen location. A public repository may not be suitable for personal details.

Follow the runtime's rules for memory updates. Approval to save a project file does not authorize changing global instructions or memories. Keep project-specific goals in the project record and link to an existing personal profile when useful.

Read back the saved file and report its location. For a read-only request, finish with the draft. A saved profile helps future agents only when their environment loads it or points them to it; do not promise automatic recall.
