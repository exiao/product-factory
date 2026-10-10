---
name: get-to-know-me
description: Learn the user's role, current work, goals, and working preferences, then prepare a short addition to the project's AGENTS.md. Use when the user asks to introduce themselves to an agent or create or refresh their personal working profile.
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
- Who do you work with, and where can the agent find relevant context?
- How do you want the agent to communicate, make decisions, and involve you?

Adapt the questions to what is missing. Batch related questions using the available question tool or ask them together in chat. Let the user skip a question. Ask a follow-up when an answer needs clarification, and stop when you have enough context to support their work.

Collect only information useful for this purpose. The user can share relevant experience or preferences without giving private details. Connecting company data belongs to [connect-my-data](../connect-my-data/SKILL.md).

## Show the profile before saving it

Return a short draft for the project's `AGENTS.md`, under a heading such as `## Who you are helping`. Include the role, responsibilities, current work, goals, constraints, partners, preferences, and source pointers the user actually shared. Keep dates, targets, and current values when supplied; do not invent them. Mark uncertain interpretations and ask what they would change. Reuse prior approval of the content and destination.

Default to the project root's `AGENTS.md`. Read it before editing, update the matching section if present, and preserve unrelated instructions and customizations. Create it if missing once the user agrees to the draft and location. If the user chose another file, use that location instead. Keep private details out of a shared or public file; propose a private profile with a short pointer when needed.

Follow the runtime's rules for memory updates. Approval to save a project file does not authorize changing global instructions or memories. Keep project-specific goals in the project record and link to an existing personal profile when useful.

Read back the saved file and report its location. For a read-only request, finish with the draft. A saved profile helps future agents only when their environment loads it or points them to it; do not promise automatic recall.
