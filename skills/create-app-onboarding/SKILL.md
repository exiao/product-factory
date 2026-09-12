---
name: create-app-onboarding
description: Design and implement mobile app onboarding screens, questionnaires, and first-run flows in an existing app. Use for creating or redesigning the flow; use growth for activation diagnosis and conversion experiments.
---

# Create app onboarding

Build a first-run experience that helps a specific person reach a useful outcome in the actual app. Scale the work to the request: a copy edit does not need a new blueprint, and an accepted flow does not need discovery repeated.

## Establish the outcome

Work in the app project. Read its instructions, existing product brief, onboarding plans, relevant screens, localization, navigation, state models, authentication, subscriptions, and permission call sites. Reuse prior decisions from project artifacts and conversation context; verify them against the current implementation. Do not require a particular memory service or write personal memory automatically.

Identify the audience, their current difficulty, the outcome the app can actually deliver, and one core action a newcomer can complete. Treat an unmeasured activation event as a hypothesis. Inspect existing evidence when available; missing analytics should not prevent a requested prototype or build.

Trace fresh launch, returning users, incomplete setup, and completed onboarding into the main app. Check which permissions and account requirements are needed for the first useful action; a manifest declaration alone does not justify an onboarding prompt.

Resolve material unknowns from the code and existing context first. Ask only when a missing product decision changes the direction. Carry forward already authorized implementation without approval at every screen.

## Shape the flow

Describe the promised outcome in the user's language, grounded in real capabilities. Give enough context to understand why any questions matter. Choose screens using [screen patterns](references/screen-patterns.md); these are options, not a fixed sequence or minimum screen count.

For substantial work, keep a concise blueprint in the project's existing planning location, or `docs/onboarding.md` if none exists. Include:

- The person, first useful outcome, known constraints, and unresolved assumptions.
- Each screen's objective, headline, inputs, next action, back/skip behavior, and branches.
- Where each answer changes the product, where value appears, and any account or payment boundary.
- Acceptance criteria and the runtime evidence needed to prove completion and recovery.

Prefer one real core interaction using the app's existing components and data models. Produce a visible result that survives entry into the main app. When real setup requires an external account, upload, or substantial work, consider a clearly labeled sample preview with an honest transition to setup. Choose this based on the task and evidence; do not mandate either a pre-paywall demo or a paywall-first flow.

Ask questions only when their answers affect the experience or another explicit product purpose. Explain that purpose; avoid collecting sensitive information merely for engagement. Use easy-to-answer choices with a way to handle users outside the proposed categories. Mirror answers through useful defaults or results, not repetitive persuasion screens.

## Design and copy

Use the app's native toolkit, existing design system, and real assets. For requested alternatives, show distinct directions before implementing a large redesign. For before/after comparisons, capture or faithfully reproduce current screens and exact localized copy; preserve elements outside the requested change.

Draft the full headline, helper text, options, CTA, validation, and recovery copy together. Make CTAs explain the next action. Use only supported benefit claims and authentic proof. Omit unavailable testimonials and statistics; never invent them. Loading states should represent actual work, and progress should reflect real completed steps along the current branch.

Provide readable text, accessible selection and focus states, screen-reader labels, reachable controls, keyboard-safe layouts, and reduced-motion behavior where relevant. Avoid relying on swipe, color, or animation alone to communicate an action. Keep developer notes outside the product flow.

## Implement and verify

Follow [implementation and runtime checks](references/implementation.md) when building. Reuse existing navigation, persistence, authentication, purchase, and permission integrations. Do not add a paywall, trial, social sharing, or review prompt unless it fits the requested scope and real product configuration.

For measurement, separate screen exposure and completion, onboarding completion, the first useful action, and purchase. Reuse event conventions and avoid recording raw sensitive answers. Use [growth](../growth/SKILL.md) for funnel diagnosis and experiment design; use [posthog-instrumentation](../posthog-instrumentation/SKILL.md) when implementing PostHog events.

Run the app and exercise the affected paths. Use $ios-simulator for iOS runtime inspection when available, or the project's corresponding platform tooling. A browser prototype demonstrates design, not native permission or purchase behavior. Report implemented behavior, observed evidence, and any unverified platform or service boundary separately. Update the project blueprint with decisions and remaining work so another task can resume.
