# Render verification mechanics

Persist accepted changes to source and recheck after reload. Temporary browser-side styling is exploration, not a saved implementation.

Use these checks within design-eval’s shared evaluation and confirmation pass. Use realistic long and populated content so overflow and wrapping are visible.

When alignment is disputed, use computed geometry such as `getBoundingClientRect()` and treat the numbers as ground truth; screenshots and vision judgments are supplementary. Verify no horizontal overflow, clipped overlays, missing focus, or incorrect touch targets. Apply relevant project and accessibility requirements rather than treating an arbitrary target size as universal.

For server-rendered pages, extract inline scripts and run `node --check` before trusting an interactive screenshot. Data attributes plus event delegation are safer than nesting quotes across a server template, JavaScript string, and HTML attribute. For client-side sorting/filtering, assert the resulting row order after a real click, not merely that headers look clickable.

If a capture is blank, stale, or taken before the state settled, recapture it before judging the implementation.

## SVG delivery

For SVG deliverables, use a viewBox and responsive sizing, avoid duplicate IDs in reused definitions, and inspect labels and marks at their actual display sizes. Verify embedded and standalone exports separately: exports may need explicit styles and assets supplied by page inheritance. Give informative diagrams an accessible name and useful text explanation.
