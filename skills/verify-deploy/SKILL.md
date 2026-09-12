---
name: verify-deploy
description: Check the health of explicitly named deployed services after a release or during a health review, using their documented endpoints and available provider APIs. Use for deploy verification, production health checks, latency checks, or deploy digests.
---

# Verify deploy

This is an observational check. Determine the target services, environment, and endpoints from the user's request, repository documentation, or configured provider data. Never invent a host, substitute a similarly named service, or probe a dead/legacy endpoint. Confirm the current CLI/API shape with `--help` or provider documentation before using it. Credentials come from the environment or connector and must never appear in output.

For every explicitly monitored endpoint, record status, latency, and a bounded body summary when safe. Distinguish frontend and API paths, redirects that are expected for auth, cold-start latency, cross-origin resource status 0, and wrapper/tool failures. Retry a slow 200 once or twice before flagging a transient spike, while retaining the original measurement. For post-release verification, establish that the intended commit or deploy ID reached the target environment; health alone may describe the previous release. Read relevant existing provider runs and logs. Use documented non-destructive smoke checks when in scope; verification alone does not authorize repairs or state-changing tests.

Lead the report with actionable failures, then include the endpoint table, recent deploy signal, and any cron/workflow status. State the exact evidence, timestamp, auth state, and untested surfaces. A health check does not authorize a deploy, rollback, message, or code fix. If the user also asks for a fix, continue through the authorized repair and reverify; do not stop at diagnosis or ask for the same authorization again.

Read [references/probe-and-report.md](references/probe-and-report.md) for endpoint semantics, workflow/cron interpretation, and a compact report shape.
