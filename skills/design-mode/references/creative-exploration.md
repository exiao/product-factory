# Creative exploration

Use for open visual exploration or a substantial aesthetic revision. Existing product constraints and the user's chosen direction still govern.

Adapted from the accessible portion of Anshu Chimala's [How to turn your AI into a world-class designer](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world). The retrieved article stops at the heading for technique 7; its remaining content was unavailable.

- Explore brief, widely differing concepts before detailing favorites. Translate the user's reactions into concrete material, composition, and interaction choices.
- If exploration keeps converging, optionally generate a random string with a local script as an inspiration cue. Keep it out of the product; judge the resulting direction on merit.
- For a substantial visual revision, use a fresh-context subagent critic with screenshots, the intended aesthetic, and relevant reference images. Withhold implementation rationale and prior critiques. Request specific composition and detail gaps; references establish a quality baseline, not a design to copy.
- Start with one critique and one confirmation. Avoid an endless numerical-score target.
- Develop generated media as part of the visual concept when it can supply distinctive subjects, materials, atmosphere, or a visible transformation. Use the storytelling guidance below; do not equate adding motion with adding meaning.
- Finish by removing decoration, labels, or containers that contribute no useful meaning.

## Image assets

Use generated images in two ways: concept previews to resolve an open visual direction, or production assets for the selected direction. Generate previews only when they help a real choice; a precise brief can proceed to the production asset. A generated page concept is visual evidence, not a functioning interface.

For each useful asset, derive a compact brief from its actual placement: purpose and subject, style references, palette, composition and focal point, intended aspect ratio and responsive crops, negative space for overlaid copy, and transparency when needed. Identify supplied images as references or edit targets and preserve required brand and product details. Keep functional text and controls in the implemented interface rather than baking them into the image.

Load [$image-generation-guide](../../image-generation-guide/SKILL.md) for the brief and visual checks, then use Codex built-in image generation/editing and save the result locally. Generate the needed raster asset rather than merely describing one. Follow that skill's tool and fallback rules; if unavailable or blocked, report the missing asset and unresolved integration accurately. Do not silently substitute another provider. Generation is unnecessary when existing assets, native vectors, or code better meet the brief.

Inspect the output, copy the selected production asset into the project's asset directory, and update the consuming code. Do not leave project references pointing at temporary or tool-owned output paths. Preserve originals unless replacement is requested. Set appropriate dimensions, delivery size, and semantic alt text or decorative treatment.

Inspect the asset in the rendered page at relevant desktop/mobile sizes: crop, focal point, copy contrast, transparency edges, loading, and visual consistency. Refine the image or layout for observed defects within the existing verification budget. Preview-only concepts may remain previews; distinguish them from integrated deliverables.

## Generated media and storytelling

For an open visual brief, actively look for one strong media-led idea before committing to a code-only composition. Generated media can carry personality, emotional tone, an explanation, or a miniature story; it need not justify itself only through functional utility. Name its contribution in a sentence: **the viewer sees X become/reveal Y, which expresses Z about this product or experience**. A still can contain the entire story. Do not force a narrative arc onto every icon or add promotional media to a task-focused screen merely to meet this preference.

Choose the medium from the intended experience:

| Role | Concrete treatment | What makes it useful |
|---|---|---|
| Story-bearing still | A specific scene, character, material study, or visual metaphor with deliberate composition | Establishes a recognizable feeling, relationship, or distinctive visual world; not interchangeable stock-like decoration |
| Integrated motion loop | A subject assembles, unfolds, breathes, or changes in a short restrained loop | Brings the visual idea to life while preserving the page's reading and interaction hierarchy |
| Transition between states | Establish clear start/end keyframes and generate the transformation between them | Reveals a product property or explains progression, with motion controlled by an action, scroll, or gesture when appropriate |

Example: a suitcase floating, landing and opening, then receiving its contents can reveal its shape and capacity through a sequence. A writing product could illustrate a tangled thread becoming a clear line, then show the real editor separately. These are possible mechanisms, not required themes. An unrelated spinning object does not tell a product story just because its rendering is elaborate.

