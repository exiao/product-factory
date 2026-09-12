---
name: frontend-design
description: Design and implement polished, functional web pages and components with a coherent visual direction. Use for frontend builds, landing pages, and interactive prototypes; preserve existing product systems and scope for bounded edits.
license: Apache-2.0. See LICENSE.txt and NOTICE.md.
---

# Frontend design

Build the requested working interface with deliberate hierarchy, typography, color, spacing, and interaction. Choose a direction that serves the product and its reader; novelty alone is not a design objective.

## Establish the context

Reuse the user's brief, repository instructions, PROJECT_BRIEF.md, PRODUCT.md, design documents, existing components, and supplied references. Separate explicit product intent from assumptions inferred from implementation. Ask only when missing audience, purpose, or brand direction would materially change the result. For a bounded edit, preserve its surrounding system and proceed with reasonable assumptions.

For an existing product, extend its tokens, assets, components, and interaction conventions. A faithful implementation request takes precedence over inventing a new aesthetic. New work benefits from one clear direction and an identifiable hierarchy, rather than arbitrary styling on each section.

## Implement with purpose

- Make content and intended actions drive the layout. Group related information and vary separation between groups. Use cards, modals, grids, and centered layouts when they express useful structure, not as an automatic template.
- Choose typography for reading, hierarchy, and brand fit. Preserve licensed fonts and sensible fallbacks; system fonts can be the correct choice. Use responsive sizing without making zoom or narrow layouts unusable.
- Derive colors and spacing from the chosen system. Make states distinguishable beyond color alone. Avoid ornamental charts, empty metric panels, and decoration that competes with the main task.
- Implement real navigation and state transitions within the requested scope. Provide relevant loading, empty, error, success, disabled, and focus states. Label prototype data and simulated behavior rather than implying a connected backend.
- Use semantic controls, keyboard access, visible focus, appropriate labels, responsive layouts, and reduced-motion support. Do not hide critical functionality on small screens or put necessary controls exclusively behind hover.
- Add motion when it clarifies state or supports the chosen experience. Keep essential content usable if animation or JavaScript fails; a reveal class appearing in the DOM does not establish that the content is visible.
- Fit implementation complexity to the task. Reuse the repository's framework and components; do not introduce dependencies or rewrite a whole file merely to add visual polish.

Read [interface craft](references/interface-craft.md) when implementation needs detailed typography, layout, color, interaction, or responsive guidance. For stakeholder pages, product concepts, or embedded SVG, read [prototypes and visual evidence](references/prototypes-and-evidence.md).

## Iterate and verify

Prefer editing the local source and reviewing the running result. Temporary browser-side styling can help explore an isolated preview, but it is not a saved implementation. Do not assume arbitrary JavaScript against a production page is harmless or authorized. Persist accepted changes to the actual source and recheck after reload.

Inspect the rendered page at relevant widths and exercise the principal interaction, keyboard path, and failure/empty states when applicable. Check text clipping, overflow, font loading, media, contrast, and whether controls perform their advertised action. Use repository-required checks and focused validation proportional to the change. Distinguish a passing build from visual verification, and report inspection limits honestly.

Deliver the working artifact or code, its location, the meaningful design choices, and what was verified. Publishing is governed by the requested scope and available deployment workflow; a frontend build does not automatically authorize a public deployment.

## Related workflows

Use [$impeccable](../impeccable/SKILL.md) for a broader interface design or improvement workflow, [$design-mode](../design-mode/SKILL.md) for alternative design artifacts, [$ui-lint](../ui-lint/SKILL.md) for a formal critique or focused implementation polish. Do not load all of them as prerequisites. This skill's default deliverable is the requested frontend implementation.
