---
name: verify-feature
description: Prove a code change works by running the application and observing the real CLI, API, UI, or agent surface with runtime evidence. Use for requests to verify, prove, or dogfood a feature change.
---

# Verify feature

Verification is runtime observation. Read the diff, identify the user-facing surface reached by the changed code, run the app or service, drive the smallest path that executes the change, and capture the result. Tests, typechecks, imports, and code reading can support a report but do not substitute for reaching the real surface.

Start by stating the commit/diff scope and whether the change is visual, behavioral, backend, CLI, or configuration. Map it to a surface: terminal for CLI/TUI, an HTTP request for an API, a real browser capture for web UI, the native simulator for native UI, or the running agent for prompt/config changes. If a full app cannot build or the feature is isolated behind auth, use a throwaway harness containing the real public component/export and label that limitation.

Drive the changed behavior, including the claimed interaction and its resulting state. For destructive, publishing, sending, or external-write paths, use a dry-run or safe target; otherwise verify surrounding behavior and clearly mark the live path untested. For visual changes, capture matched before/after states from the same route, viewport, auth state, data, and capture method. A new surface or a non-visual change may use an after-only capture when that exception is stated.

Use `shot-scraper` or the in-app browser for browser verification. Do not install tools or publish evidence automatically. A browser PASS needs an attached screenshot; an interaction claim needs a capture that performs the interaction and shows its result. New-tab links require driving the new tab or window, not treating a same-tab timeout as a product failure.

Probe at least one realistic edge case or failure path. Record method, exact route/command, evidence paths, what was not tested, and a verdict of PASS, FAIL, BLOCKED, or INCONCLUSIVE. Preserve the user's requested review/fix/publish scope: verification does not authorize changing code, pushing, or publishing.

When a consequential or recurring failure can be replayed, preserve its minimal request, relevant starting state, observed failure, verifier, and reset instructions using the [failure-to-eval handoff](references/failure-to-eval.md). Reuse existing fixtures; ordinary one-off verification does not require a new harness or case library. Keep expected answers and failure diagnoses out of the executor's inputs.

For a comparative improvement claim, run baseline and candidate with equivalent starting state, tool access, and evaluator configuration; retain both outcomes and material time/cost differences. An after-only check proves the observed behavior, not improvement over the baseline. A replay or simulation supports only the behavior it exercises; retain real-surface verification for live claims.

Read [references/runtime-evidence.md](references/runtime-evidence.md) for the report and before/after rules, and [references/inert-feature-probe.md](references/inert-feature-probe.md) when a change may be wired into no real caller.
