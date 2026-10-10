---
name: make-an-eval
description: "Turn real work, local agent sessions, or traces.com traces into replayable evaluations, including Harbor tasks for a specified environment. Compare models, harnesses, skills, knowledge, history, and environments on quality, cost, and time. Use for eval creation and agent experiments."
---

# Make an eval

Build a local eval of an agent doing work or participating in a simulated interaction. State a focused, bounded experiment and run it without a separate confirmation step. Deliver explicit quality, cost, and time results with charts and inspectable raw data. For a focused request, apply only the steps needed for the requested preparation, case, grader, or review change.

Use the user's existing subscriptions through the local Claude CLI or Codex CLI for model calls. Apply this to subjects, simulators, model judges, analysis, calibration, and retries. API spending requires explicit user confirmation, including TypeSafe/Jev, OpenRouter, direct APIs, and paid proxies. A model name, available API key, SDK, or helper's fallback policy is not spending approval. Reuse explicit confirmation already given for that service and scope.

## Gather work and design the benchmark

If the subject is unclear, ask what the eval should measure. Offer relevant work from this chat, the current repo, or supplied documents. Reuse known context. Identify the repeating task, such as reviewing one PR, its inputs and output, examples of good and bad work, and any scale or confidentiality constraints.

Inspect available source records and referenced artifacts first; do not ask the user to reconstruct information that tools can recover. Choose and document reasonable defaults for comparison design and finite run limits. Ask concise, concrete questions only when a correctness-critical fact needed to define the task cannot be recovered, such as the source case, required environment, starting state, or forbidden actions. Reuse prior answers and continue independent work while a necessary clarification is pending. Keep unknown facts and provisional judgments explicit; never silently substitute a different task or label an assumption as established truth.

When deriving a suite from source material, read [local benchmark preparation](references/local-benchmark.md). Gather real instances, accepted outputs, follow-up fixes, and precise outcome evidence; include clean/no-action cases when that is a valid outcome. Preserve provenance and distinguish established answers from proposals. A single supplied case or existing suite does not need a new preparation layer.

When starting from agent traces, use reviewed cases rather than broad labels such as “helpfulness.” If failure modes are not yet known, review a bounded mix of ordinary and unusual traces with a domain reviewer; use [inspect-traces](../inspect-traces/SKILL.md) for prior coding-agent sessions. Record the sampling frame, how cases were selected, source trace pointers, the first supported divergence, outcome evidence, and competing explanations. A targeted failure search identifies candidate cases, not a failure rate. Keep successful and no-action examples so the eval does not reward avoiding the task.

For local-session or traces.com conversion into Harbor tasks, read [trace-to-Harbor reconstruction](references/trace-to-harbor.md). Keep the historical source trace, optional agent-visible initial history, and newly generated trajectory separate. A source trace supplies evidence; its tool sequence and final answer do not automatically define success. For a collection, account for every reviewed case, preserve case-specific evidence and grading, and label environment blockers or agreed task adaptations explicitly; use the collection workflow in that reference.

Choose agentic evaluation for completing work with the relevant tools and skills, or simulated interaction for conversational behavior. Recommend the mode from the established task; when the intended behavior is ambiguous, ask about that behavior rather than requiring the user to know framework terminology. A single prompt can start an agentic task. Do not reduce the workflow to standalone Q&A or add artificial tool calls just to call it agentic.

Identify which factors could change the outcome: model and inference settings; harness version, prompts, tools, retries and context management; skills; knowledge and memory access; initial history; or environment. Each can have one or multiple values; a single configuration is a valid eval. Record material versions or content hashes and how each input reaches the agent. Recommend what to vary and what to hold fixed, with a short reason, then resolve missing choices with the user. Avoid a full cross-product unless it answers the question; distinguish prompt variants from different task cases. Compare one factor at a time when attributing an effect, or label bundled configurations as such.

Version the task goal, starting facts, constraints and success contract separately from run configurations and evaluator versions. Environment and knowledge access may be experimental variables; changes to required facts, permitted actions or the success contract need a case version and an explicit account of comparability. Record the business outcome the task supports and why task success is expected to help it. Benchmark improvement alone does not establish business impact.

