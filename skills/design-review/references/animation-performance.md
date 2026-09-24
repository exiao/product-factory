# Animation performance checks

Use for an observed slow page, continuous animation, canvas/WebGL effect, or suspected long-session leak. This is adapted from [Optimize Web Animations](https://github.com/MengTo/Skills/tree/main/agent-skills/codex/optimize-web-animations). Prefer the project's existing visibility and cleanup patterns.

1. Measure the named route before editing. Sample the visible top, a middle section, and the footer; include the relevant mobile width. Record which CSS animations and canvas or JavaScript loops still run when their owners are offscreen. For a leak report, compare bounded idle and route-cycle samples, with DOM/canvas counts and memory data only when the runtime exposes it.
2. Find the owner of each active loop. CSS `animation-play-state` can pause a CSS animation, including a targeted pseudo-element rule, but it cannot stop `requestAnimationFrame`, media playback, GSAP, or a WebGL render loop. Gate those at their actual owner when the work is unnecessary offscreen.
3. On hide or unmount, cancel scheduled frames and timers, disconnect observers, remove listeners, pause detached media, and release graphics resources owned by the component. Guard async loads that may finish after unmount. Cap simulation frame deltas when resuming after a visibility pause.
4. Re-run the same samples. Confirm that offscreen work under test stops, visible motion resumes correctly, normal interaction still works, and route cycles do not accumulate elements or renderers. Report unavailable heap counters as unmeasured rather than as proof of no leak.

Do not remove useful visible motion merely to lower a counter. A passing build or reduced-motion style check does not establish runtime performance; record the observed before/after behavior and the tested browser or device.
