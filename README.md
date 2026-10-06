# Product Factory

**Teach your coding agents how you make product decisions.**

Skills for coding agents such as Codex and Claude Code, covering research, design, implementation, and learning from past work. Each skill is a readable `SKILL.md` instruction manual you can edit and share with your team.

![Evidence and context become problem statements, storyboards, and prototypes for your judgment. Feedback returns to the shared context.](assets/product-factory.png)

## Get started

Ask your coding agent:

```text
Read https://github.com/exiao/product-factory and install its skills.
Preserve my existing customizations.
```

Then try:

```text
Use $product-factory to investigate [product problem].
Use our customer evidence and priorities. Ask about important gaps,
and show me possible directions before building a prototype.
```

## Build your product factory

![Give agents context, confirm understanding, build shareable skills, delegate, and build improvement loops.](assets/build-product-factory.png)

| Step | Workflow | What you get |
| --- | --- | --- |
| Give agents context | [`gather-context`](skills/gather-context/SKILL.md) | A brief with prioritized sources and missing evidence. |
| Confirm understanding | [`confirm-understanding`](skills/confirm-understanding/SKILL.md) | A clear task, boundaries, and unresolved assumptions. |
| Build shareable skills | Your coding agent's skill creator, or [meta-skills](https://github.com/exiao/meta-skills/tree/main/skill-creator) | Instructions that capture a repeatable team practice. |
| Delegate to coworkers | [`product-factory`](skills/product-factory/SKILL.md), [`make-it-work`](skills/make-it-work/SKILL.md), and native delegation tools | Bounded assignments and checked results. |
| Build improvement loops | [`inspect-traces`](skills/inspect-traces/SKILL.md), then an existing evaluator and hill-climbing workflow as needed | A diagnosed failure and a supported change. |

Invoke a skill with a request such as `$gather-context for this project`. Reuse existing context and decisions; run only the steps you need. See the [setup workflow](skills/product-factory/references/factory-setup.md) for handoffs.

For skill creation, audits, and measured skill optimization, see [meta-skills](https://github.com/exiao/meta-skills): [skill-creator](https://github.com/exiao/meta-skills/tree/main/skill-creator), [skill-audit](https://github.com/exiao/meta-skills/tree/main/skill-audit), and [skill-improver](https://github.com/exiao/meta-skills/tree/main/skill-improver). Use your coding agent's existing creator when available. These external skills are optional and are not bundled here.

Delegation means assigning a concrete outcome, context, boundaries, and completion check to an agent coworker, then inspecting what it delivers. Trace inspection explains what happened; hill-climbing compares candidates against an evaluator and keeps supported improvements. A one-off correction may need only a scoped fix and recheck.

## Start with these skills

| Skill | When to use it |
| --- | --- |
| [`product-factory`](skills/product-factory/SKILL.md) | Investigate a product problem and explore directions. |
| [`design-mode`](skills/design-mode/SKILL.md) | Create designs, prototypes, or visual alternatives. |
| [`artifact-review`](skills/artifact-review/SKILL.md) | Choose, combine, or revise prepared work. |
| [`make-it-work`](skills/make-it-work/SKILL.md) | Implement the agreed outcome and verify it. |
| [`inspect-traces`](skills/inspect-traces/SKILL.md) | Find mistakes and repeated corrections in past agent work. |

For focused work, try [explore-unknowns](skills/explore-unknowns/SKILL.md) to uncover assumptions, [design-review](skills/design-review/SKILL.md) to check usability and accessibility, or [synthetic-userstudies](skills/synthetic-userstudies/SKILL.md) for simulated walkthroughs. Simulated findings are hypotheses, not customer evidence.

[Browse all 32 skills](skills/).

## For coding agents

Reading the accompanying article? Open [this repository](https://github.com/exiao/product-factory) for the actual instructions.

- Read project instructions and the relevant `SKILL.md`, loading references as needed. Use the [product workflow](skills/product-factory/references/product-workflow.md) for a full initiative.
- Reuse accepted decisions, ask about important gaps, and verify results. Keep evidence and assumptions distinct.
- Install only when requested. Copy complete skill folders into the target agent's supported directory; compare existing copies and preserve customizations. For Codex, use `$CODEX_HOME/skills`, defaulting to `~/.codex/skills`.
- Report missing tools or access. Skill installation does not authorize publishing, spending, deployment, or messages.

<details>
<summary>Runtime requirements and updates</summary>

Model access and tools come from your coding-agent environment. Research needs web access; browser QA, image generation, and deployment need the corresponding tools and accounts. Native iOS testing needs macOS and Xcode.

Artifact Review includes a review template and an optional Codex feedback bridge. Saved feedback is not proof of dispatch or completed revisions. Impeccable's launcher may download its pinned engine on first use.

Pulling this repository does not update installed copies. When replacing `software-factory` with `product-factory`, preserve customizations and retire the old folder. Likewise, replace retired `design-eval` and `ui-lint` copies with `design-review`.

[CI](.github/workflows/validate.yml) checks metadata, links, and review persistence and dispatch. It does not measure downstream agent performance.

</details>

## Credits

- [Impeccable](https://github.com/pbakaus/impeccable) by [Paul Bakaus](https://github.com/pbakaus): bundled design skill and tooling.
- Anshu Chimala's [How to turn your AI into a world-class designer](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world): [creative exploration guidance](skills/design-mode/references/creative-exploration.md), adapted from the accessible portion of the article.

Original source links and license notices remain with the material; this repository does not relicense it or imply endorsement.
