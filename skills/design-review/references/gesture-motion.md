# Gesture and motion checks

Use when the affected UI has a drag, swipe, sheet, carousel, comparison slider, or another control whose motion follows input. Draw on [Apple Design](https://github.com/emilkowalski/skills/tree/main/skills/apple-design) and [Design Engineering](https://github.com/emilkowalski/skills/tree/main/skills/emil-design-eng) for the interaction model; confirm behavior in the running product. Preserve the project's animation system and avoid a new dependency for a small fix.

## Before choosing motion

- Identify what state changes and whether movement helps the person predict or confirm it. Remove motion that delays a frequent action or competes with the current task. Repeated keyboard navigation should remain prompt and visibly focused.
- Give immediate visual press feedback where useful, but commit a consequential action on release so a pointer can cancel by moving away. Motion must not delay the action or hide its result.
- Respect reduced-motion preference: keep state changes perceivable with a static or low-motion alternative, and test that alternative in the rendered UI.

## Direct manipulation

- During a drag, the object should track the pointer continuously from its grabbed offset. Use pointer capture when the pointer can leave the element; account for a second touch or interrupted gesture.
- At release, hand off from the current on-screen position and velocity. If the control can be grabbed again mid-flight, it should retarget without a jump or input lock. A spring or another retargetable method can work; a CSS transition is acceptable when the observed behavior is continuous.
- Keep snap points and bounds understandable. A flick may select the next target based on direction and velocity, but should not move farther than the person reasonably expects. Use resistance at a boundary only when it clarifies that the end has been reached.
- Check entry and exit paths and the trigger origin for a sheet or popover. Motion should make the spatial relationship legible, not imply a destination different from the resulting state.

## Verify with the target input

- Tap, drag, release, and interrupt the control. A drag must complete, not merely start. Swipe along the page's scroll axis across it and verify the page or container can still scroll; then drag along the control's intended axis and verify the control responds.
- Exercise the equivalent keyboard or single-pointer path when the task otherwise depends on dragging. Check focus, dismissal, and reduced motion after the change.
- Say whether evidence came from a physical device, browser engine, emulated viewport, or synthesized touch input. A screenshot or resized viewport verifies layout, not a gesture. Report an untested physical-device path without guessing.
