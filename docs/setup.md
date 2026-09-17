# Setup and runtime requirements

[Back to the README](../README.md)

## Install safely

Requires Git and Python 3.8 or newer. You can also download and extract the repository ZIP.

The installer copies skills into `$CODEX_HOME/skills` (default `~/.codex/skills`). Run it from this checkout:

```sh
python3 install.py
```

A fresh install checks destination skill names before copying and refuses existing folders. It saves `.product-factory-install.json` in the destination with hashes of the files it installed. Keep this receipt: it lets later updates distinguish bundle files from local customizations.

To inspect the bundle without changing your installation:

```sh
python3 install.py --dest ./preview-skills
```

If copying fails, the installer removes the folders created by that attempt. Fix the reported permissions or disk-space problem and rerun. The destination must be outside the source `skills/` directory. An abrupt process kill or failed cleanup needs inspection before retrying: back up affected files and remove `.product-factory-install.lock` only after confirming no installer is running.

## Runtime requirements and limits

These are agent instructions, not a standalone application or a bundle of model access:

- Use an agent runtime with filesystem and shell access. Research needs web access; browser/native QA needs the appropriate browser or simulator tools.
- Make It Work selects reviews for the changed surface and uses independent subagents when available and authorized. Without them, run the applicable checks directly and disclose the review limit. Goal tracking and recurring follow-ups require an explicit user request and runtime support; ordinary delivery uses the existing task record. Model names in supporting guidance may need mapping to models available in your account.
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

`git pull` updates this checkout, not installed copies. For an installation with a receipt:

```sh
git pull --ff-only
python3 install.py --update
```

Use the same `--dest` for custom locations, for example `python3 install.py --update --dest ./preview-skills`.

Updates replace unmodified managed files and add new bundle files. Files removed upstream are deleted only when their installed contents still match the receipt. Local additions, modified files and local deletions are preserved; conflicts are reported with a nonzero exit status even when other files update successfully. A new skill cannot be mixed into an existing unowned skill folder. Symlinks at managed paths are refused before updating.

Back up each customization outside the skills directory before resolving a conflict. To accept upstream for a managed file, copy the current checkout version to its installed path and rerun `--update`. For an unowned file or folder collision, move it to your backup location first. To keep a custom version, leave the conflict in place; it will keep being reported. Retrying never adopts a conflicting custom file as the new baseline.

Older installations without a receipt cannot be updated automatically. Install into an empty preview directory, compare against your installed skills, and back up only the bundle folders you intend to replace before performing a fresh install. Preserve unrelated skills and customizations, including any skills from the original 55-skill bundle. Do not fabricate a receipt for an older installation.

## Repository checks

Run the same checks as CI before publishing changes:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These check Markdown file links, skill metadata, inventory consistency and the installer against temporary destinations. They do not install into your real skills directory or prove downstream product behavior. See [workflow ownership](workflow.md) for the handoffs these skills implement.

Installing these skills grants no authorization to publish, spend, or contact people. Keep credentials and deployment targets in your own environment.
