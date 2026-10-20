# Product Factory

Skills for coding agents like Codex and Claude Code to help with product research, design, and implementation. Each skill is a `SKILL.md` file with instructions you can read, edit, and share.

Companion to How to build a product factory.

![An agent uses project context to create problem statements, storyboards, and prototypes for you to review.](assets/product-factory.png)

## Get started

Paste this into your coding agent:

```text
Read https://github.com/exiao/product-factory and install its skills.
Preserve my existing customizations.
```

See the [installation guide](docs/installation.md) for setup, updates, and required tools.

Then give it a real task:

```text
Use $product-factory to investigate [product problem].
Use our customer evidence and priorities. Ask about important gaps,
and show me possible directions before building a prototype.
```

[`product-factory`](skills/product-factory/SKILL.md) guides the work from understanding the problem to a prototype and implementation. It uses [`design-mode`](skills/design-mode/SKILL.md) for design, [`review-with-me`](skills/review-with-me/SKILL.md) for feedback, and [`make-it-work`](skills/make-it-work/SKILL.md) to build and verify the agreed outcome. You can also invoke these skills directly.

## Follow the article

Use these skills to set up how you work with agents. Start where you need help; reuse setup you've already done.

| Step | Skill | What it helps you do |
| --- | --- | --- |
| 1. Give agents your context | [`add-my-context`](skills/add-my-context/SKILL.md) | Save your role, goals, and source locations in project instructions, and check the agent can read the sources. |
| 2. Confirm their understanding | [`confirm-understanding`](skills/confirm-understanding/SKILL.md) | Ask questions, check assumptions, and explain ideas visually. Save communication preferences when requested. |
| 3. Build shareable skills | [`build-skills`](skills/build-skills/SKILL.md) | Find skills to install or create for your recurring work. |
| 4. Delegate your work | [`product-factory`](skills/product-factory/SKILL.md), [`make-it-work`](skills/make-it-work/SKILL.md), [`review-with-me`](skills/review-with-me/SKILL.md) | Coordinate assignments with native agent tools, inspect the work, and request revisions. |
| 5. Build improvement loops | [`inspect-traces`](skills/inspect-traces/SKILL.md), [`build-eval`](skills/build-eval/SKILL.md), [`hill-climb`](skills/hill-climb/SKILL.md) | Find recurring problems in past work, turn them into repeatable tests, then test improvements within a budget. |

[Browse all skills](skills/) or see [meta-skills](https://github.com/exiao/meta-skills) for more tools to create, audit, and improve them.

## For coding agents

If you're reading the article as an agent, use this repository for the full instructions.

Read the project's instructions and the relevant `SKILL.md`. Load its references as needed.

For detailed steps, read the [product workflow](skills/product-factory/references/product-workflow.md) or [factory setup guide](skills/product-factory/references/factory-setup.md).
