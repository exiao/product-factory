# Creative workflow reference

Read this reference for roadmap work, performance iteration, static batches, or a stakeholder review package.

## Evidence-ranked strategy

Treat a concept as a testable hypothesis: `segment × motivation × angle × format`, with a receipt. Rank evidence by what is actually available:

1. Converting account creative with the same angle or segment.
2. Recurring customer, support, or sales language.
3. Traceable competitor or category patterns supplied by the user.
4. Organic engagement or qualitative demand signals.
5. An adjacent-category pattern.
6. A team hunch.

The ranking sets priority, not production fidelity. Keep a low-fidelity test cheap until it earns a funnel signal. If the account is exploratory, go broad across segments and motivations. If it is scaling, make visually distinct variations of proven concepts, probe sub-angles, and reserve a smaller lane for new bets so fatigue does not empty the pipeline.

Maintain three horizons when a roadmap is useful:

```text
Icebox: every concept with evidence and source
Next period: the few themes chosen and why now
Current slate: concept | evidence | production effort | owner | status | metric
```

Check real capacity before committing a slate. A retro should record winners and losers, where each concept died in the funnel, metric-specific wins, uncertainty, and the resulting re-rank, revision, or kill. Do not turn a thin sample or a platform quality label into a causal claim.

## Static concept formats

Use structural variety to create angle variety. Pick formats that fit the evidence and placement; do not force a fixed count or pretend a format is proven. Useful families include:

- headline statement or product hero;
- problem → solution;
- before → after (only when the transformation claim is supportable);
- review or testimonial card (real quote and permission/status required);
- stat or data callout (source, date, denominator, and timeframe visible in the brief);
- FAQ / objection card;
- feature or ingredient spotlight;
- comparison or “old way vs. new way” (factual, substantiable, and policy-checked);
- founder/origin note;
- numbered reasons or checklist;
- press mention (real coverage and permitted logo use);
- lifestyle or product-in-use hero;
- chat, notes, or app-screen mockup (build text and geometry deterministically where possible).

Every concept has this minimum record:

```markdown
## Concept: [name]
**Angle / audience / stage:**
**Hook:**
**Headline / primary text / CTA:**
**Format and placement:** [include intended ratio or dimensions when known]
**Visual direction:** [composition, subject, text hierarchy, and crop]
**Grounding:** [source, exact quote/field, or "hypothesis — no direct source supplied"]
**Claim status and risks:** [verified / illustrative / hypothesis; policy or proof notes]
**Test variable and success metric:**
```

For scaled batches, add an `INDEX.md` with one line per concept and its grounding status. Keep the per-concept files as the audit trail. Use current platform documentation or supplied specs for exact character and asset limits; do not rely on stale remembered limits.

## Review deliverable

Create a self-contained HTML review page when a stakeholder needs to choose among concepts or a slate review needs a visual decision surface. Curate roughly 2–4 concepts. Store a strict JSON data block and render it with inline CSS/JS so the file can be opened locally without a build or network dependency.

Each concept should expose a name, one-line distinction, one or more frames, selectable headline variants, primary text, CTA/destination if supplied, and a required `grounding` disclosure. A frame label names its narrative job (`Hook`, `Problem`, `Proof`, `Ask`), not just what is pictured. If an image is absent, show a labeled placeholder with the visual prompt; do not imply it is rendered. Escape `</script>`-like text when embedding JSON, keep image paths relative, and validate that the page loads before claiming it was reviewed. Do not host or distribute the page automatically.
