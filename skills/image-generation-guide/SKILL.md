---
name: image-generation-guide
description: Create or edit raster images using concrete visual briefs, reference roles, identity and product preservation, controlled iteration, and visual verification. Use for image generation, portrait realism, product imagery, reference edits, illustration assets, explanatory comics, notebook sketches, sticker-style assets, and image prompt writing; excludes video generation and code-native vector or interface implementation.
---

# Image generation guide

Turn the requested image into a concrete visual brief, generate or edit it, inspect it, and deliver the actual file. Keep the creative method independent of provider, model, and reference-token syntax. A prompt-only request ends with the prompt.

## Generated media in this workflow

For design/content assets, use [generated media and storytelling](../design-mode/references/creative-exploration.md#generated-media-and-storytelling) to brief a specific scene, relationship, or visual transformation rather than generic decoration. Include the intended layout, crop, surrounding palette, and copy space; deliver a usable asset for integration. For motion anchor frames, preserve the subject, geometry, camera, and lighting needed by the planned transition, and identify start/end states explicitly. If the frames will be supplied to image-to-video, save the start and end as separate full-frame images with matching dimensions and aspect ratio; a combined review sheet does not replace those files. A generated keyframe remains a still until the downstream motion is produced and inspected. Respect the host's pending human choices before expanding the asset set.

## Execution and local delivery

In Eric's Codex environment, use the built-in image-generation tool and follow its current tool instructions. Save requested deliverables in the current project, normally `output/images/`, or the user's chosen directory. This means local files, not inference running on the Mac or offline generation. Do not invoke a provider CLI, paid API, plugin generation service, or remote rendering workflow as an automatic fallback. If the built-in capability is unavailable, report the blocker and retain the brief; an explicit request for another provider changes this choice.

A specialist skill may own the product, storyboard, thumbnail, illustration style, or video production brief; this guide owns its still-image prompting and review. Apply the execution preference above to still-image generation and editing within specialist skills and plugin workflows, including reference sheets and intermediate assets. Keep their useful creative requirements while replacing default external image-generation steps with the built-in tool, unless the user explicitly requests another provider. This includes still-image assets within video workflows; it does not apply to video or audio generation. For built-in tool mechanics, use the installed imagegen skill when available; do not copy its implementation details here.

Inspect local references before editing. Label each image by role: edit target, identity, product, scene/composition, or style. Use only actual provided or generated images and the reference mechanism supported by the current tool. Never invent numbered upload IDs, paths, or model parameters.

## Shape the brief

Preserve the user's specific prompt rather than expanding it with extra objects or invented requirements. For a vague request, add the minimum concrete detail needed to make composition and purpose clear:

```text
Purpose and format:
Subject and action:
Scene and composition:
Light sources and material detail:
Reference roles:
Preserve:
Change:
Exact text, if any:
Avoid observed failures:
```

Omit irrelevant fields. Resolve the visual identity from the explicit brief, current project assets and design rules, then applicable personal defaults. Inspect a project visual-identity file when one exists; do not impose a historical brand palette on unrelated subjects. Choose framing, crop, negative space, and subject scale for the actual output surface. For a web asset, brief the image separately from the UI; controls and responsive text remain code. Preserve existing official logos and product assets when generation would distort them. Use vectors or code for existing vector systems and precisely editable diagrams when those are the requested deliverable.

- For comics explaining a change, plan, or process, read [webcomic explainers](references/webcomic-explainer.md).
- For photographs and identity edits, read [realism and reference editing](references/realism-and-identity.md).
- For the black-and-blue notebook look, read [notebook sketch style](references/notebook-sketch.md).
- For die-cut stickers and sticker-style cards, read [sticker style](references/sticker-style.md).
- For products, thumbnails, illustration sets, and visual assets, read [composition and asset sets](references/composition-and-sets.md).
- For where this guidance came from and the source limitations, read [sources](references/sources.md). Historical observations are not universal model guarantees.

## Generate, compare, and finish

Start with one useful draft unless the user requested alternatives or a comparison is needed to resolve a real choice. For a controlled comparison, hold the subject, framing, setting, and all other instructions fixed while varying one factor. Do not call a comparison controlled if the light, camera, and background also changed.

Edit the strongest existing candidate to preserve identity and composition. Keep its original file. Change only the observed problem and restate the important invariants. A model may still change untargeted details: inspect the whole result, especially text, hands, product geometry, face, lighting, and background. Do not keep retrying without new corrective information; report an unresolved limitation after focused corrections stop improving it.

For each delivered image, verify subject/count, composition, requested style, reference fidelity, text, anatomy or geometry, light/shadow consistency, unwanted elements, and intended dimensions/crop. Keep two judgments separate: does the image communicate the intended idea, and does the delivered file meet the requested specification? Distinguish brief violations from optional taste changes. Check transparency only when requested and supported. Inspect thumbnails at their display size and integrated web assets in their actual layout. Use thumbnails and contact sheets for triage, then inspect each selected final at full resolution as well as at its intended display size. OCR can help verify words and numbers but cannot validate shape, identity, attire, or composition; keep those checks unverified if visual inspection is unavailable. Do not claim an image is photoreal, identity-consistent, or production-ready from its prompt alone.

Save final images under stable filenames with the exact prompt and reference roles in a concise sidecar when useful for reuse or asset sets. Preserve the source render before format conversion. Verify the final saved or transferred copy exists and opens; measure its actual dimensions and detect its format rather than trusting the requested settings or filename. A viewer failure alone does not prove the image is corrupt. Show the image and provide an absolute local file link. Report material deviations or unfinished checks. Generation does not authorize publishing, ad uploads, or other external distribution.