### Develop the visual before implementing the effect

Derive the subject, action, composition, palette, material, lighting, camera, and intended placement from the accepted direction. Show the generated keyframe **inside its intended layout**, with actual copy and controls, before committing to extensive generation or integration. If direction remains unresolved, show comparable concrete alternatives and get the required human decision through the host workflow; Preserve any approval checkpoints in the host workflow. Do not treat this preference as blanket approval of a new creative direction, provider, or spend.

Once selected, use the still as a reference for motion. Preserve subject identity, product geometry, camera, scale, light, and palette across states. Where the chosen tool supports it, use start/end keyframes; use the inspected last frame of one clip to seed the next. Inspect the join rather than assuming seeding guarantees continuity. Test the essential transformation in a short draft before producing the full sequence. Prefer one excellent media element over unrelated images across every section.

Combine generated media with precise HTML/CSS, vector, shader, or 3D work when each has a clear role. Keep live text, buttons, data, and interaction state in code. Use real captures and supplied product assets for factual demonstrations; a generated UI, customer, result, or physical behavior must not masquerade as observed product proof. Illustration can be openly fictional without undermining its emotional value.

### Loops and compositing

A plain-background clip can be composited into the layout using keying or matting where supported, or deliberately integrated as an opaque scene. Test the subject against the actual light/dark backgrounds. Examine edges, shadows, fine details, and transparency artifacts at the final display size; choose the delivery format only after checking alpha support on target browsers/devices. A source background matching the page palette can make baked lighting more coherent.

Baked glass/refraction does not dynamically refract arbitrary content behind the video. If the effect must respond to live page content, use an appropriate real-time implementation or narrow the visual promise. Do not claim background removal creates physically correct transparency. Check the loop seam for pose, light, camera, and velocity discontinuities; a forward/reverse loop is useful only when its reversed action makes sense.

### Interactive playback and delivery

For scroll/gesture sequences, map the input to a bounded timeline and keep state transitions coherent when moving backward, jumping, resizing, or loading late. Avoid hijacking ordinary navigation to force the visitor through the animation. Essential content and actions must remain available if playback fails or is disabled. Provide an appropriate static poster/reduced-motion presentation; load media in proportion to its visibility and importance, and fit dimensions, compression, and decoding cost to the target device.

Review the integrated result at target viewport sizes: the first frame, intermediate frames, keyframe joins, loop seam, and actual playback or scrubbing. Check subject consistency, meaningful progression, crop, contrast, edges, controls, fallback, and loading. Frame inspection alone cannot verify fluid motion. State unverified playback honestly; use the host's existing review budget and human review surface instead of adding an unrelated review process.

For stills, use [image-generation-guide](../../image-generation-guide/SKILL.md) and the built-in image tool. For video, use video-direction (optional, when installed) to define the shot and video-editor (optional, when installed) for assembly, with an available video-generation provider under the current authorization. If choosing Fal, load its installed skill and discover current capabilities before selecting an endpoint. Do not hardcode the excerpt's model names, availability, or billing claims. Preserve tool blocks and required cost decisions; credentials belong in the supported local environment, never in frontend bundles or shipped assets.

Source: user-supplied “Technique 4: Use image generation to enrich designs” and “Technique 5: For more advanced motion, use video generation” (2026-09-23). The excerpt contributes generated imagery, composited loops, and keyframe-driven interactive transitions. Its model/billing claims and claims about increased engagement are not treated as verified facts. The storytelling and review rules above adapt these techniques to the design workflow.

## Integration constraints

The visual critic does not replace implementation inspection, accessibility checks, or interaction testing. Follow session model and delegation preferences; do not hardcode an article's model names. If delegation is unavailable, disclose a self-review. Use available media skills/tools, preserve reduced-motion alternatives and performance budgets, and do not introduce credentials into product code. Continue targeted fixes for known material defects under the existing verification rules.

The user subsequently supplied a visual comparison of overused patterns and alternatives. Its concrete guidance is incorporated in the personal defaults in [design-mode](../SKILL.md); this does not establish access to the remainder of the article.
