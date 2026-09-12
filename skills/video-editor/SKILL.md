---
name: video-editor
description: "Edit and assemble video with available local media tools such as ffmpeg: trim, concat, overlays, transitions, speed, crop, scale, captions, audio mixing, normalization, GIFs, and edit decision lists."
---

# Video editor

Editing and rendering are execution work. Confirm the input files, output path, available tools, and requested deliverable before changing media. Check `command -v ffmpeg` and `ffprobe -version`; inspect each input with `ffprobe` for duration, streams, codec, resolution, frame rate, and audio channels. Keep source files and prior cuts intact, write outputs to an explicit project directory, and preview a short segment before a long render.

Use frame-accurate re-encoding when cuts must land precisely; stream copy is appropriate only when keyframe and codec constraints are acceptable. For mixed inputs, normalize resolution, frame rate, pixel format, and audio layout before concat. For captions, logos, and UI, composite them in post. For audio, measure real voice durations, duck music under speech, normalize to the requested loudness, and verify sync at several timestamps.

For multi-take edits, create a reviewable JSON EDL with source take, in/out seconds, scene ID, and rationale. Select on performance, clean starts/ends, continuity, and intelligibility. Re-render from the EDL instead of making opaque manual changes. After rendering, verify full decode, duration, stream presence, frame samples, audio levels, and any requested caption or transition behavior. Decode proves file integrity; it does not prove artistic quality, pacing, emotion, or lip sync, so label those judgments separately.

For AI-generated sequences, assemble representative shots early so continuity and performance problems are found before more generation. Cut for setup, reaction, consequence, and payoff; do not force quick cuts where a held moment carries the scene. Unify voices, room tone, sound perspective, and color across separately generated clips. Test texture, grain, and upscaling on the actual output; they can damage detail and do not repair weak story or acting. Mark the precise missing reaction, insert, transition, or audio beat for the production workflow when an edit cannot resolve it. See [AI creative judgment](../content-factory/references/ai-creative-judgment.md) for audience-payoff and authenticity checks.

Sources: [Mork editing workflow (2026-04-25)](https://pjace.beehiiv.com/p/you-re-using-seedance-2-0-wrong-try-this-massive-time-saver-instead) describes bringing shots into the timeline during generation; [Patchwright interview (2026-05-13)](https://pjace.beehiiv.com/p/gossip-goblin-s-crazy-workflow-for-building-original-worlds-200m-views) discusses editorial cohesion, sound, and avoiding damaging upscaling. These are dated production accounts, not universal tool benchmarks; verify techniques on the actual output.

This skill may execute local editing commands when the user asks for an edit. It does not generate footage, buy media, publish, or send the output externally unless that scope is explicitly included. Read [references/recipes.md](references/recipes.md) for common filter chains and [references/multi-take-edl.md](references/multi-take-edl.md) for auditable take selection.
