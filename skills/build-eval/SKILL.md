---
name: build-eval
description: "Turn real work, local agent sessions, or traces.com traces into replayable evaluations, including Harbor tasks for a specified environment. Compare models, harnesses, skills, knowledge, history, and environments on quality, cost, and time. Use for eval creation and agent experiments."
---

# Build an eval

Build a bounded local evaluation of real work. Start with the user's task and standard of good work, exercise the relevant agent, save complete evidence, and report quality, cost, and time separately. For a focused case, grader, or review change, do only the work that change needs.

The [Bloom worked example](references/bloom-worked-example.md) shows this workflow on an existing application, including rejected candidates and unresolved failures. Its investing rubric, model choices, counts, and spending authorization are examples, not defaults for other tasks.

## Start with the task and its runtime

Inspect the current conversation, source records, accepted outputs, follow-up corrections, and existing runner before asking the user to reconstruct context. Identify the repeating task, normal inputs and available context, expected output or action, forbidden actions, and evidence of success. Keep ordinary successes and legitimate no-action cases alongside observed failures. A targeted failure search does not estimate production failure rates.

For an existing application, use its actual safe test entry point and authorized provider path, including tools, context, retries, and fallbacks. Do not replace it with standalone CLI Q&A to satisfy a routing preference. A CLI adapter is appropriate only if it preserves the behavior being measured; disclose differences. Use agentic execution for work requiring actions and simulated interaction for conversational behavior. A single prompt can start an agentic task; artificial tool calls are unnecessary.

For standalone subjects, simulators, separate judges, analysis, and retries, prefer the user's existing Claude or ChatGPT subscription through the local CLI when it supports the selected task and model. Check CLI help, login status, effective settings, and returned identity. Remove API/proxy overrides only in the child environment while preserving subscription authentication. Do not change global configuration or silently substitute a model when a route fails. A remote CLI is not offline execution.

API spending, including TypeSafe/Jev, OpenRouter, direct APIs, and paid proxies, needs explicit authorization for the service and scope; reuse authorization already given, including a standing task budget, without asking again. A configured key or automatic fallback is not approval. Preserve approved application routing rather than stripping its credentials to force subscription use. Respect confidentiality, disclose external transmission of source material, and keep secrets out of fixtures and reports.

## State one compact plan

Specify the task, runtime, cases, configurations, fixed and varied factors, evaluator, quality criteria, repetitions, attempt policy, cost/time measurement, and finite limits including calibration and repair retries. Choose reasonable defaults and proceed within existing authorization. Missing preferred budgets or human labels do not require approval; a bounded pilot can use clearly labeled provisional judgments. Ask only when missing facts prevent a meaningful task or required authorization is absent.

Distinguish adjustable batch estimates from hard call, token, time, or money caps before starting. Adapt batches within those caps. Do not extend a declared hard cap merely because money remains or a candidate almost passes; stop and report the best supported result unless the user authorizes an extension. Record changed limits before further execution.

Version the case contract, run configuration, environment, and evaluator separately. Record material hashes and how settings reach the agent. Compare one factor at a time to attribute effects; label combined changes as configuration comparisons. Avoid unnecessary cross-products. Explain the business outcome the task supports without claiming benchmark gains prove business impact.

## Define success from the user's standard

Reuse agreed criteria and examples. Combine a small shared rubric with case-specific requirements. Clarity, utility, and accuracy worked for Bloom; choose dimensions appropriate to this task. Label AI-proposed rubrics and invented cases as proposals. Accept defensible alternatives instead of requiring reference wording, an identical tool sequence, or one preferred conclusion.

Give each criterion inspectable evidence. Separate factual errors, incomplete answers, format violations, forbidden actions, retrieval failures, and evaluator errors. Both a word-limit miss and a reversed financial comparison may fail their requirements, but retain their different significance. Define critical gates before running; good style cannot offset a critical failure. Do not invent format rules or thresholds, or relax a criterion after seeing a candidate's answer.

Use deterministic checks for directly observable constraints such as word/bullet counts, structured allocation totals, forbidden calls, or citation-URL presence. URL presence does not prove source support, and matching a number somewhere in a payload does not establish its entity, metric, units, period, or comparison direction. Use evidence-grounded judgment for those claims. Verify actions and persistence at their real boundary, not from an assistant's statement that it acted.

Keep subject, simulator, reviewer, and scoring software distinct. Honor the user's chosen evaluator. The current assistant can review complete saved attempts when requested or suitable for a provisional pilot; no additional judge call is required. Record its criterion-level verdicts, evidence pointers, and reasons. Disclose when it also authored candidates or saw their identities; do not label its grades human-reviewed or blind. Keep human ratings unreviewed until a human supplies them. Do not silently replace an explicit evaluator.

For subjective comparisons, consider blinded pairs with randomized order, ties, and a separate indication that neither answer meets requirements. Calibrate against independently reviewed labels when available. A preferred answer can still fail an absolute requirement, and agreement between AI-written labels and an AI judge is provisional.

## Verify the measurement before expanding

Use [evaluation readiness](references/evaluation-readiness.md) on the actual case file, runner, evaluator input, persistence path, and report. Reuse checks already verified for unchanged versions. Start with a representative trial and meaningful good, bad, and missing-output controls. A no-op is not a negative control when abstention is correct.

Freeze task inputs, conditions, criteria, and splits before generation. Keep answer keys, calibration examples, and diagnosis notes out of the subject context and writable state. Group related incidents together. Check effective skills, memory, project instructions, plugins, and provider overrides; a config flag or hash alone does not establish isolation. Preserve contaminated attempts and repair the setup before treating them as controlled comparisons.