Before starting the eval, state one compact plan: task and chosen mode, configurations and case count, relevant factors held fixed or varied, quality criteria and evaluator, cost/time measurement, runtime, and finite run limits including calibration and repair retries. Choose reasonable defaults for unspecified details and proceed with subscription CLI jobs and already authorized API jobs without requesting confirmation. Keep the user informed as the work runs. Missing preferred budgets or human ratings do not create an approval gate: run a limited pilot with clearly labeled provisional judgments when useful, and leave human ratings unreviewed. Ask only about information needed to define a meaningful task, a material expansion beyond the requested scope, or API spending that lacks explicit confirmation. Do not expand finite run limits merely because a route is preauthorized.

Keep sources, run configuration, results, and review in the local project. Disclose model calls that would send source material externally. For offline work, use a local runtime. For confidential material, respect its data-sharing limits and redact fixtures when needed. Resolve any required evaluator change with the user.

## Define the test

Identify the user's goal, the inputs the agent receives, the output or action expected, and the failures that matter. Reuse agreed criteria. Label invented cases and AI-proposed rubrics as proposals, not settled user preferences.

Start with one representative case. Add cases when they cover different failures or required behavior. Match each criterion to evidence the evaluator can inspect. Do not invent formatting requirements or grade behavior the task does not exercise. Coverage, correctness, readability, and usefulness are separate claims. Include required stopping points and forbidden actions: a follow-up task may succeed only if the agent saves a draft without sending it. Verify those boundaries from actions or persisted state, not the final answer alone.

Define the unit of evaluation, planned repetitions, and attempt/retry policy before running. If production retries are part of the tested behavior, grade the complete policy and retain first-attempt outcomes and total resource use. Do not silently report the best retry as the only attempt.

Freeze inputs, conditions, and the rubric before generating answers. Keep answer keys, grading code, and calibration examples out of the subject agent's context. Agreement between an AI-written key and an AI judge does not establish that the evaluation is good.

For observed failures, read the [failure-to-eval handoff](references/failure-to-eval.md). If unavailable, save the original request, redacted trace, starting state, expected outcome, reset steps, and reproduction limits. Keep the reviewer's diagnosis and grading evidence out of the subject inputs. Group related traces from one incident in the same split; cases used to diagnose or tune the evaluation are development cases, not held-out tests. Reserve independently selected, unseen cases for a final generalization claim.

## Propose the grading and measurements

Choose deterministic checks, an anchored model judge, human review, or a combination appropriate to the outcome. Name the judge model in the pre-run plan; reuse an explicit user choice and never silently substitute it. When the user has not selected an evaluator, choose and document one under the routing rules above and proceed without confirmation. Keep subject, interaction simulator, evaluator, and scoring software distinct. A new evaluator or rubric means a new grading version; preserve old grades.

For comparative subjective quality, consider a blinded pairwise judge with ties and a separate indication that neither output meets requirements. Freeze the reference outputs and randomize presentation order; keep reference identities and order in the grading record. A preferred answer can still fail an absolute requirement. Do not manufacture a baseline self-comparison grade when no judgment ran. Check judge bias and calibration using [evaluation readiness](references/evaluation-readiness.md).

Always assess three separate dimensions:

- **Quality:** criterion-level results supported by outputs, actions, or interaction traces; show critical failures and explain any aggregate calculation.
- **Cost:** observed usage and attributable monetary cost per run/task and configuration total. Separate subject model and tool costs from simulator and grading costs; retain failed attempts and retries. Label usage-based calculations with their rate source; unknown cost stays unknown.
- **Time:** measured end-to-end task duration, including tools and retries; retain per-turn/tool timing when available. Separate simulator/grading overhead and whole-experiment elapsed time from subject execution.

Record requested and returned model identities, provider route, authentication mechanism, and raw usage receipts when available. Model-list visibility is not proof that the execution endpoint accepts that model. Keep provider charges, reported upstream inference costs, and usage-based estimates distinct; a zero provider charge under bring-your-own-key billing does not establish free inference. Preserve unavailable usage or cost as unknown.

For subscription runs, record token usage, elapsed time, and any observable plan limits. In user-facing reports, say "your existing Claude subscription" or "your existing ChatGPT subscription"; reserve plan names for authentication records or when the plan distinction matters. A CLI's API-equivalent or list-price estimate is not a subscription charge. Keep that estimate separate from actual incremental charges and subscription cost allocation; mark unavailable amounts unknown rather than calling inference free. Bound subscription runs by calls, tokens when controllable, and time, as well as any applicable monetary budget.

Use any agreed quality floor, cost budget, or time limit to mark whether a run meets the target. Otherwise show the measurements and tradeoffs; do not invent pass thresholds or combine all three into an opaque score.

