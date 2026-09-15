# Product Factory

**Turn a product idea into something you can try, review, and ship.**

A collection of Codex skills for product discovery, design, implementation, and verification. Start with the person and problem. Explore the approach. Play with a standalone prototype before committing to the build.

![Product Factory workflow: define the product, try a prototype, then build and verify. Review and revise at consequential decisions.](docs/assets/workflow.svg)

## Pick your starting point

| You want to… | Use |
| --- | --- |
| Develop an idea from vision through a working product | [`$software-factory`](skills/software-factory/SKILL.md) |
| Review generated work and request changes | [`$artifact-review`](skills/artifact-review/SKILL.md) |
| Implement an agreed outcome and prove it works | [`$make-it-work`](skills/make-it-work/SKILL.md) |

Software Factory starts at the earliest incomplete stage and carries agreed decisions forward. Clear fixes go straight to implementation. You can also ask for one focused step, such as comparing approaches or reviewing a flow.

## Install

You need Git and Python 3.8+.

```sh
git clone https://github.com/exiao/product-factory.git
cd product-factory
python3 install.py
```

Skills install into `~/.codex/skills`, or `$CODEX_HOME/skills` if configured. Existing skills are never overwritten. See [setup and updates](docs/setup.md) if you have conflicts or an earlier installation.

Start a new Codex task in your project:

```text
Use $software-factory to develop a joke-writing tool for beginners.
Start from scratch and stop at a playable prototype.
```

## Try the product. Review the work.

Artifact Review creates a concise review site for the decisions that need your judgment. Product prototypes open at their own URL so you can use the actual interaction, then return with feedback. Requests for revisions stay separate from approvals.

Make It Work carries an agreed outcome through implementation, independent review, fixes, and runtime checks. Completion comes with observed evidence and any remaining limits.

## Inside the bundle

26 skills cover research, problem framing, storyboards, interaction design, prototypes, reviews, and verification. Browse the [full inventory](BUNDLE.md) or the [detailed product workflow](skills/software-factory/references/product-workflow.md).

These are instructions for your agent. Browser tools, image generation, model access, and deployment accounts come from your environment. See [runtime requirements](docs/setup.md#runtime-requirements-and-limits).
