# Persona annotations on actual screenshots

Use for visual walkthroughs, rendered UX variants, and gate reviews. The deliverable should let the reader see exactly what prompted the reaction. This is a presentation and grounding workflow, not authorization to capture unrelated screens or share sensitive material.

## Ground the reaction in an image

1. Capture meaningful states with the supported browser/app tool, or use supplied screenshots. Keep task context and the action that reached each state. Record screenshot ID, route or screen name, viewport dimensions, and provenance (captured now, supplied, or earlier capture). For supplied/earlier images, do not imply freshness or successful live execution.
2. Before guided actions or detailed element prompts, inspect the initial screen in the persona's task context: "What seems primary?", "What would I do first?", and "What competes for my attention?" Record the simulated impression, including uncertainty or no friction. For redesigns, include the available original on the same task and a comparable viewport; disclose if it cannot be inspected. These are hypotheses about hierarchy, not measured gaze, attention, or task time. If the persona already knows the screen, label that familiarity instead of claiming a cold impression.
3. Have each persona inspect the actual screenshot before reacting. A source-code read cannot substitute for visual inspection. Use the same screenshot set for variant comparisons where appropriate, and keep persona annotations distinguishable.
4. At each meaningful moment, capture a short first-person reaction and the element that prompted it: expectation, confusion, intended action, relief, or a reason to continue. Include helpful moments and disagreement when present; don't force a negative or a quota of notes.
5. Verify objective claims separately. A visible disabled control is observable; its behavior after a click needs a live check. "I'd leave here" is a simulated intention, not observed abandonment. Missing input fields should be anchored to the relevant task area and described as absence, not pinned to an invented control.

For delegated visual reviews, provide a compact brief: persona ID and context, task, prototype boundaries, assigned states, screenshot paths, preceding state, verified action results, and annotation format. Exclude the researcher's desired finding. Return states covered, screenshots actually inspected, observed actions/results, annotation records, and untested states. The coordinating agent checks coverage against the task, completes material gaps where possible, and labels what remains untested. Functional PASS results alone do not establish understandable UX or replace the annotated board.

Suggested annotation record:

```json
{
  "id": "a1",
  "screenshot_id": "comparison-mobile",
  "persona_id": "p1",
  "persona": "Maya (synthetic)",
  "target": "Choose a direction button",
  "anchor": {"x": 0.72, "y": 0.84},
  "reaction": "I'm still deciding. Do I have to pick one first?",
  "simulated_action": "Look for a way to ask a follow-up",
  "observed_fact": "Button appears disabled in this capture",
  "verification": "Visual only; click behavior not tested"
}
```

Coordinates are normalized to the displayed source image, including its original crop; use a box when a region is more precise than a point. Choose anchors from the inspected image rather than guessed source-code order. Preserve original image dimensions and crop metadata so markers stay aligned when resized.

## Build the annotated artifact

Prefer a small HTML board with the untouched screenshot as an image and deterministic overlay pins/boxes, connected to numbered notes beside or beneath it. This keeps text selectable and avoids rewriting screenshot pixels. A static annotated image/PDF is also suitable when requested and supported. Image generation is unnecessary for annotation overlays and must not redraw the app as evidence.

- Put **SYNTHETIC REACTIONS** and the screen/state label visibly on each board or exported page. Quotes remain hypothetical even on a real screenshot.
- Show the persona's distinct display name and a concise first-person quote for each pin; retain its stable `persona_id` in the annotation data. Put analyst interpretation, alternative explanation, and proposed check in secondary detail; do not rewrite the quote as a designer recommendation.
- Keep controls and important copy visible. Put long notes in the margin, not over the screen. Use more than one view if a full-page screenshot makes everything tiny. Retain orientation when cropping and link the original capture.
- Use source image coordinates for pins and responsive positioning. On narrow screens, put notes below the image and provide a full-size view. Don't shrink a tall screenshot until its labels are unreadable.
- In interactive boards, selecting a pin should reveal/highlight its matching note. Use real keyboard-operable buttons, visible focus, accessible names, and a readable numbered-note fallback; do not rely on hover or color alone. Multiple personas may share a pin, but preserve dissent rather than collapsing it into a consensus quote.
- Use fictional or suitably redacted task data where possible. If a capture contains sensitive information, minimize or clearly mark redactions before including it in a shareable board; keep raw sensitive captures restricted rather than automatically bundling them. Keep the permitted source capture and annotation data available with the artifact. Store project-bound files together and use relative asset paths. Publish or send the board only within the user's requested scope.

## Verify and deliver

Render the board at its intended reading size. Check every pin against the actual element, note numbering, screenshot legibility, image loading, and any keyboard/selection behavior. A pin landing on the wrong element is a material error. Recheck affected annotations after changing a crop or replacing the screenshot.

Lead the handoff with the annotated screenshots/board, followed by a short synthesis of what worked, friction hypotheses, differences between personas, and what was actually reproduced. Full text transcripts can remain accessible as supporting detail. Do not claim customer validation, gaze tracking, measured behavior, or observed sentiment from synthetic annotations.
