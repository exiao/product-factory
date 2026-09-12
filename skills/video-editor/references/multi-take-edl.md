# Multi-take EDL

An edit decision list keeps take selection reviewable and reproducible:

```json
{
  "fps": 24,
  "output": "final.mp4",
  "scenes": [
    {"scene": 1, "clip": "take03.mp4", "start": 1.89, "end": 12.40,
     "rationale": "Complete line, clean start, no filler, good eyeline."}
  ]
}
```

Transcribe or review each take, choose on complete performance and continuity rather than assuming the last take is best, cut in silence when possible, and record why incomplete or noisy candidates were rejected. Render each selection with frame-accurate encoding, concatenate in scene order, then re-check the result's transcript, timing, joins, and full decode. Fix the EDL and re-render when verification fails; keep the previous cut for comparison.
