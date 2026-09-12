# Implementation and runtime checks

## Trace the existing contract

Locate the launch routing decision, onboarding completion flag, draft answers, result model, authentication transition, and entry into the main app. Extend existing state patterns rather than creating a second independent onboarding state store. Decide whether state belongs to the device, guest, or account using current app semantics.

Persist enough progress to recover from app interruption. Write final completion only after the required result or setup is saved successfully. Keep back navigation and revised answers consistent with dependent selections. Preserve draft work through sign-in and avoid recreating duplicate results on retries. Avoid forcing completed users through a new flow on upgrade unless that migration is intended.

Use real components for the core interaction. A preview with sample data should remain distinguishable from a saved user result. Carry real output into the main app rather than discarding it at the last screen.

Reuse configured subscription products and entitlement handling. An unfinished or simulated purchase must not grant entitlement or appear as a successful live purchase. If the user requested only a prototype, label simulated payment behavior and keep it out of production paths.

## Evidence proportional to the change

Run the relevant build and project checks. Then exercise the affected runtime paths; select applicable cases rather than imposing a full matrix on a text edit:

- Fresh state: onboarding opens, the core action produces a result, and completion reaches the correct main screen with that result preserved.
- Return state: closing and reopening midway resumes coherently; reopening after completion bypasses onboarding as intended.
- Navigation: back, skip, changed answers, repeated taps, and branches do not lose unrelated data or create duplicates.
- Failure: denied permission, canceled sign-in or purchase, loading failure, and network retry have an understandable route forward without false completion or access.
- Existing users: returning accounts, existing entitlements, and applicable restore flows follow current product rules.
- Presentation: inspect representative small screens, larger text, keyboard overlap, screen-reader order, and reduced motion for the changed UI.
- Measurement: when instrumentation changes, observe events and properties for the actual path; distinguish screen views, completion, activation, and purchase without leaking sensitive input.

Record screenshots or concise runtime logs for material behavior. State the platform and test environment, including whether purchase behavior was exercised in a sandbox. A successful build, prototype, or analytics event does not independently prove native permissions, production billing, or retention improvement.
