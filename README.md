# Product Factory

**Hand over the generating. Keep the thinking.**

![Artifact Review: compare concepts, keep useful parts, and direct the next revision.](docs/assets/artifact-review.svg)

An agent can build a polished answer to the wrong question. Start with your customer conversations, research, and constraints. Product Factory helps the agent investigate the problem and turn possible solutions into concepts and prototypes you can inspect.

## How it works

![Four stages connect agent work to your judgment: Define, Explore, Decide, and Deliver. Artifact Review carries feedback into revised work throughout.](docs/assets/workflow.svg)

Use Artifact Review to decide what to keep, combine, revise or leave out. Once you agree on the design, Make It Work implements it and checks the real workflow against your criteria. If new evidence changes the problem, return to that decision.

## The main skills

| Skill | What it does |
| --- | --- |
| [`software-factory`](skills/software-factory/SKILL.md) | Guides research and design, then hands implementation to Make It Work. |
| [`artifact-review`](skills/artifact-review/SKILL.md) | Lets you compare work, leave feedback and request revisions. |
| [`make-it-work`](skills/make-it-work/SKILL.md) | Implements an agreed outcome, fixes issues and verifies the real workflow. |

This repository supplies **26 skills** that guide how the agent works. Model access, browser tools, and deployment accounts come from your environment.

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
