# Installing and updating skills

Ask your coding agent to install the skills you need from this repository. Copy complete folders, including references, scripts, and templates, into the agent's supported skills directory. For Codex, use `$CODEX_HOME/skills`, which defaults to `~/.codex/skills`.

Compare any existing copies before replacing them, and preserve your customizations. Pulling this repository does not update installed copies.

## Tools and access

Your coding agent provides the models, tools, and account access. Research needs web access. Browser testing, image generation, and deployment need the corresponding tools and accounts. Native iOS testing needs macOS and Xcode.

`review-with-me` includes a review template and an optional Codex feedback bridge. It presents work and collects feedback; native delegation tools run workers. Saved feedback alone does not mean a revision has started or finished. See the [factory setup guide](../skills/product-factory/references/factory-setup.md) for delegation details.

To save communication preferences across projects, ask `confirm-understanding` to save defaults for Codex and Claude Code. It preserves existing global instructions and checks which files each tool loads. Ordinary task clarification stays in the current conversation.

## Renamed skills

When updating an older installation, compare the old and current folders, carry over customizations, and remove the replaced copies so your agent finds only the current version.

| Previous name | Current skill |
| --- | --- |
| `get-to-know-me`, `connect-my-data`, `connect-your-data`, `gather-context` | [`add-my-context`](../skills/add-my-context/SKILL.md) |
| `setup-communication-defaults` | [`confirm-understanding`](../skills/confirm-understanding/SKILL.md) |
| `turn-workflows-into-skills`, `turn-workflows-to-skills` | [`build-skills`](../skills/build-skills/SKILL.md) |
| `inspect-my-traces` | [`inspect-traces`](../skills/inspect-traces/SKILL.md) |
| `make-an-eval` | [`build-eval`](../skills/build-eval/SKILL.md) |
| `hill-climber` | [`hill-climb`](../skills/hill-climb/SKILL.md) |
| `software-factory` | [`product-factory`](../skills/product-factory/SKILL.md) |
| `artifact-review` | [`review-with-me`](../skills/review-with-me/SKILL.md) |
| `design-eval`, `ui-lint` | [`design-review`](../skills/design-review/SKILL.md) |

Compare older `confirm-understanding` copies too; the current skill includes optional global setup. Existing reviews retain their saved-feedback keys. The bundled design workflow uses `design-mode`; preserve your design customizations when updating it.

[CI](../.github/workflows/validate.yml) checks skill metadata, local links, and review persistence and dispatch. It does not measure agent performance on your tasks.
