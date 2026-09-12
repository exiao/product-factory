# Rule selection

Use the smallest applicable set. These IDs are defined locally in [selected-rules.md](selected-rules.md); cite that definition when reporting a finding.

| Area | Rules to check |
|---|---|
| Interactive motion | `duration-max-300ms`, `duration-press-hover`, `spring-for-interruptible`, `easing-entrance-ease-out`, `easing-exit-ease-in`, `none-keyboard-navigation`, `staging-one-focal-point` |
| Exit and lists | `exit-requires-wrapper`, `exit-prop-required`, `exit-key-required`, `presence-disable-interactions`, `mode-pop-layout-for-lists` |
| Touch and targets | `ux-fitts-target-size`, `ux-fitts-hit-area`, `prefetch-touch-fallback`, `none-context-menu-entrance` |
| Accessibility/audio | `a11y-visual-equivalent`, `a11y-toggle-setting`, `a11y-reduced-motion-check`, `a11y-volume-control` |
| CSS structure | `pseudo-content-required`, `pseudo-position-relative-parent`, `pseudo-z-index-layering`, `pseudo-hit-target-expansion`, `transition-name-unique` |
| Type and surfaces | `type-tabular-nums-for-data`, `type-text-wrap-balance-headings`, `type-text-wrap-pretty`, `type-antialiased-on-retina`, `visual-concentric-radius`, `visual-layered-shadows`, `visual-consistent-spacing-scale` |
| Focused polish | `visual-reuse-design-tokens`, `visual-optical-icon-alignment`, `visual-image-edge-contrast`, `visual-purposeful-grouping` |
| Responsive behavior | `ux-hover-touch-path`, `ux-card-link-layering`, `ux-refresh-preserves-input` |
| Rendering and repeated feedback | `transition-explicit-properties`, `perf-will-change-evidence`, `a11y-nonessential-sound-frequency` |
| Modes and cognition | `modes-indicator-at-locus`, `modes-unambiguous-focus-target`, `modes-no-triple-state-toggle`, `modes-expose-hidden-context`, `ux-progressive-disclosure`, `ux-cognitive-load-reduce` |

Keep thresholds as heuristics where platform or product context matters. A rule named in a report should exist in the local skill's ruleset or be clearly labeled as a recommendation rather than a fabricated rule. `exit-*`, `presence-*`, `mode-*`, and related names describe patterns from libraries such as Motion/AnimatePresence; apply them only when that library is actually used, and translate the underlying lifecycle requirement for other frameworks.

For compact implementation evidence after selecting rules, use [selected-examples.md](selected-examples.md). The examples are deliberately limited to common failure modes and do not replace reading the matching rule definition.
