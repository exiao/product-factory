# Asset and claim QA

Use this gate before an ad asset or copy set is called ready for review or upload.

## Visual gate

First establish the comparison: an incumbent winner, a supplied brief, or a stated hypothesis when no benchmark exists. Then inspect the actual asset, at its intended feed size and full resolution where possible.

Check:

- the intended subject, product, action, and object count are present;
- the composition gives the hook and product enough visual weight and survives the placement crop;
- all text is legible, correctly spelled, inside the canvas, and not obscured by faces, hands, UI, or safe-area overlays;
- device frames, chat bubbles, cards, borders, corners, and repeated containers are geometrically consistent, with no phantom blank row or clipped line;
- no prompt/instruction words (`only:`, `exactly`, `label:`) appear as content, and every line could plausibly have been written by a person;
- the scene is relevant to the message, brand-safe for the stated category, and free of unlicensed logos, watermarks, or recognizable people unless supplied and authorized;
- there are no invented product details, fake testimonials, fabricated reviews, or policy-sensitive words that the brief cannot support;
- the asset is meaningfully better or differently useful than the benchmark. If it is merely polished and generic, reject or revise the concept.

If any material check cannot be observed, mark it unverified. Do not infer pixel quality from a filename, prompt, metadata, or tool-generated rating. For new code-native typography, UI, chat, notes, and card layouts, consider HTML and inspect the rendered result. For edits to a supplied or generated raster image, use the built-in image-editing tool unless the user explicitly requests another method. Do not silently switch a requested image edit into a different deliverable.

## Copy and claim gate

For each candidate line, count against the current placement spec, remove duplicates, and classify the line as headline, description, primary text, or body. Check that the CTA and destination can deliver what the ad promises.

For each factual statement or number, record:

```text
source → source field or exact quote → timeframe/denominator → ad wording
```

The source proves that a value exists; it does not prove that the value means the timeframe in the sentence. Re-check sibling fields such as daily, weekly, monthly, year-to-date, and annual values. Apply the relevant category policy to the words and the visual together. Do not let a high CTR, a thin sample, or a platform “best” label overrule an unsupported or misleading claim.

Keep separate verdicts for copy, visual, and upload readiness. A creative can have strong copy but fail visual QA, or pass visual QA while having an unsupported claim. Report the exact failing check and the smallest repair. If no asset passes, say that no assets are uploadable from the run and include the surviving recommendations; do not attach an unreviewed asset or add an upload CTA.

## Image-generation operating rule

For raster generation/editing, use the built-in image-generation tool and the installed `image-generation-guide`. Write a concrete brief covering purpose/format, subject/action, composition, light/material, reference roles, what to preserve/change, exact text, and observed failures to avoid. Generate one useful draft, then revise only observed defects; preserve the source render and verify the saved file opens, dimensions, format, crop, and display-size readability. Do not use an external provider by default. Report a missing built-in tool as a blocker; honor an explicit user provider choice. Do not claim identity preservation or production readiness without inspection.
