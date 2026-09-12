# Editing recipes

Use fresh output filenames; do not overwrite source media or prior cuts. These recipes assume the named input streams exist; check them first:

```bash
ffprobe -v error -print_format json -show_format -show_streams input.mp4
```

For a simple edit, trim to working ranges, normalize dimensions and frame rate, assemble with concat or a filter graph, then add graphics and audio in separate stages. Use a short preview for filter debugging.

```bash
ffmpeg -n -ss 00:00:10 -to 00:00:25 -i input.mp4 -c:v libx264 -c:a aac trim.mp4
ffmpeg -n -i trim.mp4 -i music.wav -filter_complex \
  "[1:a]volume=0.18[m];[0:a][m]amix=inputs=2:duration=first:dropout_transition=2[a]" \
  -map 0:v -map '[a]' -c:v copy -c:a aac output.mp4
```

For captions over busy footage, add a translucent scrim, draw a shadow before the colored glyphs, keep the block in the lower third, and cap accumulated lines. For voice plus music, sidechain or automate music volume under speech, then check loudness and sample RMS at several timestamps. For a product demo, remove setup, accelerate repetitive navigation, preserve the important gesture, add the real screen capture, and verify that the result still shows the claimed action.
