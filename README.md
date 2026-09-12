# Software Factory + Make It Work

A portable snapshot of two Codex workflows and their supporting skills:

- **`$software-factory`**: product discovery, decisions, implementation, and verification; also supports focused critiques and comparisons.
- **`$make-it-work`**: own an agreed outcome through implementation, independent reviews, fixes, and runtime verification.

## Install

Requires GitHub access to this private repository, Git, and Python 3.8 or newer. Authenticate Git with your own GitHub account first, or download and extract the repository ZIP while signed in.

```sh
git clone https://github.com/exiao/software-factory-skills.git
cd software-factory-skills
python3 install.py
```

The installer copies all bundled skills into `$CODEX_HOME/skills` (default `~/.codex/skills`). It checks for name conflicts before copying and refuses to overwrite existing skills. Back up conflicting folders outside the skills directory, then rerun. To inspect the bundle without changing your installation:

```sh
python3 install.py --dest ./preview-skills
```

Start a new Codex task after installation. In your project, try:

```text
Use $software-factory to develop this idea: [person, problem, desired outcome].
Use $make-it-work to implement and verify [specific outcome].
```

If copying fails, the installer removes the skill folders created by that attempt. Fix the reported permissions or disk-space problem and rerun. An abrupt process kill or failed cleanup may require moving those newly created folders to a backup manually; never remove unrelated skills.

For product outcomes, Software Factory follows a fixed default sequence:

**Vision → research and empathy maps → outcome criteria → alternatives and illustrated storyboards → low-fi prototype → synthetic study and fixes → refined design and detailed criteria → build and verify.**

Start at the earliest incomplete stage and reuse inspected artifacts and settled decisions. Required outputs cannot be casually skipped or substituted; an explicit scope change or earlier requested finish line still takes precedence. Checkpoints need an answer only for consequential unresolved choices.

Focused operations remain available when you want a specific step, such as comparing approaches, critiquing an idea, tracing evidence, or sharpening criteria. Journey mapping, strategy, commercial validation, and desirability work remain conditional additions. Clear contained fixes go directly to implementation and verification. Adapt reviews to the actual surface (for example, installation instructions and CLI recovery for a skill bundle).

Keep project permissions, credentials, and deployment targets in your own environment. Installing these skills grants no authorization to publish, spend, or contact people.

## What's included

`skills/` contains 25 skills: the two entrypoints plus supporting product discovery, design, implementation, and verification skills. Content production, marketing, publishing, and skill-authoring workflows are excluded. Needed standalone references are kept without importing their original parent workflows. All relative Markdown file links resolve inside the bundle. See [BUNDLE.md](BUNDLE.md) for the inventory and portability changes.

## Runtime requirements and limits

These are agent instructions, not a standalone application or a bundle of model access:

- Use an agent runtime with filesystem and shell access. Research needs web access; browser/native QA needs the appropriate browser or simulator tools.
- Make It Work expects goal tracking, subagents, and recurring checks when waiting on PRs. If a capability is unavailable, report it and track the equivalent work explicitly; do not claim an independent review ran. Model names in supporting guidance may need mapping to models available in your account.
- Impeccable includes its upstream launcher and supporting files. On first use it may download its pinned platform engine from upstream GitHub releases. It needs network access for that download; see its launcher and skill for supported platforms and fallback behavior.
- Image generation, hosted user studies, and deployment tools require your own available tools/accounts. No credentials or paid subscriptions are included. Missing optional tools only block the operation that needs them.

Verified packaging and installation are separate from proving that every downstream workflow works with your accounts and runtime.

### Optional branch prerequisites

| Branch | Additional requirements |
| --- | --- |
| Image creation | Runtime image-generation tool |
| Native iOS QA | macOS, Xcode/simulator and available automation tools |
| Browser QA | Runtime browser/computer tools or the skill’s documented alternative |
| Deployment | Your own provider tools, authenticated accounts and explicit task scope |

Read the selected skill’s prerequisites before running an optional branch; this table does not provision tools or accounts.

## Updating an earlier installation

`git pull` updates this checkout, not previously installed copies. If you installed the original 55-skill bundle, back up its installed folders outside your skill directory before reinstalling this 25-skill version. Only move folders you installed from this bundle; preserve unrelated or customized skills. The installer deliberately does not delete or overwrite existing skills.
