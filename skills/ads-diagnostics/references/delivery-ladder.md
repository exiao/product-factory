# Delivery diagnostic ladder

Walk in order and stop at the first confirmed blocker. Inspect the channels included in the task using each provider’s current API schema and status vocabulary.

## Account and policy

- Account disabled, billing/security hold, spend cap reached, or account-level review block can leave campaigns appearing active while delivery is effectively stopped.
- In regulated categories, check policy and verification before bidding or budget. A limited approval can permit some delivery while imposing a ceiling; it is different from no delivery.
- Inspect campaign and ad review status, policy reasons, and removed/tombstone rows. Do not infer a rejection reason from a generic status.

## Delivery versus budget

Compare authorized budget with actual spend and active-ad count. A budget can be healthy in total while being diluted across too many ads. Use lifetime impressions summed at the ad-set level plus age of the ads; per-ad recent impressions alone cannot distinguish a new ramp from a set that never entered an auction. Calibrate any delivery floor from the current platform/account evidence rather than copying a fixed threshold from another account.

- **Spend equals the cap**: investigate budget or account cap.
- **Spend far below budget with no auction-share evidence**: investigate bid target, demand, policy, or objective eligibility.
- **Active ads with negligible lifetime delivery**: delivery-dead or review/configuration issue; do not score creative that was never served.
- **Some delivery but thin distribution**: budget dilution, narrow targeting, placement/device mix, or learning state.

## Objective and bidding

Confirm optimization goal, promoted object, destination type, bidding strategy, target CPA/ROAS, and the conversion actions actually included in the goal. A link to a messaging app is not automatically a conversation-optimized ad. A target based on zero or corrupted value can throttle delivery; lowering it does not repair missing instrumentation. Separate a delivery dial that may unblock auctions from a profit target that claims economic success.

## Review and destination

Read the exact policy or destination error. A shared URL rejected across different ads points to destination or crawler behavior; a single creative rejection may be asset-specific. A redirect, HTTP success, or synthetic canary is not proof that the promised destination works for real users. Classify canary failures by reason and compare with live inbound traffic before recommending a pause.

## Reporting rule

Do not generate more creative for a surface that cannot serve it. Report the allocation/configuration problem, the evidence, and the smallest reversible correction. A zero-kill or empty-performance report can be a successful diagnosis when the ads never received an opportunity to produce data.
