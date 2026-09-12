---
name: posthog-instrumentation
description: Add, repair, or audit PostHog instrumentation in application code, including event capture, identity, marketing attribution, and LLM traces. Use for SDK setup and instrumentation correctness; ordinary analytics queries and PostHog account operations belong to the PostHog plugin.
---

# PostHog instrumentation

Make application telemetry answer the intended product question reliably. Preserve the user's scope: an audit reports findings; a requested implementation or fix changes the relevant code. Do not enable unrelated tracking products merely because an upstream recipe includes them.

## Choose the relevant guidance

- For event, identity, attribution, or feature-flag correctness, read [audit checks](references/audit-checks.md).
- For SDK installation, framework-specific code, LLM adapters, or deeper audits, read [upstream bundles](references/upstream-bundles.md). It includes the original collection and maintained release links. Fetch only the relevant recipe and its referenced files.
- Use the installed PostHog plugin for live schema discovery, queries, and account operations when available. Discover actual tool names and resolve the project before accessing account data. Missing account access need not block source inspection; clearly mark live checks as unverified.

## Implement or diagnose

Inspect the framework, installed SDK versions, package manager, initialization, authentication lifecycle, and relevant capture sites. Reuse existing clients and identifiers. Check current official SDK documentation before selecting imports or APIs; bundled examples are versioned snapshots.

Define the event's meaning, successful trigger, owner (client or server), stable identity, and minimal properties before adding capture. Choose events for the requested behavior without a fixed event quota. Avoid counting the same business action on both client and server. Identify from the authenticated user after authentication succeeds; reset identity on logout where appropriate.

Use existing configuration conventions. Distinguish the ingestion/project token from a personal API credential; never put a personal credential in client code. Preserve consent and data minimization settings. Follow existing secret handling, keep real credentials out of committed examples and reports, and verify behavior when optional telemetry configuration is missing.

For LLM instrumentation, choose the adapter for the actual agent framework/provider, including gateway base URLs. Preserve one session per conversation, one trace per turn, and a span per tool execution when supported. Check whether the framework already emits spans before adding duplicates. Preserve the app's prompt/completion capture policy; do not assume full text capture is appropriate.

## Verify the result

Exercise the smallest representative flow using existing authorized test credentials and fixtures. Check imports/builds as appropriate, then inspect actual capture payloads or received PostHog events. A clean diff alone does not prove delivery.

Verify event count, properties, identity, and attribution across the relevant transition. For LLM traces, use two turns in one conversation and a tool call when applicable to check grouping. Avoid paid model calls unless covered by the user's authorization; use existing fixtures where possible and state their limits.

Report source findings with file/line evidence, observed runtime results separately, and any checks unavailable due to account access or untriggered flows. If delivery was not observed, say the instrumentation is implemented but delivery is unverified. Include the upstream recipe/version consulted when it materially informed the change.
