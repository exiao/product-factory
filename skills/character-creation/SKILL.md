---
name: character-creation
description: Create reusable fictional character identities and reference assets for a video series, including appearance, personality, speech, and voice direction. Use for character consistency across episodes.
---

# Character creation

## Still-image generation

For generated or edited still images, use [$image-generation-guide](../image-generation-guide/SKILL.md): Codex built-in image generation, verified files saved in the local project. This applies to reference sheets and intermediate assets as well as final images. Keep this skill's creative requirements; do not automatically use provider CLIs, external generation plugins, or remote rendering services. An explicit user request for another provider takes precedence.

Reuse an existing series character when its identity fits. A new episode or platform does not by itself require a new character. Read supplied references and preserve approved identity decisions.

Define only the fields needed for the project: name and stable slug, audience/platform, role or niche, personality, speech style, voice qualities, visual style, appearance, and recurring costume or setting. Distinguish immutable identity traits from episode-specific expression, pose, and wardrobe.

Store reusable character material in the user's requested project directory, such as `characters/<slug>/`. Keep a compact config with relative asset paths, character description, approved reference version, and voice provider/ID only when actually selected. Do not store credentials. A prose character brief does not require image or audio generation.

When visual assets are requested, use the available image-generation capability and supplied references. Start with a useful draft, refine the selected look through reference-based edits, and deliver the resolutions/aspect ratios the downstream pipeline actually needs. A portrait and neutral face reference can serve different purposes; do not require two redundant images for every project. Never invent local image paths or claim assets were generated when only prompts exist.

Test consistency across representative expressions, angles, and lighting when repeated generation is part of the task. Compare facial structure, distinctive details, silhouette, costume continuity, and small-screen readability. Preserve approved reference files; version replacements. A prompt asking for identical features is not proof of identity consistency.

For high-volume series, consider a broader reference set or character training only after reference-based editing shows a real limitation. No fixed post count, image quota, or training purchase is required. Fit the voice to the character through actual audition when possible; voice description alone does not establish an audio match. Get consent for cloning a real person's voice.

Hand off the character brief/config, existing asset paths, selected voice details, allowed variations, and unresolved consistency limits to scripting and video production. Creating a character does not authorize account creation, posting, or additional paid training.
