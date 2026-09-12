# Destinations and optimization objectives

## Destination checks

Resolve the exact destination from the live ad creative. Check the final URL, redirect chain, response status, rendered content, tracking parameters, platform app-link behavior, and any login or consent wall. A URL that resolves in a command-line probe may still fail in an in-app browser or crawler. A prelander that infers channel from a missing parameter can misattribute paid traffic.

Treat a canary as a probe with its own dependencies. Connection refusal, repeated timeouts, and relevant 5xx responses support an outage finding. Model-auth fallback, telemetry errors, stale windows, or other probe-side warnings do not prove the user destination is down. Corroborate with recent real inbound visits and successful downstream replies.

## Messaging funnels

A normal traffic/link objective pointed at a messaging URL buys clicks, not conversations. For click-to-message campaigns, verify the provider’s native messaging objective, destination type, CTA, page/account linkage, and event definition. Count arrivals, first messages, and engaged conversations in the product system; CPC is only a proxy. Distinct prefill or ice-breaker text can provide a join key, but generic fallbacks weaken attribution.

## Optimization-event mismatch

Compare the ad set’s configured conversion event with the events actually emitted by the pixel, SDK, app, or server. If the desired event is immutable after publish, the safe recommendation may be a new paused test object rather than an in-place edit; verify current provider rules. Do not change an objective because a report is empty until you have proven whether the event was never emitted, was received but unmatched, or was simply outside the selected attribution window.
