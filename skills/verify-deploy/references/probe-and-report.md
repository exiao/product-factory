# Probe and report

Use the documented endpoint table for the target environment. For each row collect status, total latency, and a short safe body/status detail. Label API and frontend rows separately when paths overlap. Auth redirects are expected only when the endpoint is documented as gated; verify the authenticated path only when credentials are already configured.

For provider workflows and scheduled jobs, inspect the latest completed run and its actual conclusion. A canceled overlapping run may be benign; a failed or missing run needs the provider's stated reason. Do not infer a product failure from a wrapper timeout, a browser resource status of 0, a single cold start, or a generic event without logs.

Report in this order:

1. `Issues` with one factual line per actionable failure, or `All monitored checks healthy.`
2. Endpoint table with timestamp, status, and latency.
3. Intended versus observed deploy/commit identity for release verification; relevant workflow signal.
4. Slow retries, auth/cold-start notes, and untested surfaces.

Do not infer authorization for a deploy, rollback, restart, state-changing test, or notification from a verification-only request. Preserve any broader authorization already supplied by the user.
