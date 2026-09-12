# Funnel and activation

## Event map

Write the event sequence before proposing a fix. For each step record who is eligible, the numerator, the denominator, the time window, and the next meaningful action. Useful measures include form start and completion, field errors, first useful action, activation within a defined window, time to activation, onboarding completion, and day 1/7/30 retention. Use the same user or account unit throughout a comparison.

## Signup checks

- Ask only for information needed now; defer optional profile and company fields.
- Keep validation specific and recoverable. Preserve paste, autofill, password-manager behavior, keyboard navigation, and accessible error announcements.
- Make social or passwordless sign-in visible when it suits the audience, but compare downstream quality and activation rather than signup rate alone.
- Make verification status, resend, change-email, and failure recovery understandable.

## Activation

Define a candidate activation event, then compare retained and churned cohorts with the same eligibility and observation window. Correlation is a starting signal, not proof that the event causes retention. Check whether the behavior is a proxy for a more useful outcome.

## Onboarding patterns

Choose among:

- **Product-first:** the core action is simple and an empty state will not confuse users.
- **Guided setup:** configuration is necessary before personalized value is possible.
- **Value-first:** examples or demo data make an otherwise empty product legible.

Keep required steps few, order them by value, offer a clear next action, and let users skip nonessential guidance. Test step order, required versus optional fields, templates, examples, permission timing, and recovery for stalled users. Instrument loading and error states before assuming a copy or motivation problem.

## First-session guidance

Aim for one useful outcome before introducing advanced setup. An empty state should explain what belongs there, show an honest example when helpful, and offer one primary action to create the first real item. Label sample data and provide a path to replace it; viewing a sample is not equivalent to completing the real action.

Use a short, dismissible checklist when several setup dependencies are necessary, ordered by value and prerequisites. Progress must reflect completed work. Offer contextual guidance at the point of need, preserve dismissal for returning users, and do not repeatedly replay tours. Choose questions whose answers change defaults or recommendations; compare their benefit against added effort.

## Stalled users and coordinated recovery

Define stalled behavior using a product-appropriate inactivity window and unfinished meaningful action. Separate technical errors, permission denial, unclear next steps, and lack of motivation. On return, restore progress and link to the next useful action rather than restarting the tour. Offer a simpler path or contextual help based on the blocker.

When lifecycle messaging is in scope, coordinate it with current in-app state: an incomplete-setup reminder should lead to the saved next step, and activation should suppress obsolete setup reminders. Respect preferences and avoid duplicating messages across channels. Treat timing as a hypothesis, not a fixed 24/72-hour schedule. Planning messages does not authorize sending them or contacting users.

## Focused experiment choices

Choose a test from the observed obstacle rather than an exhaustive list:

| Observation | Candidate change | Evidence to compare |
| --- | --- | --- |
| Users reach an empty area and leave | First-item CTA or clearly labeled template | Real first-item creation and time to value, not template views alone |
| A questionnaire delays the core action | Defer unused inputs or use helpful defaults | Activation, result relevance, and later correction effort |
| Users abandon an external setup step | Sample preview or resumable setup | Completed real setup and downstream value, not preview completion alone |
| Returning users repeat work | Persist progress and resume the next action | Recovered activation and errors or duplicate output |
| Users dismiss a tour without acting | Contextual guidance at the relevant control | Core-action success and help requests |

Use the experiment protocol in [experimentation.md](experimentation.md). Separate setup completion from activation and retention; compare stable cohorts by source, platform, and role where relevant. Measure time to value alongside the share who never reach it, so faster times among a shrinking successful subset do not appear as a win. Include loading/error rates, support burden, and later retention or revenue as relevant diagnostics and guardrails. Accessibility and correctness defects should be fixed directly rather than withheld for a conversion test.

## Review

For each proposed change, state the affected cohort, expected behavior, primary metric, guardrails, and what would falsify the diagnosis. Avoid treating numeric step counts, touch-target sizes, email timings, or progress mechanics as universal standards; adapt them to the product, platform, and evidence.
