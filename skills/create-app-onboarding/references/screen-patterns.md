# Screen patterns

Select the smallest set that supports the requested outcome. No archetype is universally required.

| Pattern | When useful | Decision constraint |
| --- | --- | --- |
| Welcome or outcome preview | The app's purpose is not immediately apparent | Show a real capability and a clear next action; keep returning-user entry accessible. |
| Goal or preference question | Answers change recommendations, defaults, or setup | Map each answer to an actual consumer in the app; defer unused questions. |
| Obstacle question | A blocker changes the help or path offered | Offer relevant help rather than amplifying distress. |
| Personalized explanation | The connection between choices and the next action is unclear | Explain the actual adaptation without overstating what was computed. |
| Social proof | Authentic, relevant evidence reduces uncertainty | Use attributable approved content; omit it when unavailable. |
| Core interaction | A small action can deliver meaningful value | Reuse product behavior and create a result the user can keep; do not require a shareable output. |
| Sample preview | Real setup needs an integration or effort that cannot happen immediately | Label sample data and explain how to replace it; do not count viewing a sample as real activation. |
| Permission explanation | The next action needs device access and the benefit is unclear | Request access in context, explain why, and provide denial/defer behavior appropriate to the feature. |
| Result and next action | The user has completed a useful action | Carry the result into the app and make the next step obvious. Sharing is optional and user initiated. |
| Account creation | Identity is needed for an explicit capability such as sync | Explain the requirement before effort or data would otherwise be lost; preserve guest work through sign-in. |
| Existing paywall | The product's paid access model calls for it | Show real price, billing interval, eligibility, and access terms from the existing integration. Preserve applicable restore and dismissal paths. |

Questionnaire flows need context before questions. A simple utility may open directly into the core action with a useful empty state. A subscription app may benefit from personalized setup and a concrete value preview, but length and payment placement remain product decisions or testable hypotheses.

If progress is shown for branching flows, use the actual selected path or honest stage labels instead of a misleading fixed percentage. Allow users to revise selections without losing unrelated work. Avoid fake processing delays and surprise locks on work already created.

Permission behavior and purchase/review policies depend on platform and SDK version. Verify current official documentation when implementing those integrations. Do not assume all permissions have identical prompting or retry rules, or introduce blanket priming screens solely because a permission appears in configuration.
