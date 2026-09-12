---
name: notebook-sketch
description: Generate static notebook-style illustrations and diagrams with black fineliner outlines, royal-blue accents, and a cream dot-grid page. Use for notebook sketches, sketchnotes, and this hand-drawn look; not interactive web wireframes.
---

# Notebook sketch

## Still-image generation

For generated or edited still images, use [$image-generation-guide](../image-generation-guide/SKILL.md): Codex built-in image generation, verified files saved in the local project. This applies to reference sheets and intermediate assets as well as final images. Keep this skill's creative requirements; do not automatically use provider CLIs, external generation plugins, or remote rendering services. An explicit user request for another provider takes precedence.

Create a static illustration in the established notebook style. Reuse the supplied subject, references, labels, and layout constraints. For this named style, preserve the style block in [notebook style and layouts](../image-generation-guide/references/notebook-sketch.md); append the actual subject and composition. The user's explicit changes take precedence over the default palette or treatment.

Use the available image-generation capability and its instructions. Do not call old Hermes scripts, assume a specific model, or install a provider CLI. Choose aspect ratio and resolution for the subject and delivery surface: a wide comparison, a tall study, or a square single object. If the request is only for a prompt, provide the prompt without generating an image.

Spell out every required word and keep labels short. Use exact sourced values for factual diagrams; omit incidental UI text rather than inventing numbers or product claims. A complex explanatory diagram may need a simpler composition or separate panels so the visual structure and labels remain legible.

For a generated result, inspect line quality, palette, margins, label spelling, and whether the depicted relationships match the subject. Use a focused image edit to correct material errors while retaining the successful composition. Do not replace the look with vector stick figures or a generic doodle aesthetic. If the user requests interactive controls, treat that as a different deliverable and use the relevant interface workflow.

Deliver the generated image or actual absolute file path, with only necessary explanation. If generation or inspection is unavailable, state the limitation; a written prompt is not a completed illustration. Use [$storyboards](../storyboards/SKILL.md) when the main task is a product-journey comic rather than a standalone sketch.
