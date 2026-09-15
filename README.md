# Product Factory

**Hand over the generating. Keep the thinking.**

![Artifact Review: compare concepts, keep useful parts, and direct the next revision.](docs/assets/artifact-review.svg)

Let your agent research, prototype, and build. Bring your customer context, taste, and judgment to the work it produces. Artifact Review gives you a place to compare approaches, combine ideas, and ask for changes.

## How it works

![Four stages connect agent work to your judgment: Define, Explore, Try, and Deliver. Artifact Review carries feedback into revised work throughout.](docs/assets/workflow.svg)

Start at the earliest incomplete stage and carry agreed decisions forward. Try prototypes as standalone experiences before committing to the build.

## The main skills

| Skill | What it does |
| --- | --- |
| [`software-factory`](skills/software-factory/SKILL.md) | Coordinates vision, research, design, implementation, and verification. |
| [`artifact-review`](skills/artifact-review/SKILL.md) | Presents the work for your judgment and carries your feedback into the next revision. |
| [`make-it-work`](skills/make-it-work/SKILL.md) | Implements an agreed outcome, runs independent reviews, fixes issues, and checks the real workflow. |

Skills guide how the agent works. Plugins can bundle skills, tools, and service connections. This repository supplies **26 skills**; model access, browsers, and deployment accounts come from your environment.

[Browse all skills](BUNDLE.md) · [Detailed product workflow](skills/software-factory/references/product-workflow.md)

## Setup

Requires Git and Python 3.8+.

```sh
git clone https://github.com/exiao/product-factory.git
cd product-factory
python3 install.py
```

Start a new Codex task in your project:

```text
Use $software-factory to develop [your product idea].
Stop at a playable prototype.
```

Installs into `~/.codex/skills` or `$CODEX_HOME/skills`. Existing skills are never overwritten. See [setup, updates, and runtime requirements](docs/setup.md).
