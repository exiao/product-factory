# Creative exploration

Use for open visual exploration or a substantial aesthetic revision. Existing product constraints and the user's chosen direction still govern.

Adapted from the accessible portion of Anshu Chimala's [How to turn your AI into a world-class designer](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world). The retrieved article stops at the heading for technique 7; its remaining content was unavailable.

- Explore brief, widely differing concepts before detailing favorites. Translate the user's reactions into concrete material, composition, and interaction choices.
- If exploration keeps converging, optionally generate a random string with a local script as an inspiration cue. Keep it out of the product; judge the resulting direction on merit.
- For a substantial visual revision, use a fresh-context subagent critic with screenshots, the intended aesthetic, and relevant reference images. Withhold implementation rationale and prior critiques. Request specific composition and detail gaps; references establish a quality baseline, not a design to copy.
- Start with one critique and one confirmation. Avoid an endless numerical-score target.
- Consider generated imagery or video when the chosen direction benefits. Loops or keyframe transitions can support motion; inspect their actual playback and intermediate frames.
- Finish by removing decoration, labels, or containers that contribute no useful meaning.

## Image assets

Use generated images in two ways: concept previews to resolve an open visual direction, or production assets for the selected direction. Generate previews only when they help a real choice; a precise brief can proceed to the production asset. A generated page concept is visual evidence, not a functioning interface.

For each useful asset, derive a compact brief from its actual placement: purpose and subject, style references, palette, composition and focal point, intended aspect ratio and responsive crops, negative space for overlaid copy, and transparency when needed. Identify supplied images as references or edit targets and preserve required brand and product details. Keep functional text and controls in the implemented interface rather than baking them into the image.

Load [$image-generation-guide](../../image-generation-guide/SKILL.md) for the brief and visual checks, then use Codex built-in image generation/editing and save the result locally. Generate the needed raster asset rather than merely describing one. Follow that skill's tool and fallback rules; if unavailable or blocked, report the missing asset and unresolved integration accurately. Do not silently substitute another provider. Generation is unnecessary when existing assets, native vectors, or code better meet the brief.

Inspect the output, copy the selected production asset into the project's asset directory, and update the consuming code. Do not leave project references pointing at temporary or tool-owned output paths. Preserve originals unless replacement is requested. Set appropriate dimensions, delivery size, and semantic alt text or decorative treatment.

Inspect the asset in the rendered page at relevant desktop/mobile sizes: crop, focal point, copy contrast, transparency edges, loading, and visual consistency. Refine the image or layout for observed defects within the existing verification budget. Preview-only concepts may remain previews; distinguish them from integrated deliverables.

## Integration constraints

The visual critic does not replace implementation inspection, accessibility checks, or interaction testing. Follow session model and delegation preferences; do not hardcode an article's model names. If delegation is unavailable, disclose a self-review. Use available media skills/tools, preserve reduced-motion alternatives and performance budgets, and do not introduce credentials into product code. Continue targeted fixes for known material defects under the existing verification rules.

The user subsequently supplied a visual comparison of overused patterns and alternatives. Its concrete guidance is incorporated in the personal defaults in [design-mode](../SKILL.md); this does not establish access to the remainder of the article.
