# Product Factory

**Teach your coding agents how you make product decisions.**

Product Factory is a collection of skills for coding agents such as Codex and Claude Code. They help you give agents your team's context, teach them your working practices, and decide when they should ask for your judgment.

Use them to investigate a customer problem, compare possible solutions, review a prototype, or implement an agreed design. Each skill contains a readable `SKILL.md` instruction manual you can inspect, edit, and share.

![Customer evidence, usage data, team context, and priorities feed agents that prepare problem statements, storyboards, and prototypes for your judgment. Feedback returns to the shared context.](assets/product-factory.png)

## For people: get started

Ask your coding agent:

```text
Read https://github.com/exiao/product-factory and install its skills
for the coding agent I am using. Preserve my existing customizations.
```

Then try a task in your own project:

```text
Use $software-factory to investigate [product problem].
Use our customer evidence and priorities. Ask about consequential gaps,
and show me possible directions before building a prototype.
```

Once a direction is agreed, use `$make-it-work` to implement and verify it. Use `$artifact-review` when you want a review site, and `$inspect-traces` when you want to learn from a prior task.

## Build your product factory

![Five steps to build a product factory: give agents context, confirm understanding, build shareable skills, delegate liberally, and build improvement loops. Feedback improves context and skills.](assets/build-product-factory.png)

1. **Give agents context.** Connect the customer interviews, usage data, team discussions, code, and priorities that inform your decisions. Use your project's instructions to explain where that context lives and which sources matter most.
2. **Confirm their understanding.** Ask agents to summarize the problem and expose assumptions before building. Use questions, diagrams, storyboards, and small prototypes to check that you mean the same thing. [Explore Unknowns](skills/explore-unknowns/SKILL.md) helps investigate gaps and assumptions.
3. **Build shareable skills.** Capture how your team does research, reviews designs, or verifies a release in readable instructions. Adapt the [skills in this repository](skills/) to your team's practices and share them with your coworkers.
4. **Delegate to agents as coworkers.** Use agents as thinking partners, task executors, or scheduled researchers, depending on the work. Give them a concrete outcome and let them prepare artifacts you can inspect. Have them surface consequential decisions that need your input.
5. **Build improvement loops.** [Inspect past traces](skills/inspect-traces/SKILL.md) to find missed context, wrong assumptions, and repeated corrections. Update the relevant instructions, then evaluate whether the next attempt improves. For repeated, valuable tasks, use evals to compare changes to skills, models, tools, and environments.

These steps help you establish the factory. The [product workflow](skills/software-factory/references/product-workflow.md) describes how agents then carry a particular initiative from research through design and delivery.

## Start with these skills

| Skill | When to use it |
| --- | --- |
| [`software-factory`](skills/software-factory/SKILL.md) | Work through an unresolved product problem, research, and possible directions. |
| [`artifact-review`](skills/artifact-review/SKILL.md) | Inspect actual concepts, storyboards, designs, or prototypes; choose, combine, or request revisions. |
| [`make-it-work`](skills/make-it-work/SKILL.md) | Implement the agreed outcome, fix issues, and verify the real workflow. |
| [`inspect-traces`](skills/inspect-traces/SKILL.md) | Learn from prior agent work and identify specific changes to context, skills, or process. |

[Browse all 30 skills](skills/).

## For coding agents: read this before working

If you are reading the accompanying article as a coding agent, open [this GitHub repository](https://github.com/exiao/product-factory) for the actual skills and workflow details. The article explains the approach; each `SKILL.md` supplies task-specific instructions.

- Read the user's request and project instructions, then open the relevant [skill](skills/) and only the references needed for that task. For a product initiative, start with [Software Factory](skills/software-factory/SKILL.md) and its [product workflow](skills/software-factory/references/product-workflow.md).
- Reuse accepted context, decisions, artifacts, and criteria. Ask about consequential gaps. Keep evidence, assumptions, and simulated outcomes distinct.
- Present prepared work through [Artifact Review](skills/artifact-review/SKILL.md) when human judgment is needed. Hand agreed implementation to [Make It Work](skills/make-it-work/SKILL.md), and verify the actual result before reporting completion.
- Install skills only when the user requests installation. Copy complete skill folders, including their references, scripts, and assets, into the target agent's supported skill directory. For Codex, use `$CODEX_HOME/skills`, defaulting to `~/.codex/skills`; check the target client's current instructions for other agents. Compare existing copies and back up customizations before updating them. Pulling this repository does not update installed skills.
- Use the tools and accounts available in the user's environment. Report missing capabilities precisely. Installing these instructions grants no permission to publish, spend, deploy, or contact people.

## Requirements and updates

This repository provides instructions and supporting assets. Model access and runtime tools come from your coding-agent environment. Research needs web access; browser QA, image generation, and deployment need the corresponding tools and accounts. Native iOS testing needs macOS and Xcode.

Artifact Review includes a runnable review template and an optional fixed-task Codex feedback bridge. Local saving, acknowledged dispatch, and completed revisions are separate states. Impeccable's launcher may download its pinned engine on first use.

<details>
<summary>Updating an existing installation</summary>

When updating from a bundle with `design-eval` or `ui-lint`, retire those old installed copies after installing `design-review`, which combines their guidance. Preserve unrelated skills and customizations.

</details>

[GitHub Actions](.github/workflows/validate.yml) checks skill metadata, local Markdown links, and review persistence and dispatch. These checks do not measure downstream agent performance or prove that the factory learns automatically.

## Credits

Product Factory includes and adapts work from these projects and authors:

| Source | Used here |
| --- | --- |
| [Impeccable](https://github.com/pbakaus/impeccable) by [Paul Bakaus](https://github.com/pbakaus) | The bundled [Impeccable skill and tooling](skills/impeccable/SKILL.md), used by the design workflow. |
| Anshu Chimala's [How to turn your AI into a world-class designer](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world) | Design-mode's [creative exploration guidance](skills/design-mode/references/creative-exploration.md), adapted from the accessible portion of the article. |

Further method references are documented alongside the relevant skills. Original source links and license notices remain with the material; this repository does not relicense it or imply endorsement by its authors.
