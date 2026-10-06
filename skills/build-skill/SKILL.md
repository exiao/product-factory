---
name: build-skill
description: Turn a repeatable working practice into a readable, shareable coding-agent skill with clear routing and an observable completion check. Use for skill creation or a scoped revision, not measured optimization of an existing workflow.
---

# Build a skill

Capture the judgment and task-specific knowledge that the agent would otherwise need explained again. Use real work, supplied examples, corrections, and the team's quality bar. Do not write an instruction manual for an imagined process and present it as proven practice.

## Choose the responsibility

Inspect existing skills before adding another. Identify the request this skill should handle, the artifact or behavior it should produce, relevant inputs and evidence, and when it should stop or hand off. Revise an existing owner when the new instruction belongs there; avoid another wrapper that simply renames an existing capability.

Ask for consequential missing examples or decisions, and proceed with supported parts. Keep task-specific decisions in the project's brief; put a reusable method or recurring cross-task correction in the skill. Preserve the user's tool choices, scope, and authorization.

## Write the portable instructions

Use the runtime's skill-authoring guidance when available. Create a lowercase, hyphenated skill folder with `SKILL.md` containing YAML `name` and `description`. The name must match the directory. The description should make its responsibility and trigger distinguishable from neighboring skills.

Write the workflow's meaningful decisions, source use, output, failure handling, and completion evidence. Include worked examples only when they teach a non-obvious choice. Put substantial conditional detail in linked references; add executable helpers only for repeated deterministic work that needs them. Avoid machine-specific paths, embedded credentials, copied private records, and unavailable mandatory tools.

Default to normal skill discovery unless the user asks for explicit-only invocation. A skill instruction cannot grant permission to publish, install services, send messages, or perform another consequential external action.

## Verify and deliver

Check metadata, relative links, unfinished scaffolding, and any added helper's actual behavior. When meaningful, try the skill on a representative task in an isolated directory using supplied or sanitized evidence. Check the produced artifact against the user's outcome, not whether the agent repeated the skill's wording. Report what was exercised and what remains untested.

Deliver the editable skill folder and a sample invocation. A repository copy is not automatically installed: install or update it only within the requested scope, using the target agent's supported directory and preserving existing customizations. Structural validation is not evidence of behavioral improvement.

For repeated misses in an existing skill, use [improve-workflow](../improve-workflow/SKILL.md) to compare a baseline and a candidate rather than adding more instructions without evidence.
