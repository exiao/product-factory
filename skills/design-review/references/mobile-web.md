# Mobile web checks

Use for a mobile web or PWA symptom. Inspect the current viewport metadata, styles, and touch behavior before changing them. These checks adapt [Emil Kowalski's mobile-native skill](https://github.com/emilkowalski/skills/tree/main/skills/mobile-native); they are conditional fixes, not a global CSS reset.

| Observed problem | Check and smallest likely fix |
| --- | --- |
| Hover treatment sticks after a tap | Gate hover-only decoration on input capability, such as `(hover: hover) and (pointer: fine)`; keep a visible touch and keyboard state. |
| Full-height shell or bottom action is hidden by browser chrome | Check `100vh` against `100dvh` for a shell or `100svh` for a stable first-screen layout. Confirm with the browser bars expanded and collapsed. |
| iOS zooms when an input receives focus | Inspect the rendered input font size; use at least 16 CSS pixels where this behavior occurs. Keep pinch zoom available. |
| A custom tap feels late or shows conflicting feedback | Check press feedback on `:active` or pointer down and commit on release. Consider `touch-action: manipulation` for the control; preserve cancellation. Remove browser tap highlight only when the replacement feedback is visible. |
| A fixed header, sheet, toast, or bottom bar overlaps the notch or home indicator | Check `viewport-fit=cover` and padding with `env(safe-area-inset-*)`; apply safe-area padding to affected chrome, not indiscriminately to every container. |
| A swipe control steals page scroll or cannot complete its gesture | Test both axes on the target input. Set `touch-action` for the axes the browser should retain; prefer native scrolling with scroll snap when it serves the interaction. See [gesture and motion checks](gesture-motion.md). |
| Long press selects a control label or opens an unwanted callout | Limit `user-select: none` or touch callout suppression to the affected control; keep content such as addresses and error messages selectable. |
| Page scroll or pull-to-refresh interferes with an app-specific scroll area | Consider `overscroll-behavior` on the relevant root or nested scroller. Preserve ordinary document scrolling and pull-to-refresh when they are useful. |
| Browser chrome or status bar clashes with the current theme | Check `theme-color` for the displayed scheme and installed PWA mode. |

Prefer CSS capability queries and browser layout units to device sniffing. Test with a real phone when available, including an open software keyboard, landscape, and installed mode if it is a PWA. Simulator and device emulation can locate issues but do not establish hardware touch feel, browser chrome, or safe-area behavior. Report which environment produced each observation and what remains untested.
