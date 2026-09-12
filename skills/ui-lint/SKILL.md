---
name: ui-lint
description: Review UI code with named rules, assess product UX with a structured design review or heuristic scorecard, and implement focused interface polish. Use for UI code reviews, formal design critiques, and making an existing interface feel better; not broad product redesign.
license: MIT
---

# UI review and polish

Choose the depth from the request. For a formal design review, UX assessment, or heuristic scorecard, read [design-review.md](references/design-review.md) and inspect the real feature or journey. A code review or polish request uses only applicable code rules; do not impose a full scorecard on it. A narrow UX question can use the relevant portion of the design framework.

When source is available, inspect the relevant component, styles, design tokens, interaction states, and dependencies. Read [rule-selection.md](references/rule-selection.md) for code-rule routing, then use the matching definitions in [selected-rules.md](references/selected-rules.md). Source access is not required for an observed product review.

For implementation patterns, load [selected code examples](references/selected-examples.md) after choosing rules. It contains a small set of correct/incorrect examples for measured containers, exit cleanup, hover/touch access, card overlays, and refresh-safe focus.

For code findings, include file/line, rule ID, observed code, user impact, and a minimal fix. For product findings, cite the observed screen or journey step and supporting evidence; do not invent source locations or infer hidden behavior. Distinguish definite violations from visual recommendations and mark untested behavior. An assessment-only request ends with findings.

For a request to improve or polish the interface, implement the applicable fixes while preserving behavior, product identity, and existing design tokens. Prioritize demonstrated interaction and accessibility problems, then motion, typography, spacing, and surfaces. Do not turn optional wrapping, shadow, radius, or smoothing preferences into mandatory changes. Remove visual clutter only when it adds no useful hierarchy or meaning; preserve labels, click targets, and accessibility. Product redesign, publishing, and deployment require their own scope.

Do not infer a violation from a screenshot when computed style, event behavior, or touch/keyboard state is needed. Use the repository's available browser or test tooling to verify affected behavior. For polish changes, report the exact component/state changed and the viewport or input mode checked; cover relevant responsive, keyboard, touch, and reduced-motion states. Do not require a specific animation library or install one globally.
