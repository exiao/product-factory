# Multi-turn collaboration with an AI product

Use for clarification, corrections, preference elicitation, and task execution across an actual conversation with an AI product. Identify the decision under test: for example, whether the assistant asks for a missing constraint before acting. Label the user and their reactions SYNTHETIC; distinguish executed target responses and artifacts from imagined dialogue. If the target cannot be run, deliver a labeled rehearsal with the execution gap visible.

## Separate the roles and their information

Prepare three distinct inputs:

- **Simulated user:** stable persona ID, goal, initial request, relevant private facts, what they do not know, and circumstances that affect disclosure or stopping. Distinguish information offered initially, information revealed naturally or when asked, and facts genuinely unknown. Do not make every user cryptic or adversarial.
- **Target product:** its normal system instructions, authorized environment, and only the information it would receive from this user. Keep the private brief, hidden checks, and other sessions' answers out of its context and accessible files.
- **Evaluator:** the agreed success criteria, private constraints needed to check the outcome, conversation, and resulting state or artifacts. Do not feed evaluator feedback into an ongoing trial unless that feedback is itself part of the intended user experience.

Use separate contexts for user and target where available. A single model authoring both sides is a rehearsal, not independent target execution. Separate agent contexts do not ensure file isolation: inspect what each role can access when a harness shares a workspace. Record material information leakage as a limitation or invalid trial.

## Run the conversation

Have the user respond to each actual target message using only their knowledge and experience so far. Keep the initial request plausible; avoid dumping the full task specification unless that fits the persona. Answer useful clarifying questions, permit corrections and changed preferences when the scenario supports them, and allow satisfaction or abandonment. Do not invent facts to rescue the target or have the user complete the target's work through tools. Record any intended user tools, moderator help, and intervention explicitly.

Set a bounded turn or time budget and scenario-relevant stopping conditions before execution. Record why the trial ended: user-declared completion, abandonment, budget exhaustion, target failure, or infrastructure error. User-declared completion starts outcome verification; it is not a passing verdict.

## Evaluate two different things

Evaluate after the run in a fresh context when available. For each task criterion, give a verdict and an evidence pointer; mark missing evidence or evaluator errors explicitly. For durable outputs, identify the exact artifact and inspect its end state.

1. **Target outcome and interaction:** inspect the actual artifact or end state against the task criteria, including constraints disclosed during conversation. Assess clarification, corrections, and avoidable user effort where relevant. Do not penalize missing private facts unless eliciting them or handling the uncertainty belongs to the agreed task.
2. **Simulator fidelity:** review whether the user remained within their knowledge, disclosed facts consistently, reacted to actual responses, or covertly helped solve the task. Use the existing [simulation-quality review](simulation-quality-review.md). An invalid simulation limits what a target success or failure means.

Retain the private brief, initial request, full exchanged messages, role/model/configuration versions, interventions, termination reason, and evidence-backed verdict for every attempt. Apply the main skill's retest rules to comparisons. For repeatable automated scoring, use `make-an-eval` when available to author and calibrate a verifier against known good and bad outcomes. A verifier result measures this defined task; stronger models, more trials, or model agreement do not establish human fidelity. Claims of human fidelity need relevant real-user or held-out research comparisons.

## Optional Harbor execution

[Harbor's simulated-user documentation](https://docs.harborframework.com/core-concepts/jobs/simulate-a-user) describes a user agent receiving the task instruction, a target learning it through conversation, and a verifier running afterward. Its prompt separates persona, bridge instructions, and task instruction. This is a useful execution pattern, not evidence that its default user is representative of customers.

When Harbor execution is requested or fits an agreed eval, consult its current documentation and verify installed target support, model availability, limits, and artifact capture before running. Do not assume an arbitrary product endpoint is supported. Its documented roles share a task environment, so check actual file visibility and user tool permissions instead of assuming prompt privacy provides isolation. Keep harness setup and execution proof separate from the quality of the simulation.

Source context: [Viv Trivedy's September 7, 2026 post](https://x.com/vtrivedy10/status/2097041316958122487) argues for multi-turn human-AI collaboration evals and expresses hope for improved user simulation. It does not supply a validation study. The protocol above adapts the execution pattern while retaining this skill's evidence boundaries; it is not a claim that Harbor enforces every safeguard.
