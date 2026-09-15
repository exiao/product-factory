# Setup and runtime requirements

[Back to the README](../README.md)

## Install safely

Requires Git and Python 3.8 or newer. You can also download and extract the repository ZIP.

The installer copies skills into `$CODEX_HOME/skills` (default `~/.codex/skills`). It checks all destination names before copying and refuses to overwrite existing folders. Back up conflicting folders outside the skills directory before reinstalling; preserve unrelated or customized skills.

To inspect the bundle without changing your installation:

```sh
python3 install.py --dest ./preview-skills
```

If copying fails, the installer removes the folders created by that attempt. Fix the reported permissions or disk-space problem and rerun. An abrupt process kill or failed cleanup may require moving those newly created folders to a backup manually.

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

`git pull` updates this checkout, not previously installed copies. If you installed the original 55-skill bundle, back up its installed folders outside your skill directory before reinstalling this 26-skill version. Only move folders you installed from this bundle; preserve unrelated or customized skills. The installer deliberately does not delete or overwrite existing skills.

Installing these skills grants no authorization to publish, spend, or contact people. Keep credentials and deployment targets in your own environment.
