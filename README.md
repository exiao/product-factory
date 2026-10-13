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

## Follow the article's five steps

The [product factory article](https://app.notion.com/p/V2-How-to-build-a-product-factory-3dfafc6b12bc80ecbd7fca0a23682ab4) starts with context and builds toward delegation and improvement. Try the skills on a real project and reuse setup you have already done.

| Step | Skill | What you get |
| --- | --- | --- |
| 1. Give agents your context | [`add-my-context`](skills/add-my-context/SKILL.md) | Your role, goals, priorities, and source pointers in project instructions, with checked access and a brief where useful. |
| 2. Confirm their understanding | [`confirm-understanding`](skills/confirm-understanding/SKILL.md) | A shared task interpretation, consequential questions, stated assumptions, and visual explanations. Save communication defaults when requested. |
| 3. Build shareable skills | [`build-skills`](skills/build-skills/SKILL.md) | Skills that fit your role and work, using the agent's skill installer for existing skills and skill creator for new ones. |
| 4. Delegate your work | [`review-with-me`](skills/review-with-me/SKILL.md) | Actual work and alternatives you can inspect, choose, and revise while the agent carries out the assignment. |
| 5. Build improvement loops | [`inspect-my-traces`](skills/inspect-my-traces/SKILL.md), [`make-an-eval`](skills/make-an-eval/SKILL.md), then available hill-climbing tools | Evidence of what went wrong, replayable checks, and measured improvements to skills, context, models, or tools. |

Ask your coding agent:

```text
Use $add-my-context for this project. Learn what I do, what matters,
and where to find the relevant data. Help me save it in project instructions.
Use $confirm-understanding to check our interpretation of [task].
Use $build-skills to recommend skills to make or install for my work.
Use $review-with-me to show the results of [assignment] and iterate with me.
Use $inspect-my-traces to suggest three workflows I could delegate.
```

For lasting communication preferences, ask `$confirm-understanding to save communication defaults for Codex and Claude Code`. It preserves existing global instructions and checks which files each tool loads. Ordinary task clarification uses the current conversation.

Give delegated work an outcome, context, boundaries, and a completion check. Product Factory coordinates product decisions, Make It Work owns delivery, and native delegation tools run workers. Review With Me presents their work and carries feedback into revisions; it does not create background workers or schedules. See the [setup workflow](skills/product-factory/references/factory-setup.md) for handoffs.

Optional [meta-skills](https://github.com/exiao/meta-skills) tools cover [skill creation](https://github.com/exiao/meta-skills/tree/main/skill-creator), [audits](https://github.com/exiao/meta-skills/tree/main/skill-audit), and [evaluated optimization](https://github.com/exiao/meta-skills/tree/main/skill-improver). These tools are not bundled here. Start with the agent's built-in creator when available.

Use trace inspection to diagnose or recover relevant context from earlier work. Add an eval when repeatable evidence justifies its upkeep; hill-climb against those checks within an agreed budget. A one-off correction may need only a fix and recheck. Judge the factory by the useful work it produces.

## Run a product task

| Order | Invoke | What it does | When needed |
| --- | --- | --- | --- |
| 1 | [`add-my-context`](skills/add-my-context/SKILL.md) | Check access and gather the evidence and priorities the task needs. | When project context is missing or scattered. |
| 2 | [`product-factory`](skills/product-factory/SKILL.md) | Clarify the task, investigate the problem, explore directions, design, prototype, and review with you. | Main entry point; it coordinates the specialists. |
| 3 | [`make-it-work`](skills/make-it-work/SKILL.md) | Implement the agreed outcome and verify the real workflow. | After design agreement; Product Factory can hand off within the authorized scope. |
| 4 | [`inspect-my-traces`](skills/inspect-my-traces/SKILL.md) | Find mistakes and repeated corrections to improve future work. | After a task or recurring failure. |
| 5 | [`make-an-eval`](skills/make-an-eval/SKILL.md) | Build replayable tasks and measure quality, cost, and time. | When you need repeatable evidence before comparing or optimizing agents. |

Usually, invoke `$product-factory` and ask it to carry the agreed work through delivery. It uses [design-mode](skills/design-mode/SKILL.md) for designs and prototypes and [review-with-me](skills/review-with-me/SKILL.md) for your judgment and revisions. Invoke those specialists directly for focused work; clarification does not require a separate skill call.

For focused work, try [explore-unknowns](skills/explore-unknowns/SKILL.md) to uncover assumptions, [design-review](skills/design-review/SKILL.md) to check usability and accessibility, or [synthetic-userstudies](skills/synthetic-userstudies/SKILL.md) for simulated walkthroughs. Simulated findings are hypotheses, not customer evidence.

[Browse all skills](skills/).

## For coding agents

Reading the accompanying article? Open [this repository](https://github.com/exiao/product-factory) for the actual instructions.

- Read project instructions and the relevant `SKILL.md`, loading references as needed. Use the [product workflow](skills/product-factory/references/product-workflow.md) for a full initiative.
- Reuse accepted decisions, ask about important gaps, and verify results. Keep evidence and assumptions distinct.
- Install only when requested. Copy complete skill folders into the target agent's supported directory; compare existing copies and preserve customizations. For Codex, use `$CODEX_HOME/skills`, defaulting to `~/.codex/skills`.
- Report missing tools or access. Skill installation does not authorize publishing, spending, deployment, or messages.

<details>
<summary>Runtime requirements and updates</summary>

Model access and tools come from your coding-agent environment. Research needs web access; browser QA, image generation, and deployment need the corresponding tools and accounts. Native iOS testing needs macOS and Xcode.

Review With Me includes a review template and an optional Codex feedback bridge. Saved feedback is not proof of dispatch or completed revisions.

Pulling this repository does not update installed copies. Compare changes, preserve customizations, then retire replaced folders so agents do not discover competing copies.

| Previous name | Current skill |
| --- | --- |
| `get-to-know-me`, `connect-my-data`, `connect-your-data`, `gather-context` | [`add-my-context`](skills/add-my-context/SKILL.md), combining personal and project context |
| `setup-communication-defaults` | [`confirm-understanding`](skills/confirm-understanding/SKILL.md), with optional global setup |
| `turn-workflows-into-skills`, `turn-workflows-to-skills` | [`build-skills`](skills/build-skills/SKILL.md) |
| `inspect-traces` | [`inspect-my-traces`](skills/inspect-my-traces/SKILL.md) |
| `software-factory` | [`product-factory`](skills/product-factory/SKILL.md) |
| `artifact-review` | [`review-with-me`](skills/review-with-me/SKILL.md) |
| `design-eval`, `ui-lint` | [`design-review`](skills/design-review/SKILL.md) |

If you have an older `confirm-understanding` copy, compare it with the current skill before replacing it. Copy complete folders, including references, scripts, and templates. Existing reviews retain their saved-feedback keys. The bundled design workflow uses `design-mode`; preserve personal design customizations when updating it.

[CI](.github/workflows/validate.yml) checks metadata, links, and review persistence and dispatch. It does not measure downstream agent performance.

</details>

## Credits

- Anshu Chimala's [How to turn your AI into a world-class designer](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world): [creative exploration guidance](skills/design-mode/references/creative-exploration.md), adapted from the accessible portion of the article.

Original source links and license notices remain with the material; this repository does not relicense it or imply endorsement.
