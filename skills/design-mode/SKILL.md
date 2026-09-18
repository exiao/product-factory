---
name: design-mode
description: "Apply Eric’s personal design preferences alongside the selected frontend design workflow. Use for frontend creation, refinement, and review, including requested prototypes, variant canvases, HTML decks, and motion studies; preserve established design systems and requested formats."
---

# Design preferences and artifacts

## Shared quality contract

Read [$design-eval](../design-eval/SKILL.md) when applying this skill and run its evaluate → fix → recheck pass before delivering a created or revised interface. It owns removal, content necessity, disclosure, review routing, and final rendered verification; share one review budget across the workflow. For an assessment-only request, use its review-only behavior.

For prototypes, center each direction on one core loop: starting material → product contribution → useful result → accept or revise. Requested alternatives can each test a focused loop; do not merge their capabilities into one prototype. Reuse a settled loop rather than creating another discovery or approval step.

## Still-image generation

For generated or edited still images, use [$image-generation-guide](../image-generation-guide/SKILL.md): Codex built-in image generation, verified files saved in the local project. This applies to reference sheets and intermediate assets as well as final images. Keep this skill's creative requirements; do not automatically use provider CLIs, external generation plugins, or remote rendering services. An explicit user request for another provider takes precedence.

Apply the preferences below to the requested production UI or reviewable artifact. Artifact-specific packaging and controls apply only when the user needs an artifact; ordinary frontend work stays in the application. Determine the audience, format, fidelity, constraints, and unresolved choices from existing context. Ask only for missing decisions that materially affect the result; do not require a questionnaire, UI-kit upload, or option count for every task.

Inspect the current source, supplied screenshots, design files, tokens, and relevant assets. Existing visual evidence matters even without a DESIGN.md. Use the project’s existing design system and [$impeccable](../impeccable/SKILL.md) for its frontend design workflow and commands. Keep Impeccable unmodified: this skill owns personal preferences and local references, while Impeccable owns its upstream workflow and tooling. Use its public skill entrypoint rather than depending on internal reference paths. Apply these personal defaults within the requested scope; explicit briefs and established systems win. Combine overlapping steps into one workflow, including one shared review budget. Preserve the brief and established product behavior; a small change does not authorize a redesign.

## Product context handoff

When arriving from Software Factory, reuse its accepted vision, person and job, mechanism, constraints, evidence and explicit or delegated decisions. Use [$impeccable](../impeccable/SKILL.md)'s context setup once per session, reusing a completed setup, and follow its init record-writing format, including its schema marker and platform value. Create or update the resolved PRODUCT.md from accepted facts before visual work, preserving confirmed content and linking the original criteria and evidence. Keep visual decisions in DESIGN.md and decision history in the existing project record; link PRODUCT.md there instead of duplicating its facts.

For this handoff, existing explicit answers and approvals satisfy product-truth confirmation; this reuse rule takes precedence over requiring a new init interview merely because PRODUCT.md is missing. Ask only about consequential gaps or contradictions that remain unresolved. Product approval does not settle an unanswered platform, stack or design-workflow choice. Keep assumptions and open questions labeled; a file's existence does not turn an inference into an approval. Preserve Impeccable's upstream files, record format and scope limits on drift repair. Resume its applicable design workflow once the record is ready.

## Design and artifact checks

Apply these creation preferences alongside the shared quality contract:

