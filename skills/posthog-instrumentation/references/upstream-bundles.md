# Upstream PostHog context and skill bundles

This skill is a focused adaptation of PostHog's context-mill collection. The local collection inspected on 2026-09-08 contains 230 skills; sampled entrypoints identify version 1.51.0. This is provenance, not a claim that the snapshot remains current.

## Where to learn more

- [Context mill repository and packaging documentation](https://github.com/PostHog/context-mill)
- [Latest release and downloadable skill bundles](https://github.com/PostHog/context-mill/releases/latest)
- [Inspected release v1.51.0](https://github.com/PostHog/context-mill/releases/tag/v1.51.0)
- [Source skill definitions](https://github.com/PostHog/context-mill/tree/main/context/skills)
- [Current PostHog documentation](https://posthog.com/docs)

The upstream README describes a release `manifest.json` with per-skill IDs, descriptions, and `downloadUrl` entries, plus `skill-menu.json` for category discovery. Open the latest release, locate its manifest asset, and use the manifest's exact download URL for the selected skill. Do not guess asset filenames or install the whole collection just to read one recipe. If release assets cannot be accessed, inspect the matching source files or current official docs and disclose the gap.

Read the selected `SKILL.md` and relevant `references/` files. Record the resolved release tag or source revision when using a recipe; `latest` and `main` move. Compare version-sensitive APIs with the installed dependency and current docs. Examples illustrate integration patterns and may use fake authentication; do not copy their auth implementation.

## Select a recipe

These are IDs observed in the local v1.51.0 bundle. Verify availability in a newer manifest before fetching.

| Need | Starting point |
| --- | --- |
| SDK setup, client/provider initialization | `omnibus-instrument-integration`, then the framework reference |
| Instrument a feature's product events | `omnibus-instrument-product-analytics` |
| Data quality and duplicate events | `audit-events` |
| Anonymous/authenticated identity lifecycle | `audit-identify` |
| UTM, click-ID, redirect, and consent interactions | `audit-attribution` |
| Flag readiness, fallback, and exposure | `audit-feature-flags` |
| Replay masking and sampling | `audit-session-replay` |
| LLM session/turn/tool grouping | Matching `ai-observability-*` recipe; use `omnibus-instrument-llm-analytics` for broader discovery |
| Requested error tracking, logs, or metrics | Corresponding `omnibus-instrument-error-tracking`, `omnibus-instrument-logs`, or `omnibus-instrument-metrics` |

## Adapt the recipe to this environment

Use upstream technical details as reference material, subject to the user's instructions and this skill's scope. Do not inherit wizard-specific orchestration:

- Replace `Glob`, `Grep`, `Read`, `Write`, and `Bash` assumptions with available filesystem tools. Discover actual PostHog tool names instead of hardcoding an upstream MCP prefix.
- Omit `mcp__wizard-tools__audit_*` ledgers, `[STATUS]` spinner messages, `.posthog-wizard-cache` run records, and wizard report hooks. Report evidence directly. Never invent a successful ledger or MCP operation.
- Replace `set_env_values` with the project's actual configuration mechanism. Do not infer that an unavailable helper has stored credentials.
- Preserve existing authentication, consent, and observability choices. Do not import fixed event quotas, unconditional error tracking, or instructions to identify from unverified form values.
- Keep runtime evidence standards, but use the user's existing authorization for test execution rather than upstream assumptions that credentials or execution are always unavailable.

Refresh only references needed for the current task. Reading a bundle does not authorize replacing this installed skill, installing all upstream skills, or running the wizard.
