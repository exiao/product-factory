# Product Factory

**Hand over the generating. Keep the thinking.**

![Artifact Review: compare concepts, keep useful parts, and direct the next revision.](docs/assets/artifact-review.svg)

An agent can build a polished answer to the wrong question. Start with what you know: customer conversations, existing evidence, constraints, and questions worth investigating. The agent gathers more evidence, exposes gaps, and makes alternatives you can inspect.

Use that work to challenge assumptions, weigh tradeoffs, and decide what to leave out. Artifact Review carries your corrections into the next version before the agent builds further on a mistaken premise.

## How it works

![Four stages connect agent work to your judgment: Define, Explore, Decide, and Deliver. Artifact Review carries feedback into revised work throughout.](docs/assets/workflow.svg)

Give the agent your evidence, questions, and constraints. It turns them into directions you can compare and prototypes you can try. You choose what moves forward, combine the useful parts, and cut the rest. Each choice gives the next round of work a clearer target.

## The main skills

| Skill | What it does |
| --- | --- |
| [`software-factory`](skills/software-factory/SKILL.md) | Coordinates vision, research, criteria and design, then hands delivery to Make It Work. |
| [`artifact-review`](skills/artifact-review/SKILL.md) | Presents the work for your judgment and carries your feedback into the next revision. |
| [`make-it-work`](skills/make-it-work/SKILL.md) | Implements an agreed outcome, selects relevant reviews, fixes issues and verifies the real workflow; uses independent reviewers when available and authorized. |

Skills guide how the agent works. Plugins can bundle skills, tools, and service connections. This repository supplies **26 skills**; model access, browsers, and deployment accounts come from your environment.

[Browse all skills](BUNDLE.md) · [Workflow ownership](docs/workflow.md) · [Detailed product workflow](skills/software-factory/references/product-workflow.md)

## Setup

Paste this into Codex:

```text
Install the skills from https://github.com/exiao/product-factory
```

Start a new Codex task in your project, then try:

**Develop an idea**

```text
Use $software-factory to develop [your product idea].
Show me different directions before building a prototype.
```

**Review the options**

```text
Use $artifact-review to compare these concepts with me.
Let me combine ideas and ask for changes.
```

**Build the chosen direction**

```text
Use $make-it-work to implement the agreed design
and verify the core workflow.
```

Installs into `~/.codex/skills` or `$CODEX_HOME/skills`. Fresh installs refuse existing skill folders; updates preserve customizations. See [setup, updates, and runtime requirements](docs/setup.md).
