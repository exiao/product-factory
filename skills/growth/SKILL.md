---
name: growth
description: Improve signup, activation, onboarding, paywall, retention, referrals, and product experiments using measured funnel evidence. Use for in-product conversion and lifecycle questions; use content-strategy for distribution and pricing for packaging or price-setting.
---

# Growth

Use this skill for in-product growth work: finding funnel loss, defining activation, improving onboarding, presenting upgrades responsibly, reducing voluntary or involuntary churn, and designing experiments. It is a decision and implementation-planning aid; it does not authorize publishing, outreach, paid acquisition, pricing changes, or production rollout.

Reuse existing product briefs, marketing context, and prior funnel decisions before asking questions. Start with the product, audience, funnel stage, current evidence, constraints, and desired outcome. Read only the focused reference needed:

- [funnel-and-activation.md](references/funnel-and-activation.md) for signup and onboarding.
- [paywall-retention.md](references/paywall-retention.md) for upgrades, trials, cancellation, and payment recovery.
- [experimentation.md](references/experimentation.md) for hypotheses, randomization, denominators, power, and results.
- [cohort-analysis.md](references/cohort-analysis.md) for cohort cuts and causal checks.

## Workflow

1. State the decision: where should users reach value, what behavior should change, and for whom?
2. Map the current path and define each event and denominator. Separate exposure, attempt, completion, activation, retention, and revenue.
3. Check instrumentation and data quality before interpreting a rate. Record the window, eligibility rules, exclusions, and cohort start.
4. Identify the largest evidence-backed loss or user obstacle. Do not optimize a downstream step when upstream traffic or tracking is the limiting uncertainty.
5. Propose the smallest reversible change or experiment. Include primary metric, secondary diagnostics, guardrails, segment plan, and a stop or rollback condition.
6. Report what the data shows, what remains uncertain, and the next evidence step. Label hypotheses as hypotheses.

## Signup

Reduce information and effort required before the first useful action, while retaining fields that are necessary for security, delivery, compliance, or personalization. Consider value before commitment, clear expectations, useful defaults, inline errors, password managers, paste, autofill, and accessible mobile controls. Offer authentication methods appropriate to the audience; do not assume one provider is best.

Compare single and multi-step flows by completion, error rate, time, and downstream activation. A shorter form is not automatically better if it creates bad leads or prevents the product from delivering value. Preserve an understandable confirmation and recovery path for verification or failed submission.

## Activation and onboarding

Define activation as a product-specific behavior that is plausibly connected to retained value, then verify the relationship in a dated cohort rather than declaring an aha moment by intuition. Get users to one meaningful outcome quickly. Prefer doing over explaining, useful empty states over dead ends, and short dismissible guidance over tours that trap users.

For stalled users, distinguish missing motivation, unclear next action, poor performance, permission friction, and an actual product defect. Compare onboarding completion and time-to-value by entry point, device, platform, role, and other relevant cohorts before changing copy or sequence. Do not use progress, streaks, social comparison, or urgency when they pressure users or misrepresent progress.

For creating or redesigning mobile onboarding screens and implementing their flow, use [create-app-onboarding](../create-app-onboarding/SKILL.md). Keep activation diagnosis, funnel measurement, and conversion experiments here; consult both when evidence leads to a flow redesign.

## Upgrade and retention

Show upgrade value in context after a user understands the product, explain limits honestly, and provide a clear way to continue or decline. Treat trials, paywalls, discounts, and reminders as experiments with trust and long-term retention guardrails. Never hide material terms, make cancellation difficult, or use false scarcity.

For cancellation, learn the reason with a short optional question, offer a relevant reversible alternative such as pause or downgrade when it genuinely helps, and honor a direct cancellation. For payment failures, distinguish temporary, permanent, and authentication-required failures; communicate status accurately and provide a recovery path. Analyze voluntary and involuntary churn separately. Use [paywall-retention.md](references/paywall-retention.md) for the detailed structures.

## Experiment output

For an audit, report **Issue → Evidence → Likely impact → Proposed fix → Priority → Validation**. For a test, use the hypothesis form in [experimentation.md](references/experimentation.md). A result must be one of **WIN**, **FAIL**, or **INCONCLUSIVE**; FAIL means the predeclared rule establishes an adverse primary outcome or material guardrail failure, even when a secondary metric improved; a noisy negative estimate or broken instrumentation is inconclusive. Do not call a result a win from an unplanned segment or a peeked early difference.

Use [$content-strategy](../content-strategy/SKILL.md) for audience, channel, editorial, and distribution planning; [$copywriting](../copywriting/SKILL.md) or [$hooks](../hooks/SKILL.md) for asset writing; [$pricing](../pricing/SKILL.md) for packaging and price-setting; [$idea-validation](../idea-validation/SKILL.md) for buyer, pitch, price hypothesis, and demand tests. Keep this skill focused on the product funnel and lifecycle after users encounter the product.

For customer referral or affiliate program design and diagnosis, read [referral programs](references/referral-programs.md): value triggers, incentives, funnel events, contribution economics, and reward integrity.
