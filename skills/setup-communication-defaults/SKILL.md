---
name: setup-communication-defaults
description: Set or update cross-project communication preferences for Codex and Claude Code in their global instruction files. Use when the user wants defaults for questions, assumptions, visual explanations, feedback, or decision checkpoints.
---

# Set up communication defaults

Help the user set how their coding agents communicate across projects. Save a short working agreement in each requested tool's global instructions. Installing this skill alone does not change those instructions.

## Find the right files

Reuse the user's choice of tools and preferences. If the target tools are unclear, ask which ones to configure. Read the existing global instructions before proposing changes.

| Tool | Global user instructions | What to check |
| --- | --- | --- |
| Codex | `AGENTS.md` inside `CODEX_HOME`, which defaults to `~/.codex` | A nonempty `AGENTS.override.md` takes precedence. Explain this before choosing the file to edit. |
| Claude Code | `~/.claude/CLAUDE.md` in the default configuration | Check for a custom configuration directory and verify its instruction location in the current tool documentation. |

Follow existing imports and inspect symlink targets before editing. Keep the user's file organization. Do not copy these preferences into every project's instruction file. Project instructions and explicit task requests may change how these defaults apply.

## Choose the defaults

Use the user's stated preferences first. For gaps, offer the starter below and explain any meaningful conflict with their existing instructions. Ask about unresolved choices together, using a question tool when available or plain chat otherwise.

Keep the agreement about communication. Project goals, personal background, model configuration, and tool permissions belong in their existing locations.

```markdown
## Communication defaults

- Before a substantial new task, summarize the intended outcome and problem in 2–3 sentences. For a simple question or small edit, answer or act directly.
- Reuse what we have already agreed. Ask questions together when missing information could change the outcome, scope, or an important decision. Continue independent work while waiting; silence is not an answer.
- Distinguish evidence from assumptions. Make consequential assumptions visible before relying on them.
- Give your own assessment and explain disagreements with concrete reasons. Change your view when the evidence changes. When I correct you, check the work and fix it rather than inventing a reason to agree.
- Use a sketch, diagram, table, chart, or interactive example when it makes the idea easier to understand. Choose the simplest format that helps; a short answer can be enough.
- Show actual drafts, designs, or prototypes when a decision depends on seeing the work. Explain the choices and tradeoffs, and ask for my judgment at unresolved consequential decisions.
- Apply my feedback to the affected work and decisions. Keep progress updates concise, and finish with the result, verification, and remaining limitations.

These are defaults. Follow explicit task requests and applicable project instructions. This agreement does not grant permission to publish, spend, deploy, or message others.
```

Adapt this text to the user's preferences. Do not add a mandatory interview, review page, or approval step to every task. When a question tool or visual tool is unavailable, use ordinary chat.

## Save without losing customizations

When the user has requested setup or accepted a concrete proposal, apply the agreed changes. A request for suggestions alone calls for a draft. Ask before resolving a conflict that would remove or reverse an existing preference.

Show a concise summary of the changes and the target paths. Back up existing files locally outside the repository before editing. Update the existing communication section, or add one if needed. Preserve unrelated instructions and imports; rerunning the skill should not add duplicate sections. If a file changes while you are working, reread it before saving.

If Codex has a global override, do not silently write a shadowed base file or remove the override. Ask whether the user wants these defaults in the active override or wants to change their override arrangement. Report a blocked or skipped tool separately if its files are inaccessible.

## Check the result

Read the saved files and inspect the diff. Confirm that the agreed preferences appear once and existing instructions remain intact. Report the exact files changed and how to restore the backups.

Start a fresh session in each configured tool to check that it loads the defaults, when the environment supports this. If you cannot check loading, say that the files were updated but session loading remains unverified. File contents and a loading check do not prove that an agent will follow every preference.

For a particular product task, [product-factory](../product-factory/SKILL.md) handles clarification and design decisions. Use [review-with-me](../review-with-me/SKILL.md) when the user needs an interactive place to inspect and comment on artifacts.

## Sources

Instruction locations checked on October 10, 2026. Verify current documentation when the installed tool uses a different configuration.

- [Codex global guidance and instruction precedence](https://developers.openai.com/codex/guides/agents-md)
- [Claude Code user instructions and memory loading](https://code.claude.com/docs/en/memory)
