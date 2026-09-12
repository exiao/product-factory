# Interface craft reference

Use this as a decision aid while implementing or reviewing an interface. The
brief, product system, users, and supported browsers outrank these defaults.
## Visual system

- Define semantic tokens for text, surfaces, borders, actions, status colors,
  spacing, type, elevation, and motion. Keep primitive values separate so a
  theme can change semantic assignments without rewriting components.
- Prefer a small, coherent palette: neutral surfaces and text carry most of
  the visual weight; accent colors identify actions and important states.
  Assign success, warning, error, and information roles explicitly.
- Test text and controls against their actual backgrounds. Aim for WCAG AA
  contrast (4.5:1 body text, 3:1 large text and non-text controls); do not
  rely on color alone to convey status.
- Treat light and dark themes as separate surface/contrast decisions. Dark
  interfaces generally need layered surfaces and restrained accents rather
  than a literal color inversion.
- Use a limited type scale with clear hierarchy. Set a readable measure (often
  near 65ch for long text), appropriate line-height, and `rem`-based body
  sizing. Use tabular numerals where aligned data benefits from them.
- Load custom fonts with a visible fallback and metric-aware tuning when
  practical. Avoid introducing a second family without a clear hierarchy
  reason; preserve existing brand typography when it is part of the product.
- Use a spacing scale and semantic names. `gap` is usually clearer than
  sibling margins. Group content with alignment, type, and whitespace before
  adding another card or border.

## Layout and responsive behavior

- Start with the narrowest useful layout, then add complexity when the content
  requires it. Let content determine breakpoints; use `clamp()` for values that
  should scale smoothly.
- Prefer container queries for reusable components and viewport queries for
  page-level composition. A component should remain usable in a sidebar as
  well as a wide main column.
- Design for pointer and hover capability, not screen width alone. Every
  hover affordance needs a touch and keyboard equivalent.
- Protect mobile layouts with safe-area insets when the app can run edge to
  edge. Use responsive images with accurate `srcset`/`sizes`; use `<picture>`
  when the crop or composition must change.
- Tables, navigation, and dense controls need an intentional small-screen
  representation: cards, progressive disclosure, or a drawer can be valid
  choices when reading order and actions remain clear.
- Check real device behavior when touch, font rendering, memory, network, or
  keyboard chrome can change the result; emulation does not establish behavior on every real device.

## Interaction and accessibility

- Design default, hover where supported, focus, active, disabled, loading,
  error, and success states for each interactive control. Keep a visible
  `:focus-visible` treatment with sufficient contrast; never remove focus
  without an equivalent.
- Use visible labels, associate errors with fields via `aria-describedby`, and
  validate at a helpful moment. Error copy should state what happened, why it
  matters, and the next useful action.
- Keep touch targets comfortably tappable (around 44px when feasible), while
  allowing the visual icon to remain smaller through padding or hit-area
  expansion.
- Prefer native semantics (`button`, `label`, `dialog`, `details`) before
  custom roles. For tabs, menus, and radio groups, implement the expected
  keyboard model such as roving tabindex and arrow-key movement.
- Modals must manage focus, Escape, dismissal, and background inertness. For
  overlays, use native popovers or a portal/fixed-position fallback when
  clipping and stacking contexts make inline absolute positioning unsafe.
  Feature-detect newer positioning APIs and retain a supported fallback.
- Use optimistic updates only for reversible, low-stakes actions with a clear
  rollback path. Confirm or wait for server success for payments, destructive
  operations, permission changes, and other consequential writes.
- Prefer undo for reversible deletion; reserve confirmation for irreversible,
  high-cost, or batch actions and name both the action and its consequence.
- Gestures must have visible alternatives. Do not make swipe, hover, or color
  the only way to discover or complete an action.

## Motion and feedback

- Motion should explain state, hierarchy, or spatial relationship. Keep
  micro-feedback short, use transform/opacity where suitable, and avoid adding
  animation when a static state communicates better.
- Choose durations and easing per interaction rather than applying one rule
  everywhere. Exits can be shorter than entrances; long waits need progress or
  useful progressive content rather than decorative motion.
- Honor `prefers-reduced-motion`. Remove spatial movement where possible while
  preserving essential status feedback such as progress and focus.
- Use skeletons when the content shape is known and a spinner when it is not;
  do not use animation to conceal slow or unreliable work. Test loading,
  retry, timeout, offline, and partial-success states.

## Copy and review

- Label actions with a specific verb and object (`Save changes`, `Delete 5
  items`). Keep terminology consistent across navigation, controls, and help.
- Empty states should explain what is absent, why it matters, and the next
  useful action. Links should make sense out of context; icon-only controls
  need accessible names; decorative images need empty alt text.
- Leave room for translated copy and longer labels. Keep complete messages as
  translatable strings rather than assembling fragments around numbers.
- Review the primary task first: hierarchy, readable content, action clarity,
  error recovery, keyboard/touch access, responsive layout, and reduced-motion
  behavior. Validate with the actual product brief and supported environment.
