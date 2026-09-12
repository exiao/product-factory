# Typed captions

For a character-by-character reveal, render one transparent caption frame per video frame and composite it as one image-sequence input. Toggling one overlay per line only shows or hides whole lines; it cannot type within a line. Use a fixed characters-per-second rate capped by a fraction of the spoken duration, blink a cursor only on the active line, and drop it when the line completes.

Derive caption timing from measured audio durations rather than hardcoded script timestamps. Add a scrim and text shadow for readability, cap the number of accumulated rows, and keep the block clear of faces. Verify adjacent frames in the caption band: the text should grow by a few characters per frame, not appear complete at once or remain unchanged.