- For an open brief, explore structurally different concepts briefly, then turn the user's taste and reactions into a concrete direction. A fixed brief or narrow change proceeds directly.
- For new concepts and substantial redesigns, compare the proposed experience with how the person gets the job done today, including workarounds or doing nothing. State the meaningful advantage and the evidence or assumption behind it; visual novelty alone does not establish a better solution. Reuse existing research and settled decisions rather than reopening discovery for a narrow fix.
- For new designs or substantial redesigns, explicitly assess whether custom imagery strengthens the chosen direction. When it does, use [$image-generation-guide](../image-generation-guide/SKILL.md) to generate and integrate the asset; do not stop at a recommendation, placeholder, or generic gradient/shape substitute. Brief composition, palette, crop, and text placement, then inspect the integrated result at desktop/mobile or relevant target sizes. Preserve supplied brand assets and use existing imagery, code, or vectors when they better serve the task. See [image asset workflow](references/creative-exploration.md#image-assets) for exploration, production, and verification.
- When feedback rejects the underlying benefit or idea, distinguish concept weakness from usability and appearance before editing. Return to the mechanism comparison in [$software-factory](../software-factory/SKILL.md), reusing the agreed problem; a successful click path or cleaner sketch does not establish useful assistance. When output quality is disputed, inspect or produce the relevant result sample before further UI investment. Keep ordinary visual fixes scoped to the interface.
- Prefer assistance attached to the object being worked on: select a phrase, inspect an inline alternative, keep or undo it. Add a separate widget, panel, or screen only when the task needs that separation. Make a usable result look ready to use; do not present it as an unfinished form by default.
- Prefer a meaningful image, pattern, or solid background when a generic gradient adds nothing.
- Build hierarchy with placement, spacing, and typography before adding copy. Default to no decorative eyebrows (small labels above headings), redundant subtitles, section introductions, or helper sentences that repeat a heading or control. Do not fill whitespace or manufacture a visual hierarchy with extra words. An eyebrow is useful when it conveys distinct context, such as a publication section or an object's category, that the surrounding interface does not already establish. Explicit briefs and established systems take precedence.
- Match the surface to its purpose. Put the task or content first in apps, tools, visualizations, and motion studies; do not wrap them in a hero, slogan, or promotional sections unless requested. Marketing and editorial surfaces can use those elements when they serve the intended message. Apply design-eval's content-necessity test while composing, not only after rendering; preserve functional labels, accessible names, and necessary guidance.
- For a new type system, start with 1–2 font families and 2–4 text styles; use accents and italics sparingly. Existing product typography, useful labels, and functional boundaries take precedence over these defaults.

For optional exploration techniques, read [creative exploration](references/creative-exploration.md).

For custom text geometry, such as prose flowing around moving shapes or measured canvas typography, read [Pretext](references/pretext.md). Use it only when the requested behavior needs text measurement before rendering; prefer ordinary HTML/CSS otherwise.

For brand-inspired styling, use user-provided references and preserve the established design system.

For dashboards, navigation changes, charts, layout choices, or component specifications, read the applicable section of [review playbooks](references/review-playbooks.md).

For a reviewable artifact, choose the format around the decision:

- Static visual alternatives can share a labeled comparison canvas.
- Interaction or flow questions need a clickable prototype with realistic states.
- HTML decks and motion studies need navigation or playback controls.
- Requested PPTX, PDF, Figma, or other native deliverables use the available format-specific workflow; do not silently substitute HTML.

When an accepted storyboard or scenario leaves the flow, state model, or recovery behavior unresolved, read and use [$interaction-design](../interaction-design/SKILL.md) before high-fidelity visual work. It owns the behavior decisions, wireflow, and interaction brief; design-mode owns prototype rendering and visual craft. If interaction-design is already active or its handoff settles the current scope, continue from that work without routing back, repeating discovery, or adding an approval checkpoint. Visual-only work and settled interactions proceed directly.

For low-fidelity flow work, use a clickable structural prototype for the unresolved behavior. Always use [WiredJS / Wired Elements](https://wiredjs.com) for low-fidelity UI mockups and prototypes, giving them a sketchy, hand-drawn, Balsamiq-like appearance. Use actual Wired components for the relevant controls and containers; plain grayscale styling alone does not satisfy this requirement. Keep the visual treatment deliberately rough while preserving working interactions. Reuse a settled prior low-fi artifact and revise only the unresolved portions. Make the path coherent with realistic content and relevant entry, success, empty, loading, invalid, permission, failure, and recovery states. Skip low-fi for a small contained fix or an already approved high-fidelity direction.

Reuse the current project's stack and components; do not add dependencies or rewrite whole files solely for visual polish. The required WiredJS dependency for low-fidelity prototypes is an exception; keep it scoped to the prototype. Use a simple portable format when a standalone artifact calls for it. Copy only required assets when packaging a standalone artifact. Preserve significant prior versions; keep alternatives in one artifact when side-by-side comparison or toggles help. A single requested direction does not need three extra variants. Make prototype controls change coherent state and keep shared data consistent across views.

For artifacts, use standard in-page controls for requested variants. There is no assumed host Tweaks protocol, automatic model API, slide-notes bridge, or file-rewrite service. Read [references/artifact-patterns.md](references/artifact-patterns.md) for variant state, slide geometry, and artifact-specific checks.

Before handoff, complete [$design-eval](../design-eval/SKILL.md) on the final saved artifact.

For supplied design handoff archives, read [references/handoff-bundles.md](references/handoff-bundles.md). Present the actual artifact path in the app when supported. Local creation does not imply publishing; use an authorized deployment workflow only when sharing or hosting is requested. Be clear about prototype versus production behavior.
