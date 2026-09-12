# Measure a reference

When the reference is available locally, use `ffprobe` for dimensions, frame rate, streams, and duration. Use scene-change detection for approximate cut timestamps, compute cuts per minute as cut count times 60 divided by duration in seconds, and make a contact sheet to count locations, wardrobe changes, black cards, and caption placement. Sample frames to inspect typography, caption color, and whether captions appear as whole lines or reveal over time. Treat crop failures as probe failures and widen the crop before drawing conclusions.

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=width,height,r_frame_rate,duration -of default=nw=1 ref.mp4
ffmpeg -i ref.mp4 -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1
ffmpeg -i ref.mp4 -vf "select='not(mod(n,45))',scale=240:-1,tile=6x5" -frames:v 1 contact.jpg
```

Report numbers first: aspect ratio, duration, cuts per minute, locations, caption placement and treatment, and audio shape. Then state the rebuild's measured matches and gaps. Do not download a remote reference unless the user requested that retrieval and the required tool is available.
