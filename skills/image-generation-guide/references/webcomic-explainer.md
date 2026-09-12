# Webcomic explainers

Use when the user wants a comic that explains a technical change, plan, process, or system state. For product-journey research storyboards, use the storyboards skill. This is an optional illustration method within image-generation-guide, not a separate generation provider.

Adapted from `skills/creative/webcomic-explainer/SKILL.md` in hermes-setup. Retains its explanation method; legacy Nano Banana, pricing, cron, Signal, and board integration instructions do not apply.

## Ground the story

Read the actual diff, plan, report, or supplied source. Extract the mechanism, the obstacle or change, its consequence, and the one takeaway. Keep identifiers and facts accurate. If a fictional example helps, label it explicitly; never represent the comic as customer evidence or a real event.

Keep any existing deterministic detection or comparison upstream. The illustration explains the resulting facts; it does not re-decide them. For an explicitly requested recurring workflow, reuse unchanged illustrations and the source's deduplication rather than generating on every tick. Do not create a recurring workflow merely to illustrate a document.

## Compose the explanation

Pair a short plain-language brief with a readable comic. The brief states the takeaway and any actual decision needed; the comic makes the cause and effect visible.

- Use a small multi-panel arc, often 3–6 panels: initial situation, obstacle or test, changed mechanism, resulting outcome. Choose the count around the explanation.
- Make the characters act on the mechanism. Avoid decorative mood art or a box diagram merely dressed as a comic.
- Use real short specifics when helpful: a command, filename, status, or value. Put long explanations in the surrounding prose. Do not invent metrics to make the scene persuasive.
- Keep recurring characters, objects, connections, and action direction consistent. Write panel-by-panel invariants before generation: what stays the same, what changes, and why.
- Match the user's or project's style. Provide exact short dialogue, panel order, aspect ratio, and the intended reading size. A comic should remain legible without zooming excessively.

## Generate and inspect

Use the parent guide's built-in image workflow, reference handling, local delivery, and bounded revisions. Save the panel script or exact prompt with the image. Do not inherit an old provider choice, quota workaround, or blanket ban on correcting text.

Inspect every panel for reading order, text, character identity, geometry, and causal continuity. In the local watering-machine trial, the test-panel jet came from a different fitting: an attractive comic can still misrepresent its mechanism. Check connectors, nozzles, switches, and other objects carrying the explanation across frames.

If a correction is needed, edit the strongest image with only that targeted change and preserve its original. Deliver the readable image and short brief; disclose unresolved continuity or text defects. Keep final files in `output/images/` or the user's chosen directory. Generation does not authorize external sharing.
