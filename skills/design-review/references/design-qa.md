# Design QA

Compare a selected visual source with the rendered implementation. Use this mode for faithful recreation or checking design drift, not for inventing a new visual direction. The shared evidence and authorization rules in design-review still apply.

## Establish comparable evidence

Identify and open both the exact source (image, mockup, Figma frame, or live capture) and the implementation. Record their paths or URLs and relevant version/state. A source file or successful build alone does not establish a match. If either side is unavailable, report the comparison as blocked and continue only independently supported checks.

Supplied screenshots support a screenshot comparison; they do not prove live behavior. For a build handoff, capture the current running implementation rather than relying on an older screenshot.

Match route, content, theme, scroll position, interaction state, viewport, crop, scale, and pixel density before judging. Settle loading and animation. Compare app content without browser chrome, surrounding canvas, or device bezels unless the reference includes them as part of the target. Normalize @2x imagery and CSS-pixel captures to comparable dimensions without stretching proportions. Record source/implementation pixel dimensions, CSS viewport and device scale when known; label unknowns and any remaining comparison limitations.

Put source and implementation together in one comparison input, such as a paired image, rather than judging from memory or unrelated image views. Inspect the full composition and paired region crops when text or details are too small to assess. Reuse existing valid Impeccable comparisons instead of generating a duplicate review.

## Check fidelity and behavior

Evaluate these five surfaces explicitly:

- **Typography:** family, weight, size, line height, spacing, wrapping, truncation, and hierarchy.
- **Layout:** proportions, alignment, margins, padding, gaps, radii, elevation, density, and above-the-fold content.
- **Colors:** palette, contrast, opacity, gradients, and semantic state tokens.
- **Assets:** identity, crop, scale, sharpness, transparency, icons, and font/image substitutions.
- **Content:** source wording, labels, data, missing regions, and invented additions.

Distinguish source mismatches from approved deviations, inferred behavior, and shortcomings in the source itself. An inaccessible pattern faithfully copied from the reference remains a usability issue, not a fidelity mismatch. Do not invent source states or claim exact fidelity at breakpoints the source does not show.

When live access and the scope allow it, exercise primary interactions, responsive layouts, focus/keyboard behavior, and relevant loading, empty, error, and selected states. Report runtime checks separately from visual comparison. Screenshots cannot prove backend completion, persistence, accessibility compliance, or interaction correctness.

## Findings and correction

For each finding give priority, location, source versus implementation evidence, user impact, and a concrete correction. Use P0 for blocked core use, P1 for major mismatch/regression, P2 for material drift, and P3 for optional polish. Include precise component/token suggestions when supported by inspected code.

Review-only work stops at findings. For authorized fixes, batch the material corrections, recapture the affected states under the same conditions, and compare again. Reuse the enclosing build's review budget; otherwise use one inspection, one correction batch, and one confirmation pass. Record unresolved issues when that budget ends, rather than converting them into a pass or repeatedly hunting for minor polish.

## Result

Report **passed** only for the checked scope when no actionable P0/P1/P2 mismatches remain. Report **blocked** when required comparison evidence is missing, and **needs fixes** when material mismatches remain. P3 items may be follow-ups. A review can be complete while the design still needs fixes.

Include the source and implementation evidence, comparison conditions, results across all five surfaces, prioritized findings, approved deviations, visible accessibility risks, and untested boundaries including unverified accessibility checks. After fixes, identify earlier findings and the confirming evidence; a fix-only check supports a verdict on those fixes, not a new whole-product pass. Keep the report inline or in the existing project record unless a saved report is requested; no mandatory filename or deployment step.
