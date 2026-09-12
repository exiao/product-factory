# Portable artifact patterns

## Variants

Expose only meaningful decision variables: layout, density, typography, a flow choice, or copy variant. Keep the control panel small and label options by their real difference. Use ordinary state and, when persistence helps, namespaced localStorage with a reset control. Handle unavailable storage gracefully. Saving browser state does not write source files or change the selected implementation by itself.

For a revised final artifact, put the selected defaults in the source. Avoid unsupported `window.parent.postMessage` host protocols and hidden runtime bridges. Browser-only AI demos need a real authorized backend or explicitly simulated outputs; never embed provider secrets in shipped HTML.

## Deck and motion geometry

Use one-based slide labels matching the visible counter. Add keyboard navigation and accessible play/pause where relevant. Restore slide/time position when useful for iterative review, but give users a clear restart option. Include speaker notes when requested and make sure the chosen deliverable actually supports them.

For a fixed-size slide stage, scale to fit the available viewport without clipping. One reliable method positions the unscaled stage at 50%/50%, centers it with negative half-width/half-height margins, then applies only scale with a centered transform origin. A wrapper with measured dimensions is another option. Measure bounds after scaling; do not assume a particular centering technique always fails. Initialize custom-element children after parsing, or observe changes, to avoid an empty slide count.

Use a timeline/scrubber for a motion study when it helps review the requested animation. Interactive prototypes can often use simple state and CSS transitions. Avoid adding an unnecessary framework or fixed historical CDN versions.

## Verification and delivery

Verify the artifact in its actual delivery mode. Multi-file prototypes may need a local server; standalone files must include or package their dependencies. Check loading, navigation, viewport fit, assets, text overflow, and representative interactive states. Keep presentation controls out of exports. An HTML motion study is not an exported video until rendering creates and verifies a video file.
