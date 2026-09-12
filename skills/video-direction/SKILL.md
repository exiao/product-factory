---
name: video-direction
description: Develop video visual treatments, shot lists, camera and lighting plans, blocking, visual continuity, generation prompts, and take selection. Use for visual concepts and directing an existing scene or script; narrative and spoken-copy writing belong to video-script.
---

# Video direction

## Still-image generation

For generated or edited still images, use [$image-generation-guide](../image-generation-guide/SKILL.md): Codex built-in image generation, verified files saved in the local project. This applies to reference sheets and intermediate assets as well as final images. Keep this skill's creative requirements; do not automatically use provider CLIs, external generation plugins, or remote rendering services. An explicit user request for another provider takes precedence.

Direction is model independent. Own visual treatment, shot breakdown, camera, lighting, blocking, visual continuity, generation prompts, and take selection. For a narrow prompt or shot revision, deliver only that direction; do not require a script first. Use [$video-script](../video-script/SKILL.md) when narrative or spoken-copy work is also requested. For a finished-video request, use the applicable production workflow, drawing on direction as needed.

When a script exists, add stable shot IDs beneath its scene IDs in the same production document. A scene may contain several shots. Scene sections remain authoritative for spoken copy; shot records reference the relevant lines rather than maintaining another editable copy. Preserve approved story, dialogue, caption text, and essential visual beats. Flag timing conflicts and propose adjustments instead of silently rewriting approved copy. If copy changes are authorized, update the scene text and affected shot references together.

Put the visual treatment at the top and repeat its useful style constraints in each shot. For production handoffs, record relevant framing, movement, action, environment, lighting, duration, sound cues, references, continuity, and acceptance notes. Omit fields that add no useful direction. For direction-only work, a compact shot list is sufficient. When handing work to another maker or reviewer, use the assignment requirements in [production coordination](references/production-coordination.md), even if no separate role is needed. Put them in the existing production document or assignment rather than creating a second template.

Reuse supplied references and prepare additional product, character, location, prop, or spatial references only when needed for continuity or an authorized generation task. Compare alternatives with one variable changed at a time and keep the strongest candidates until motion proves which one holds. Prepare separate references for deliberate mid-scene changes. A short generated shot is usually safer than asking one generation to carry a long sequence; join separate clips in post.

For generated sequences, establish a few distinctive anchor frames, character references, and spatial relationships before filling coverage. Test a representative frame in motion before expanding the look; a beautiful still may animate poorly. Keep direction specific through chosen materials, light, props, and behavior rather than generic cinematic adjectives. Use shared frames or small angle groups when they help continuity, checking face detail and composition at delivery size. Treat grid sizes, upscalers, model rankings, and long-versus-short shot preferences as workload-dependent choices to verify, not permanent rules from a tutorial. Preserve pacing, reactions, and breathing room for performance. Read [AI creative judgment](../content-factory/references/ai-creative-judgment.md) when synthetic realism or story credibility is at issue.

Sources: [Patchwright workflow (2026-05-13)](https://pjace.beehiiv.com/p/gossip-goblin-s-crazy-workflow-for-building-original-worlds-200m-views) discusses anchor images and distinctive world details; [Hellgrind and Mork workflow (2026-04-25)](https://pjace.beehiiv.com/p/you-re-using-seedance-2-0-wrong-try-this-massive-time-saver-instead) discusses motion trials and spatial continuity; [four-shot reference workflow (2026-01-09)](https://pjace.beehiiv.com/p/i-regret-nothing-except-reading-the-comments) offers a dated small-grid technique. These are dated production accounts, not universal tool benchmarks; verify techniques on the actual output.

Write prompts as temporal action, not a pile of adjectives. Lead with camera and lens, then subject/action, environment, real light sources, tactile texture, color, mood, and beginning/middle/end motion. Describe the physical actions that matter; avoid overconstraining incidental motion. Generate text, logos, UI, and subtitles in post because video models commonly render them unreliably.

This skill plans and reviews direction. It may use an available media-generation capability when the user requests generation and the relevant tool is present, but it must not invent a provider CLI, install a global tool, spend credits, publish, or submit a paid generation outside the user's scope. If no generation capability is available, return the complete shot list and prompts for handoff. Review the actual media before calling a take good; inspect motion, identity, continuity, audio, and the intended cut.

Read [references/shot-list-workflow.md](references/shot-list-workflow.md) for the canonical shot-list fields and revision loop, and [references/prompting.md](references/prompting.md) for compact prompt language.
For short-form openings, read [references/short-form-first-frame.md](references/short-form-first-frame.md) to direct the first visual action alongside the spoken hook.

## Optional production roles

For a substantial production or a request for separate story, creative, and technical reviews, use [production coordination](references/production-coordination.md). Keep direction and canonical-document ownership in the main task. Load only the role briefs needed for a bounded assignment; they are not mandatory stages or separately configured agents. A small edit can use [$video-editor](../video-editor/SKILL.md) directly, and prose critique belongs with [$evaluate-content](../evaluate-content/SKILL.md).