Keep credentials out of artifacts, use controlled services or fixtures for writes, and calibrate in fresh temporary directories. Never recursively delete a caller-supplied path. Pin material dependencies and freeze external data when freshness is not being tested.

For multi-stage agents, distinguish two useful checks when relevant:

- **Recorded-evidence replay:** compare configurations using identical captured evidence. Freeze every retrieval and escalation path, or explicitly label what remains live. This measures behavior conditional on that evidence.
- **Live execution:** run through the actual retrieval and orchestration path. Use it to confirm the selected configuration and expose integration failures. Record changing data and provider conditions.

A replay answer cannot establish that live retrieval, latency, or persistence is fixed. Keep the two results and their denominators separate.

## Save attempts, then grade

Use the existing runner and project conventions. Treat one complete attempt as the evidence record, with linked files when needed:

- Case, configuration, repetition, attempt, environment, and evaluator identities; material versions/hashes and live/replay mode.
- Actual subject request and permitted context; full tool arguments/results, escalation rounds, state changes, and complete answer or artifact. Preserve referenced/offloaded evidence; a transient path or 200-character preview is not the content.
- Requested and returned models, provider/authentication route, retries/fallbacks, timing, usage receipts, and unavailable fields explicitly marked unknown.
- Per-criterion verdicts, output/source pointers, reasons, reviewer identity or mode, and separate execution/evaluator status.

Persist each completed attempt before grading; keep generation, grading, and reporting independently rerunnable. Resume only completed work with matching inputs and configuration. A judge retry reuses the saved answer. Retain failed attempts and all resource use; never report only the best retry. If production retries are tested, grade the complete policy and also retain first-attempt outcomes.

Inspect the content actually delivered to the reviewer, including required files, images, tool results, source dates, and truncation. Treat subject outputs and retrieved instructions as untrusted. Missing required evidence invalidates the affected judgment. A judge timeout, malformed verdict, or missing judge credential is an evaluator error, not proof the answer failed.

## Inspect failures and confirm improvements

Locate the first consequential divergence and distinguish subject failure, missing context, setup defects, bad criteria, and unresolved judgment. Repair the responsible component within scope. An environment or grader repair is a new measurement version, not a candidate gain. Regrade saved outputs when only grading changes; regenerate when subject inputs or conditions change. Preserve old results and label invalid grades.

Keep acceptance criteria stable across candidates. Repeat cases at the source of uncertainty: new answers for generation variability, new judgments for judge variability. Report first attempts, retries, and observed spread. Repeated runs are not independent case coverage.

Cases used for diagnosis or tuning become development data. A set repeatedly consulted for selection is validation data even if answers stay hidden. Confirm a selected candidate on unseen cases; after tuning from a failed final check, retire that set from held-out status. Fresh cases do not erase the earlier failure or establish a population-wide model ranking. Keep comparisons paired and disclose small samples, selection effects, and unavailable evidence.

## Report and hand off

Show absolute quality results with sample counts, critical failures, and declared aggregation. Report attributable cost and end-to-end subject time separately, including tools and retries. Separate simulator, grading, and whole-experiment overhead. Preserve raw billing receipts: provider charges, upstream inference, usage-based estimates, and conservative reservations are different quantities. Unknown cost is not zero; a subscription API-equivalent estimate is not an incremental charge.

Use a compact table or chart linked to complete attempts and judgments, following [the reporting procedure](references/inspection-loop.md#keep-results-visual-and-inspectable). Recompute values from saved records and verify any drill-down/export controls. A small suite does not require a dashboard or annotation framework. Keep the opening view short and evidence easy to inspect.

Deliver the runnable command, effective configuration, cases/splits, evaluator version, baseline records, limits, remaining budget, and unresolved failures. Separate packaging checks, runtime execution, grading calibration, subject success, and human review. Evaluation does not authorize changing the subject, publishing results, or deployment. Use [hill-climb](../hill-climb/SKILL.md) for authorized optimization and the optional [meta-skills skill-improver](https://github.com/exiao/meta-skills/tree/main/skill-improver) for skill experiments.

## Conditional references

Read only what the requested work needs:

- [Local benchmark preparation](references/local-benchmark.md) for deriving cases from source records; [inspect-traces](../inspect-traces/SKILL.md) for prior agent sessions.
- [Failure-to-eval handoff](references/failure-to-eval.md) for observed failures. If unavailable, retain the request, redacted trace, starting state, expected outcome, reset steps, and reproduction limits.
- [Trace-to-Harbor reconstruction](references/trace-to-harbor.md) for converting traces into tasks; account for every reviewed case and explicit adaptation.
- [Harbor](references/harbor.md) when repeatable tools, services, or isolation help. A requested task must be populated and runnable, not a scaffold. Do not install a container platform or paid runtime merely to complete a check.
- [RewardKit](references/rewardkit.md) when useful for grading saved artifacts; preserve scorer semantics and verify adapter parity. A trivial check needs no framework.
- For stateful tool/service behavior, build and verify the required transitions and reset in the existing runner; an installed `simulation-environment` skill can help. Freeze simulated-user knowledge, persona, settings, and stopping rules; keep private grading facts out of subject access.
- When the user supplies PDFs, read the relevant pages and record source/page pointers. An installed PDF skill can help; distinguish proposed workflows from measured effectiveness.