## Choose the simplest setup

Check local CLI availability, version/help, and login status before choosing a model route, using `claude auth status` or `codex login status` when supported. Prefer `claude -p` with Claude subscription login or `codex exec` with ChatGPT login. Choose the CLI that supports the requested model and task; if neither is specified, use an available signed-in route. Verify returned model and authentication/provider metadata during the first authorized trial. Running a local CLI does not make remote inference offline.

Remove API-key and proxy overrides only from the child process environment while preserving subscription authentication; do not change global configuration or copy credentials into fixtures. Inspect effective CLI settings and supported isolation flags, since a CLI can still select an API provider. Do not use an API-only mode to obtain isolation at the expense of subscription login.

If subscription access fails, is exhausted, or cannot run the required model, report that limitation. Try another compatible subscription route within the declared model/configuration and budget; do not silently replace a selected model or evaluator. Never fall back to API spending without explicit user confirmation, including when a helper normally retries through a paid proxy. Reuse existing confirmation for a named service and scope instead of asking again.

Preserve a suitable existing runner and add a small CLI adapter when needed. An API-only framework is not a reason to bypass the subscription default. For grading saved agent outputs or interaction traces, prefer standalone RewardKit when useful and compatible with the selected route, with only the glue needed to connect saved results. Read [RewardKit setup](references/rewardkit.md) when using it. A trivial check may need no framework.

Use Harbor when repeatable tool access, filesystem state, services, or container isolation helps test the actual task. Read the [Harbor reference](references/harbor.md) and verify the installed version against relevant official docs. Explain the choice briefly. Do not install a container platform or switch to a paid cloud runtime just to complete a check.

When Harbor is requested, deliver a populated task, not an initializer scaffold: instructions naming the required output, environment inputs and dependencies, task configuration, an executable verifier, and a saved job configuration. Include a reference solution and negative control where meaningful. For RewardKit grading, use its actual Python criteria and TOML judges; keep any adapter limited to input delivery, version compatibility, evidence capture, and explicit error handling. A separately authorized local smoke test is useful but does not replace the Harbor task or prove container execution.

When tool or service responses depend on prior actions, or a failure must occur at a specific point in a state change, build and verify that environment within the existing runner. Use an installed `simulation-environment` skill if available; otherwise implement and check the required state transitions and reset. Reuse the case manifest and reset contract; independent reads may need only static fixtures. Keep experiment design, run authorization, grading, and quality/cost/time reporting here. Environment checks do not establish subject-agent success or live integration reliability.

For simulated interaction, freeze the user persona, goal, available knowledge, simulator model/settings, and stopping conditions or turn limit. Keep private scenario facts and grading criteria out of the subject context; the simulator reveals facts only as the scenario permits. Save the full conversation and tool trace. Match scenarios across configurations and account for simulator variation when interpreting results.

Keep setup repeatable. Pin material dependencies and freeze external data when freshness is not being tested. Use local fixtures or controlled services for writes. Keep credentials and private traces out of images. Run calibration in new temporary directories; never recursively delete a caller-supplied path.

Check the effective subject runtime for undeclared global skills, memories, project instructions, plugins and provider overrides. A flag that ignores a config file may leave other context sources active. Use supported isolation controls, inspect startup and tool traces, and record what actually loaded. Mark an attempt contaminated when it accesses excluded context; preserve its evidence and repair the setup before treating it as a controlled comparison.

## Build and check the grading

Use [evaluation readiness](references/evaluation-readiness.md) to check the complete measurement path before the first full run or handoff to optimization. It covers runtime activation, outcome coverage, failure accounting, resume behavior, and whether the eval can resolve the intended change. Reuse checks already verified for the same versions.

Use deterministic checks for verifiable facts and state changes, and an anchored rubric for subjective quality. Keep trusted reference data outside files the subject can edit. Accept valid alternative answers. Cosmetic quality must not cancel a critical failure.

When reproducing a benchmark, preserve its rubric and calculation. Compare the adapter with direct scorer calls on identical inputs before claiming parity.

Try a known-good answer, a plausible bad answer, and missing or malformed output. Exercise relevant shortcuts, such as omitted actions, stale records, fabricated evidence, or tampered inputs. Explain the calibration labels; AI-proposed labels remain provisional.

