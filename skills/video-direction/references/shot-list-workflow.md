# Shot-list workflow

Keep one canonical production document. When a script exists, preserve its scene sections and add shot records beneath them. Scene text owns dialogue and narration; shots reference scene/line IDs. Use stable shot IDs such as SC01-SH01 and SC01-SH02 for multiple shots within SC01. A direction-only request can use shot IDs without inventing a script. Start with three treatment adjectives, each tied to an observable test for image, movement, or sound. Record a few visual directions with strengths and trade-offs, then lock the chosen direction. For each shot, separate essential details from flexible details so a useful surprise is accepted without losing story, identity, dialogue, framing, or continuity.

Recommended fields:

```text
shot_id, scene_id_if_present, purpose, essential_details, flexible_details,
framing_and_camera, action_and_performance, duration_target,
edit_join, spoken_line_refs, sound_cues, references, continuity_in,
continuity_out, prompt, candidate_takes, selected_take,
measured_duration, edit_range, notes
```

Treat the flow as treatment -> scene changes -> shot list -> references -> generation or capture -> assembly with sound -> review -> targeted revision. Preserve prior cuts and update only failed shot IDs or ranges. A changed duration updates downstream offsets. Distinguish estimated duration from measured take or edit duration. If the planned shots cannot accommodate approved spoken copy, identify the affected scene and propose a timing or copy adjustment; do not silently change the copy. After an authorized revision, update scene timing and dependent shot references together. A deterministic fixture can prove IDs and assembly plumbing, but cannot prove identity, acting, artistic quality, or intelligibility.
