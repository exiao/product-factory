---
name: storyboards
description: Create illustrated product-journey storyboards that show a person’s problem, current workaround, product interaction, and changed outcome. Use for storyboard comics and before/after journeys; video shot lists belong to video-direction.
---

# Product storyboards

## Still-image generation

For generated or edited still images, use [$image-generation-guide](../image-generation-guide/SKILL.md): Codex built-in image generation, verified files saved in the local project. This applies to reference sheets and intermediate assets as well as final images. Keep this skill's creative requirements; do not automatically use provider CLIs, external generation plugins, or remote rendering services. An explicit user request for another provider takes precedence.

Start from one person and one situation. State the people problem in plain language: what they are trying to do and why the current way fails them. State the design question the storyboard should help answer. Describe a functional, emotional, or social need before naming a solution. Reuse supplied research, label material claims with source IDs and confidence, and distinguish an imagined scenario from an observed customer story. A dogfood pass can support product-behavior claims, not customer sentiment.

Write captions before drawing. The default six-panel arc is setting, trigger, old way, encounter with the feature, one meaningful action, and the changed situation back in the person's life. Across the sequence, show how the person’s action leads to the product response, enables the next step, and could produce the outcome. Mark untested causal links; do not force a complete action/outcome cycle into every panel. Keep the same persona, situation, goal, and surrounding context across before/after alternatives; change the intervention being compared. Use a separate strip for a meaningful branch. Follow a requested panel count or narrative structure instead of forcing six.

Use the notebook-sketch visual language in [references/notebook-style.md](references/notebook-style.md) unless the user supplies another style. Default to a three-column, two-row composition for six panels. Keep captions short; specify exact labels and any required screen text. Do not invent product features, tickers, numbers, or successful outcomes as factual evidence.

For an illustrated storyboard request, use the available image-generation capability and its instructions. Pass the full panel specification, shared character details, and style in a single coherent brief. Reuse supplied character references when relevant. Do not call old provider scripts or promise a specific model unavailable in the current environment. A text-only storyboard request needs only the captions/panel specification.

Inspect the image before delivery: panel count and order, consistent person, situation, and actions, legible labels, causality from action to response to next step/outcome, and adherence to the selected style. Show waiting, retry, failure, abandonment, or recovery when that state is part of the design question. A proposed successful outcome is valid when clearly labeled as intended, not observed. Match visual polish and caption certainty to the evidence: a polished drawing must not make a hypothetical outcome look observed. Correct material mistakes with a focused edit. If visual generation or inspection is unavailable, report that limitation; a prompt is not a completed comic.

When the storyboard is a research stimulus, pilot comprehension with someone who has not heard the intended story, when available: ask them to describe what happens in each panel before explaining the concept. Record confusing transitions, then separately probe the problem, intervention and claimed benefit. A coherent story can depict an unwanted solution; agreement with its narrative is not demand. A synthetic reader remains a simulation. Do not add participant testing to a simple illustration request.

Deliver the people problem, design question, concise panel captions, and the generated image or actual file link. When the storyboard informs a product decision, add a compact decision note: claim-level evidence labels/source IDs and confidence, the recommendation, a plausible alternative explanation, and what evidence would change it. Preserve source and uncertainty labels received from research or a journey map; drawing a claim does not validate it. For a simple illustration, captions and the image are sufficient. Keep the story centered on the person's experience; it is a design explanation, not proof the product achieves the depicted outcome.