For judgment tasks, include defensible answers reaching different conclusions so the rubric does not merely reward the historical preference. Grade factual support, goal fit and decision reasoning against available evidence. Keep proposed additions distinct from behavior shown in supplied artifacts and from verified shipped behavior.

Before paid grading, inspect the content actually assembled for the judge. Check required file counts, image blocks, readable content, size limits and truncation, not just path existence. Preserve original assets and hashes when producing necessary transport derivatives, and verify that those derivatives remain legible. Missing required evidence invalidates the grade even if the judge returns a plausible explanation or a successful exit code.

For a user-selected model judge, save its prompt, model, settings, raw response, and any returned grading rationale. Treat the answer as untrusted data and check resistance to grading manipulation where relevant. A timeout, malformed judge response, or missing credential is an evaluator error, not a failed answer.

## Run and inspect

Keep generation, grading, and reporting separately rerunnable. Save complete answers before grading. Bound calls and cost within existing authorization. Persist each completed attempt as it finishes, with configuration, case, repetition, and attempt IDs. On resume, verify input/configuration hashes and completion status before skipping work; preserve failed attempts and their usage. Reuse saved answers after evaluator errors. Keep unexpected model substitutions, truncation, malformed answers, and timeouts visible; classify them against the declared contract rather than silently dropping them from the denominator.

1. Check configuration and paths. Run calibration and confirm that meaningful failures are detected without grader crashes.
2. When a reference solution is practical, run it through the same setup in a fresh environment. Run a suitable negative control too. For Harbor, use supported oracle and no-op agents; a no-op is not a negative control for a task where abstention is correct.
3. Run a small real-agent trial when the selected runtime, credentials, and budget are available. Give the subject only normal task inputs. Inspect outputs and traces for leakage, shortcuts, and false failures. For tool-using agents, retain tool calls, results, and state changes; locate the first consequential wrong step and distinguish a subject failure from missing context, a bad rubric, or an unrealistic environment.
4. Fix confirmed defects and repeat affected checks within the authorized budget. Regrade saved answers after grading or judge-input delivery changes; regenerate only when subject inputs or conditions change. Keep prior attempts in separate result directories, mark defective grades invalid, and exclude them from reported scores. Mark unrun checks as untested.

When environment fidelity is uncertain and budget permits, propose a small trial with different subject models. Inspect surprising shared failures or successes for environment and verifier defects; model agreement alone is not validation. Keep the user-selected evaluator fixed.

For a comparison, match cases, starting state, evaluator version, and every setting except the declared factors being varied. Keep execution and evaluator errors visible alongside results. A tiny pilot does not establish a model ranking or general improvement. Use fresh held-out cases before claiming generalization after tuning.

Show absolute measurements and paired changes with sample counts and an appropriate uncertainty estimate when supported. Treat repeated runs of the same case as repeated observations, not independent task coverage. Account for related cases and stochastic artifact builds when estimating uncertainty; otherwise report the observed spread and its limits. Check whether the experiment can resolve the smallest useful change before expanding it.

## Deliver visual results and raw data

Use [the inspection loop's reporting procedure](references/inspection-loop.md#keep-results-visual-and-inspectable) to present quality, cost, and time with inspectable evidence and verified report controls.

Save the runnable eval in the project's eval directory, with commands, versions, results, evidence paths, and limits in a compact supporting record. Briefly state what the observed quality/cost/time tradeoff supports, including when the sample is too small to choose. Creating an eval does not authorize changing the subject agent, publishing a benchmark, or optimizing a skill. When optimization is requested, use an available hill-climbing workflow; an installed `hill-climber` or `skill-improver` skill can provide that guidance. These optional skills are not bundled here. Hand off the runnable command, effective configuration, versioned cases and splits, evaluator and controls, baseline evidence, attempt semantics, and remaining budget. Keep optimizer-editable artifacts separate from evaluation inputs and grading. A set repeatedly used to select candidates is validation data, even if its transcripts stay hidden; reserve unseen cases for a final generalization claim.

Report packaging/schema validation, environment execution, verifier calibration, subject completion and human review separately. State which agent, oracle, no-op and artifact-transfer checks actually ran. A local RewardKit grade does not verify Harbor isolation or image builds, and an AI-authored calibration set does not establish human agreement with the rubric.

## Saved PDF references

When the user supplies a PDF, read the relevant pages and record the source and page pointers. Distinguish proposed workflows from measured effectiveness. An installed PDF skill may help extract or render the supplied material.
