# Attribution and conversion diagnostic ladder

The platform distinguishes an event being **sent**, **received by a dataset**, and **attributed to an ad**. A green send log or a healthy pixel does not prove ROAS. Use this ladder where the platform exposes these stages; privacy-preserving or aggregate attribution may not expose user-level click matching. Missing access is not evidence of failure:

| Layer | Evidence | If absent |
|---|---|---|
| Click captured | click ID or visitor row in the product system | landing/capture path issue |
| User/install matched | attribution row and match-method distribution | capture, consent, matching, release, or measurement limitation |
| Postback processed | terminal postback row and handler branch log | handler gate, event map, or runtime issue |
| Dataset event received | provider event stats or test event | transmission/schema/credentials issue |
| Attributed to spend | provider insights with action/value | attribution window, matching, or objective issue |

Confirm that every metric is instrumented before interpreting its gap. For example, a landing-page-view metric requires the relevant browser emitter; without it, clicks versus views is missing instrumentation rather than a measured drop-off. An empty terminal table needs an instrumentation, retention, environment, and expected-volume check before being classified as a defect.

## Silent-success traps

A webhook returning HTTP 200 can have exited through an ignored event type, non-production filter, missing attribution, or early return. Inspect the handler’s own accepted/rejected branch logs and terminal table, not only provider delivery status. A deployed fix is not proof; verify a new terminal row and its event payload.

Check whether code merged actually shipped to the client. A missing SDK or an app-store/OTA release gap cannot be fixed by server-side mapping alone. Keep deterministic and probabilistic match methods separate and report their distribution.

## Metric integrity

Label bidding metrics separately from all-event reporting metrics. A goal-scoped conversions/value column can be zero while a shadow/all-conversions column contains events; query the conversion-action or event segment before declaring revenue absent. Confirm that the configured optimization event fires in the same campaign or ad set. A campaign name is not evidence of its objective.

When several channels share a landing route, join click IDs with source/medium and inspect defaults. Paid clicks can be filed under an organic or bot channel even when every upstream system appears healthy.
