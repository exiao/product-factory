# Composition and asset sets

## Products and branding

Use supplied product and official brand assets as truth. Preserve packaging shape, proportions, material, label text, marks, colors, and recognizable features. Separate an exact packshot from a lifestyle scene, a person using the product, a virtual try-on, or a deliberately conceptual treatment. A conceptual effect must not accidentally change the product itself.

Brief a camera angle, grounded perspective, contact shadow, light direction, background, and crop that make the product readable. For worn or held products, check scale, grip, occlusion, fit, and body geometry. For a hero banner, reserve the requested text region and inspect desktop and mobile crops. Do not fabricate labels, ingredients, prices, endorsements, or product benefits.

Preserve official vector marks with deterministic placement when exactness is required rather than regenerating them. Generated typography can be useful for pictorial designs, but editable or compliance-critical copy usually belongs in a separate text layer. Follow the user's requested format.

## Text and thumbnails

For edits to app screenshots, labels, or other factual text, first transcribe the source words, values, and claims into a ground-truth checklist. Specify exact words and placement, keep copy short where possible, and check the generated result against that checklist; plausible replacement text is still a defect. Preserve a good render before an edit: fixing one word can damage others. If text corruption accumulates, restart from the clean source with the required corrections together rather than treating a degraded edit as the new truth. Use a focused image edit when appropriate; if repeated corrections fail or precise editable text is required, keep the image and compose the text separately using an authorized suitable method. A single historical failure does not justify banning all text edits.

When useful references exist, compare a draft alongside them at the same crop and display size; name the visual feature being compared rather than treating popularity as proof of causation. For thumbnails, make the subject, visual tension, and focal point readable at small size. Use authentic expressions and contrast appropriate to the concept, not a mandatory shouting face or unsupported performance claim. Compare requested variants at the same display size. Verify current platform requirements when export or upload depends on them.

## Illustrations, storyboards, and UI assets

Carry the selected style through palette, line weight, texture, perspective, and character proportions. A named notebook style belongs to the notebook-sketch skill; product-story narrative belongs to storyboards. Use these specialist briefs without inventing extra panels or style changes.

For explanatory imagery, show the mechanism: what changed, why, and what action causes the result. A metaphor should carry the source facts, not just decorate a status message. Keep real labels and factual relationships traceable to the input; do not let generation re-decide what happened.

For a sequence, lock shared identity/style constraints and vary only the scene-specific action or content. Verify panel order, counts, spatial relationships, and readable captions. A polished depiction of a proposed product outcome remains hypothetical, not research evidence.

For a UI comp, describe the screen's regions and relative scale before its atmosphere so the result represents a usable layout rather than a poster. Generate pictorial assets separately for implementation; do not ship rasterized interactive controls or inaccessible body text as the interface.

## Batches

Choose one concrete value per variant instead of an unresolved menu of poses or backgrounds. Keep shared invariants in a reusable brief, with explicit per-image variables and stable filenames. Retain the reason for rejected concepts and exclude that rejected visual family from subsequent variants unless the user deliberately reopens it; changing colors or copy does not fix the same rejected concept. Use a contact sheet when it helps compare identity, crop, product fidelity, and style across a real set. Do not require a batch framework or additional variants for a single-image request.

## Transparent assets and delivery crops

Request a transparent background through the built-in tool when needed. Verify an actual alpha channel and inspect edges against both light and dark backgrounds: hair, pale borders, thin parts, and soft shadows should not disappear or acquire a matte halo. A checkerboard drawn into opaque pixels is not transparency. Deliver the checked final cutout, not an earlier solid-background render. Use a focused built-in image edit for corrections; do not silently install a background-removal model or substitute an external service.

For stickers or flat cards that must sit square, specify upright orientation and no perspective skew; tilted art remains valid when requested. Leave padding for the actual placement, platform overlays, and crop. Check important faces, marks, text, and borders against the intended display area instead of assuming a universal safe-zone percentage.

When exact dimensions or aspect ratio are required, a mismatch fails the export check even if the image looks good. Preserve proportions: crop to the required aspect before scaling only when the crop preserves required content and is within the brief. Otherwise revise the framing or report the mismatch; never stretch the image or silently cut off required text, faces, or product details. Follow the current image-tool rules for any corrective edit.
