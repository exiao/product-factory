---
name: ad-creative
description: Create, review, and iterate paid ad copy and creative concepts using product truth and performance evidence. Use for ad variations, paid-social hooks, static concepts, creative testing, and review packages; use copywriting for landing pages and platform ad skills for campaign operations.
metadata:
  version: 1.0.0
---

# Ad creative

Turn a product, audience, offer, and evidence into testable ad creative: copy, static concepts, video briefs or scripts, and a review-ready package. Make the smallest useful assumption when inputs are missing and label it as a hypothesis. Never invent claims, statistics, testimonials, reviews, performance results, or customer language.

## Route the work

First identify the platform and placement, format, audience and funnel stage, product truth and offer, brand constraints, and the requested output. Separate three kinds of source material:

- **Supported**: product facts, claims, observed performance, or quotations with a traceable source and stated verification status. A supplied or approved claim is not automatically independently verified.
- **Illustrative**: a layout, placeholder, or example that is not presented as proof.
- **Hypothesis**: an angle or prediction to test, with the evidence and uncertainty stated.

Use the available evidence without making it a gate. If winning ads, reviews, comments, or performance data are absent, proceed from the product truth and clearly mark the angles as hypotheses. Replace an unsupported claim with a supported mechanism or omit it. Questions and hypothetical framing must not imply an unproven result; keep hypotheses in the brief, not disguised as proof in customer-facing copy.

Choose the working mode:

1. **Generate**: define 3–5 distinct reasons to click, then write multiple executions per angle.
2. **Iterate**: diagnose the funnel and compare winners, losers, placement, spend, and sample size before creating the next slate.
3. **Static batch**: use the structural formats in [creative-workflow.md](references/creative-workflow.md), cite the source or status of every claim, and include visual direction.
4. **Strategy / roadmap**: rank concepts by evidence, account state, production effort, risk, and capacity; turn selected concepts into briefs.
5. **Review package**: curate a small set for human selection and produce the self-contained review deliverable described in [creative-workflow.md](references/creative-workflow.md).

For an ad copy deliverable, use the installed `copywriting` skill when its offer and messaging guidance is useful; use `writer` when the user asks for Eric-authored voice. For a video script or visual treatment, use `video-script` or `video-direction`. Those skills own their specialties; this skill owns the performance-creative decision and evidence trail.

## AI-led creative

For Eric's AI-led ads, prioritize a concrete comic premise or useful explanation unless another direction is selected. Use [AI creative judgment](../content-factory/references/ai-creative-judgment.md) to test the payoff and authenticity. A fictional exaggeration can dramatize a real problem; invented customer testimony cannot supply proof. In narrative ads, make the product causally relevant to the setup, reveal, or resolution. Ask whether any unrelated logo could replace it unchanged. Repair a weak connection before producing variants. Surprise and reaction shots can support a joke, but shock, controversy, and generated spectacle are not objectives by themselves.

Source: [Lindy ad breakdown (2025-08-13)](https://pjace.beehiiv.com/p/steal-our-viral-ad-formula-that-got-us-100m-views-in-a-month-e7742bdae1e74b81) connects surprise, reactions, a product question, and a closing action. These are creator accounts, not controlled performance evidence. The comedy/education default and authenticity safeguards are Eric’s preference and our editorial synthesis, not findings proved by these posts.

User-selected taste reference: [slopject’s “iPhone Duo Performative Mode”](https://x.com/slopject/status/2097849527726190649). Both still images were inspected: a fictional outward-facing book-cover display turns literary status signaling into a product feature. The reusable lesson is a specific social observation expressed through one legible visual contradiction, with restrained copy. A compact still-image joke can be the whole result; do not force a video or full story arc. See [the analysis](../content-factory/references/ai-creative-judgment.md) for observation versus interpretation. Treat this as Eric’s selected creative standard, not conversion evidence.

## Copy and concept workflow

Build an angle matrix before filling slots. An angle should name the audience or situation, motivation, promise or tension, proof, and format—not merely say “UGC” or “benefit.” Useful angle families include pain, outcome, identity, comparison, objection/FAQ, mechanism, curiosity, founder/origin, and real urgency. Choose the families that fit the evidence and product rather than forcing all of them.

For each concept, record:

```text
angle; audience/stage; hook; primary text; headline; CTA;
format/placement; visual direction; source or claim status; test variable; risks
```

Vary one meaningful variable per test where possible: hook, proof, framing, format, or CTA. Remove near-duplicates. Make headlines and descriptions work independently when the platform combines them. Validate against the current platform specification before delivery; show character counts and provide a trimmed alternative for anything over the limit.

For performance iteration:

1. State the decision metric and placement scope.
2. Read the funnel (for example, thumb-stop or hold rate → click rate → conversion rate → cost/value), not just ROAS or a platform label.
3. Compare the strongest and weakest cohorts, including sample size and time window. Count a pattern in losers as well as winners before calling it durable.
4. Preserve what is working, vary the execution meaningfully, test a small number of new angles, and retire only with enough evidence or a clear policy/quality failure.
5. Deliver an iteration log: evidence reviewed, observed pattern, confidence/limits, concepts created, and the next decision.

## Visual generation and QA

Use the built-in image-generation tool for raster image generation or editing and follow the installed `image-generation-guide` skill. Save requested files in the current project, normally `output/images/`, or the user's chosen directory. Do not invoke an external provider by default; if the built-in tool is unavailable, report the blocker. An explicit user choice of another provider takes precedence. Preserve supplied logos and product assets. New code-native text layouts, UI, cards, and diagrams can use code/HTML; edits to existing raster images use the built-in image-editing tool unless the user explicitly requests another method.

Read [asset-qa.md](references/asset-qa.md) before approving or presenting generated assets. Inspect the actual pixels at full resolution and intended display size when visual inspection is available. Check the whole creative: subject and count, composition, legibility, crop, geometry, text fidelity, unwanted or irrelevant imagery, brand/policy triggers, and whether it is stronger than the incumbent. A render existing, clean spelling, or an automated PASS is not sufficient evidence. If pixels were not inspected, say so.

Apply the claim gate to every line and number: source, timeframe, denominator, qualifier, and destination must match the wording. Keep illustrative proof, dramatized dialogue, and hypotheses labeled. Apply the relevant platform and category policy without importing constraints from an unrelated category. A quality review can conclude that no asset is uploadable; still deliver the copy or recommendations that remain supportable.

## Delivery boundaries

Produce reviewable files and recommendations. Uploading, publishing, scheduling, spending, contacting people, or accepting terms must be within the user's authorization; preserve authorization already given. A skill invocation alone does not authorize those actions. When a visual review page helps, use the format in the reference: a local HTML page with a small curated set, platform mockups or frame storyboards, copy variants, and an honest grounding disclosure. Honor a requested text or document format. Keep source paths relative and do not claim the page was hosted or viewed unless it was.
