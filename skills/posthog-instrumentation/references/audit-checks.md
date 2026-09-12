# Focused audit checks

Select checks that match the user's problem. Trace from the relevant user action through capture and, when accessible, into the target PostHog project. Code patterns suggest hypotheses; confirm runtime-dependent findings before describing them as defects.

## Events

- Match event names and properties to a meaningful action and its success/failure semantics. Look for capture during render, repeated effects, retries, or duplicate browser/server ownership.
- Check unstable event names, unbounded property cardinality, sensitive payloads, and missing session linkage where the analysis requires it.
- Check whether development/staging traffic reaches production. For cost findings, measure volume and downstream use before recommending removal; frequent events are not automatically useless.
- Account for SDK autocapture/pageview defaults before adding manual equivalents.

## Identity

- Follow anonymous browsing, successful login/signup, subsequent server activity, logout, and a second account on the same device.
- Check stable internal user IDs, correct anonymous-to-known association, and logout reset. Form submission alone is not proof of authenticated identity.
- Check frontend/backend identity agreement and session propagation only where those runtimes must join. Apply the current language-specific SDK API rather than assuming all SDKs expose the same identify method.
- Inspect alias and person/group property updates for intended lifecycle semantics; do not rewrite historical identity from a code-only hypothesis.

## Marketing attribution

- Trace landing parameters through SPA navigation, OAuth redirects, checkout, and signup. Inspect first-touch versus latest-touch semantics rather than treating any overwrite as a bug.
- Check relevant UTM and ad click identifiers, cross-subdomain identity, consent timing, and cookieless behavior against the intended measurement model.
- Reproduce with synthetic URL parameters and inspect the captured properties. Missing attribution may reflect consent or platform limitations; do not disable those controls to improve measurement.

## Feature flags and replay, when relevant

- For flags: check readiness races, bootstrap consistency, fallback behavior, and exposure events. Code audits do not authorize changing rollout conditions.
- For replay: inspect masking, consent, sampling, and SDK initialization. Do not enable recording or expand captured content just to complete an audit.

## Findings

For each material issue, give the observed behavior, source or query evidence, consequence, and smallest useful correction. Separate confirmed defects from hypotheses and skipped live checks. Use ordinary reports; no wizard-owned ledger or status protocol is required.

For deeper procedures, select `audit-events`, `audit-identify`, `audit-attribution`, `audit-feature-flags`, or `audit-session-replay` using [upstream bundles](upstream-bundles.md).
