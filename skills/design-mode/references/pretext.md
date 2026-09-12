# Pretext: custom text geometry

Use [@chenglou/pretext](https://github.com/chenglou/pretext) when a requested interaction needs line breaks or text dimensions before rendering: prose flowing around moving shapes, canvas typography, word-based games, or measured wrapping for virtualized layouts. Prefer normal HTML/CSS for ordinary pages, forms, articles, and static wrapping. Do not add Pretext merely to decorate an interface.

Pretext computes layout; the application draws it. Keep design-mode and Impeccable responsible for visual direction, accessibility, and verification. Follow the project palette and typography rather than imposing a dark demo aesthetic.

## Implementation notes

- Check the library documentation for the chosen version and pin it. The local demo used `@chenglou/pretext@0.0.6`; this is a tested reference version, not a claim that it is current.
- Prepare text once per text/font configuration; reuse the prepared result while geometry changes. Match measurement fonts to rendered fonts and wait for custom fonts before measuring.
- Use `prepare` / `layout` for dimensions, or `prepareWithSegments` / `layoutNextLineRange` / `materializeLineRange` for variable-width rows. Verify signatures against the selected version.
- For obstacles, reserve space for the entire glyph row, including ascenders, descenders, and a gap. Preserve left-to-right reading order across split lanes. Skip lanes too narrow for readable text; constrain obstacle size and position on resize.
- Preserve semantic text when drawing to canvas. Supply accessible controls and keyboard alternatives for dragging; respect reduced motion and make playback labels reflect actual behavior.
- Verify the real browser at narrow and wide widths, including dragging, size extremes, font loading, text clearance, and pause/resume. Use the existing design-mode verification workflow.
