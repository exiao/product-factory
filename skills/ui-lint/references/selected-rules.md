# Selected rule definitions

These compact definitions are the minimum evidence standard for the IDs in `rule-selection.md`.

## Timing and motion

- `duration-max-300ms`: user-initiated feedback should usually complete within about 300ms. Treat this as a usability heuristic; longer transitions can be valid for large spatial travel or an intentional staged sequence.
- `duration-press-hover`: press and hover feedback is commonly about 120–180ms. Check that it responds quickly and consistently; do not fail a different value without evidence of sluggishness or inconsistency.
- `spring-for-interruptible`: use a spring or an equivalent retargetable interpolation when a gesture can reverse mid-flight. A CSS transition is sufficient when it retargets correctly.
- `easing-entrance-ease-out` / `easing-exit-ease-in`: ease-out generally suits arrivals and ease-in generally suits departures. These are recommendations for natural motion, not universal defects.
- `none-keyboard-navigation`: do not animate routine keyboard focus movement or high-frequency navigation in a way that delays the user's next action; preserve a clear focus indicator.
- `none-context-menu-entrance`: context menus should appear promptly when invoked; reserve motion for a brief exit if it does not delay dismissal or obscure the user's target.
- `staging-one-focal-point`: avoid competing simultaneous emphasis animations. Apply this when multiple animations impair hierarchy, not merely because several elements move.

## Lifecycle and lists

- `exit-requires-wrapper`, `exit-prop-required`, `presence-hook-in-child`, `mode-pop-layout-for-lists`, and `nested-propagate-required` are Motion/AnimatePresence-specific checks. Report them only when that API is present; otherwise state the framework-neutral requirement: mounted elements need a reliable exit lifecycle, stable layout behavior, and cleanup.
- `exit-key-required`: dynamic animated lists need stable unique identity keys, never array indexes when reordering/removing items can occur.
- `presence-disable-interactions`: an element leaving the UI must not remain an active click or keyboard target during its exit interval.

## Touch, accessibility, and sound

- `ux-fitts-target-size` / `ux-fitts-hit-area`: provide a sufficiently large, non-overlapping interactive target for the platform and context. Around 40px is a useful web heuristic, not a universal standard; use the platform's accessibility guidance when stricter.
- `prefetch-touch-fallback`: hover or pointer trajectory prefetch must have a touch/keyboard path and must not be required for correctness.
- `a11y-visual-equivalent`: sound cannot be the sole carrier of status or meaning; provide a visible or haptic equivalent where the product needs one.
- `a11y-toggle-setting`: recurring nonessential sound needs an accessible way to mute or control it.
- `a11y-reduced-motion-check`: honor `prefers-reduced-motion` for nonessential movement. Control sound separately; reduced-motion preferences do not express an audio preference.
- `a11y-volume-control`: independent sound layers should have usable volume control when the product exposes those layers.

## CSS structure

- `pseudo-content-required`: `::before` and `::after` need a `content` declaration when used for generated content or decoration.
- `pseudo-position-relative-parent`: an absolutely positioned pseudo-element needs the intended positioned containing block.
- `pseudo-z-index-layering`: pseudo-elements and interactive children need an explicit stacking relationship when overlays can intercept clicks or obscure focus.
- `pseudo-hit-target-expansion`: an invisible hit-area expansion must remain inside the intended control and must not overlap neighboring controls.
- `transition-name-unique`: View Transition names must be unique for simultaneously transitioning elements; remove temporary names after the transition.

## Type, surfaces, modes, and cognition

- `type-tabular-nums-for-data`: use tabular figures when changing numeric columns need stable alignment; it is optional for prose.
- `type-text-wrap-balance-headings`: balanced heading wrapping is a presentation improvement for short headings, not a correctness requirement. Verify the browser support and avoid it for long text.
- `type-text-wrap-pretty`: pretty wrapping can reduce orphans in short/medium prose; do not call its absence a bug.
- `type-antialiased-on-retina`: font smoothing is platform-dependent and should be tested visually; never treat a missing declaration alone as a defect.
- `visual-concentric-radius`: nested radii can be calculated from padding to create a coherent surface; use the existing design system when it defines another convention.
- `visual-layered-shadows`: layered shadows can communicate elevation; report only a demonstrated contrast, hierarchy, or consistency problem.
- `visual-consistent-spacing-scale`: prefer the product's spacing tokens; a raw value is a finding only when it breaks established rhythm or responsive behavior.
- `modes-indicator-at-locus`: persistent modes need a visible indicator near the user's focus or control.
- `modes-unambiguous-focus-target`: when several inputs accept keystrokes, the active destination must be apparent and keyboard focus must be reliable.
- `modes-no-triple-state-toggle`: avoid cycling through three or more subtle states on one control; expose state and alternatives clearly.
- `modes-expose-hidden-context`: accumulated filters, chat context, or edit modes need a visible summary and a simple reset path.
- `ux-progressive-disclosure`: reveal complexity when it becomes relevant while keeping the basic path understandable.
- `ux-cognitive-load-reduce`: remove information or motion that does not support the current decision; do not equate minimalism with fewer features automatically.

## Focused polish and interaction

- `visual-reuse-design-tokens`: reuse existing font, color, radius, and spacing tokens when they express the intended value. Preserve the product identity; propose a new type system only when that is in scope.
- `visual-optical-icon-alignment`: asymmetric icons may need optical adjustment rather than geometric centering. Treat this as a recommendation and verify it at the rendered size.
- `visual-image-edge-contrast`: a subtle outline can distinguish image edges from the surrounding surface; consider dark edges on light surfaces and light edges on dark surfaces. Verify both themes and avoid adding outlines without a visible need.
- `visual-purposeful-grouping`: remove redundant eyebrow labels, unnecessary card wrappers, decorative backgrounds, or competing text styles only when doing so improves hierarchy. Preserve meaningful grouping, controls, and the established visual identity.
- `ux-hover-touch-path`: hover-revealed controls need keyboard and touch access. Gate hover-specific reveals behind a hover-capability query where appropriate; give touch menus a usable toggle and dismissal path. Verify focus and dismissal, not just appearance.
- `ux-card-link-layering`: avoid nested interactive elements in whole-card links. A stretched link overlay must leave inner links/buttons independently operable and focus visible; verify pointer and keyboard behavior.
- `ux-refresh-preserves-input`: polling or live refresh should update the relevant content without discarding typed input, selection, or focus. Check the active editing state during an actual refresh.
- `transition-explicit-properties`: transition only intended properties instead of using `transition: all`, which may animate unrelated layout or state changes. Retarget user-controlled transitions without jumps when interrupted.
- `perf-will-change-evidence`: avoid `will-change: all` and speculative persistent layer promotion. Use targeted hints only for an observed rendering problem, verify their effect, and release temporary hints when no longer needed.
- `a11y-nonessential-sound-frequency`: avoid decorative sound on high-frequency interactions; repeated cues can distract or overwhelm. Keep meaningful feedback and accessible audio controls.
