# Generate, run, inspect, revise

Use this workflow for a new eval idea or small comparison suite. The purpose is to find whether both the answers and the measurement match the intended outcome.

## Choose the runner

| Work being measured | Starting point | Tradeoff |
| --- | --- | --- |
| Simulated interaction | Existing conversation runner with a bounded user simulator | Retain full turns and scenario state; account for simulator cost, timing, and variation |
| Tool use, files, services, multi-step state changes | Harbor when its environments fit | Repeatable isolation and lifecycle; runtime setup and container overhead |
| Existing production agent/runner | Reuse its safe test entrypoint and captured fixtures | Better behavioral fidelity; record what remains live or uncontrolled |

Choose agentic evaluation or simulated interaction from the task without asking the user to select a type. An agentic environment can use frozen input files, relevant tools/skills, and model configuration; add isolation only when it helps reproduce the work. A local simulation is not evidence about live services. Use the Harbor reference only when Harbor is selected.

## Produce the whole pilot

Use the declared plan: one or multiple models, prompts, tools, and skills, varying only factors relevant to the question. One case or configuration is valid; add cases to exercise distinct behavior. State reasonable finite defaults and run subscription CLI jobs and already authorized API jobs without a confirmation step. Follow the main skill's explicit-confirmation requirement for API spending. Use real examples when supplied; otherwise label generated examples and their assumed audience/context. Include a successful ordinary case and meaningful failure/edge cases.

Separate these responsibilities, using existing project conventions instead of imposing filenames:

- **Tasks/inputs:** case ID, user prompt, audience/context, source artifacts, condition, provenance, and dataset version.
- **Answer key/rubric:** required facts/actions, acceptable alternatives, forbidden errors, subjective anchors, labels and their evidence. Exact reference wording is optional; for decisions, a defensible alternative can be valid even when it differs from a historical choice.
- **Environment/runner:** frozen inputs, available tools, model/provider settings, fresh context/reset, bounded run configuration and errors. Use identical task inputs across models within a condition; record unavoidable adapter differences.
- **Raw outputs:** complete response or produced artifacts and relevant tool trace, case/run/model IDs, request configuration, timing and usage when available. Never substitute summary text or fabricated samples for an executed response.
- **Grading:** per-criterion verdict/score, evidence from output, rationale, evaluator version, and separate execution/evaluator errors. Machine checks and subjective judgments retain separate identities.
- **Results:** quality, attributable cost, and measured time per case/run/configuration, with errors and retries visible; charts and data rows link to outputs, traces, and grading evidence.

State which dimensions are measured and excluded: fact coverage, factual correctness, style, and decision quality are different claims. A coverage judge is not a truth verifier.

Keep generation, grading, and reporting independently rerunnable. Save raw responses before grading so rejudging does not regenerate answers. Save revised grades as a new version; retain the original. Unknown costs are unknown, and unfinished/failed runs stay visible rather than improving a leaderboard by disappearing.

## Keep results visual and inspectable

Lead with quality, cost, and time. Use charts or a compact table suited to the actual observations: configuration comparisons, per-case scores/cost/duration, or a single-run timeline. Show sample counts and missing measurements. Avoid unsupported rankings or distribution plots with insufficient samples. Keep quality criteria and critical failures inspectable; use only declared weights for aggregate scores.

Keep subject/tool cost and execution time separate from simulator, grading, and overall experiment overhead. Include retries and failed attempts. Unknown cost is not zero; label cost calculated from usage and rates. Evaluate agreed quality/cost/time targets explicitly and otherwise show tradeoffs without invented thresholds.

Favor charts and raw data over explanatory scaffolding. Provide direct access from a point or row to the full prompt, tested model/prompt/tool/skill configuration, answer or artifact, conversation and tool trace, criterion results and rationale, usage, and timing. Offer raw JSON/CSV downloads. Add filters or sorting only when useful; a static chart with linked records is sufficient for small results. Do not force a one-case-at-a-time review or build decorative dashboards.

Use the evaluator declared in the pre-run plan, preserving any explicit user selection. Identify deterministic rules separately and preserve evaluator labels and old grades with their evaluator versions. Human ratings stay unreviewed until the user responds; persist any submitted rating against its case/run/criterion/version. A configuration selector must not imply grading ran unless it actually did.

Verify chart/table values against raw records and exercise any filtering, drill-down, persistence, or export controls provided. Keep the opening view short and make evidence easy to reach.

## Learn from disagreement

Classify supported problems as subject failure, bad/ambiguous task, unrealistic environment, incorrect/incomplete key, grader false positive/negative, or unresolved preference. Repair the responsible artifact. Do not automatically rewrite the subject's skill because it disagreed with a synthetic reference answer.

Test pairs that should order correctly for the intended goal: useful/complete versus polished-but-empty, precise for the declared audience versus oversimplified, compliant alternative versus exact-reference wording. For a metric that rewards brevity, keep completeness observable. Do not import readability-specific weights, banned words, or pass thresholds into unrelated domains.

After rubric/scorer changes, recalibrate and regrade the same saved outputs under a new version. If task inputs, environment, or subject instructions changed, create a new condition and regenerate affected outputs. Compare only matched case sets and compatible conditions/evaluator versions; equal sample counts alone do not establish comparability. Label tiny runs as pilots and do not invent a universal significance threshold.

Reviewed cases inform development. Use fresh held-out cases before claiming generalization after tuning against feedback. An AI-generated pilot can reveal useful disagreements; it cannot independently prove that its own criteria capture the user's judgment.

## Design reference

Inspired by [readability-eval](https://github.com/exiao/readability-eval), inspected 2026-09-09: its [methodology](https://github.com/exiao/readability-eval/blob/main/METHODOLOGY.md) describes fact coverage, controls, condition separation, and rejudging saved answers. Reuse those experiment patterns, not its domain-specific scoring or published rankings. The screenshot's model names, counts, and scores are illustrative, not evidence or a prescribed run budget.
