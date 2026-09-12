# Hypothesis → live observation → validation

For visual study delivery, use [persona screenshot annotations](screenshot-annotations.md): preserve the action/evidence record below, and anchor synthetic reactions to the actual captured states.

Use a synthetic panel to propose possible failure mechanisms, then inspect the real product when live verification is requested or needed for an objective claim. A reproduction strengthens a claim about interface behavior; it does not verify the persona's emotions, the prevalence of a problem, or its causal effect on conversion.

## Procedure

1. Ground the hypothesis in exact supplied or rendered copy and the preceding task. Distinguish a proposed mockup from a shipped flow. Name the expected behavior and the suspected failure.
2. Identify what observation would support or contradict the hypothesis. Consider another explanation before reproducing; do not seek only confirming screenshots.
3. Reach the relevant state on the authorized surface. Record prerequisites, action, actual response, and recovery behavior with tool output or screenshots. Verify only the surfaces relevant to the request; a second client is useful for cross-platform claims, not a universal requirement.
4. Classify the result: reproduced objective defect, observed behavior with uncertain user impact, contradicted hypothesis, or unverified due to missing access/evidence.
5. If funnel evidence is accessible, check event meanings, cohorts, time window, and denominators. A drop at a gate may be consistent with several causes. Report the association without claiming the panel identified its cause.
6. Recommend the next check appropriate to the remaining uncertainty: runtime reproduction, human usability observation, language review, or a suitably designed experiment. State what result would change the recommendation.

## Live surfaces

Follow the active browser tool's documented entrypoint and methods, as described in [embodied-persona-live-browser.md](embodied-persona-live-browser.md). Never assume accessibility indexes, DOM evaluation, or screenshot methods from a previous runtime.

Use a local server, simulator, or connected app only when exposed and authorized. Inspect the project's actual instructions before building or launching. Do not install dependencies, deploy a page, create accounts, or transmit personal data as an implicit extension of a synthetic panel. If a build or account is unavailable, deliver the offline work and name the missing live evidence.

For long pages, disambiguate repeated controls from current context. Use supported scrolling, fresh state, and screenshots. If content cannot be reached or inspected, mark it unobserved rather than absent.

## Assess potentially manipulative interactions in context

Separate a visible pattern from a conclusion about deception or harm. Inspect the user's goal, clarity of material terms, informed choice, ability to decline, and the actual consequence of each option. Do not use a single visual or timing threshold as a verdict.

- **Decline and cancellation:** inspect wording, visibility, discoverability, operability, and whether the alternative is realistically available. Visual hierarchy alone does not establish fairness or manipulation. Use the applicable current accessibility guidance for measured compliance claims.
- **Urgency and scarcity:** verify the underlying expiration or inventory behavior before alleging it is fake. A screenshot of a timer alone cannot establish deception.
- **Rewards and discounts:** check whether eligibility and comparison prices support the claim, and whether recurring terms are clear. Post-value timing does not automatically make an offer honest.
- **Pricing and renewal:** inspect what is billed, when, how recurring charges are disclosed, and what cancellation entails. Distinguish visible ambiguity from a verified mismatch.
- **Loading feedback:** inspect actual state and timing before alleging fabricated work. A minimum display time may avoid flicker; cached and cold responses alone do not prove intent. Check whether the feedback misrepresents progress or prevents useful action.

Use precise descriptions of observed behavior and user consequence. Reserve definitive claims for the evidence obtained; otherwise propose a check.

## Delivery

Keep separate: synthetic predictions, live observations, external/customer evidence, and remaining inferences. For example: "The button opened a paywall before account connection. Simulated personas expected connection instead; whether intended users share that expectation remains untested." Never state that live reproduction confirmed a psychological mechanism unless appropriate human evidence actually supports it.
