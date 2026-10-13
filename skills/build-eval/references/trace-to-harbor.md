# Turn a trace into a Harbor task

Use this workflow for a local agent session or traces.com trace. Reuse the existing eval record and the [failure-to-eval handoff](failure-to-eval.md); do not create a second manifest system. Read [Harbor implementation](harbor.md) for version-specific packaging and execution.

## Establish the case with the user

Reuse supplied answers. Ask which trace and task to recreate, whether the agent should start fresh or continue from a checkpoint, which environment and tools it must use, and what observable result counts as success. Ask about forbidden actions and unavailable starting data when relevant. Resolve these questions before building dependent fixtures. Recommend a concrete checkpoint and environment after inspection, but do not assume approval for a different task or a simulated replacement.

## Retrieve and preserve evidence

Use [inspect-traces](../../inspect-traces/SKILL.md) to retrieve the selected local session or hosted trace. Save its source URL or path, stable ID, event range, relevant artifacts, and retrieval completeness in the case record. Inspect pagination, truncation, missing attachments, compaction and fork boundaries. Search snippets or summaries alone cannot establish the full original input. Preserve a bounded source copy when permitted, record transformations, and keep private source material outside the subject environment and version control unless explicitly intended.

Before declaring inputs missing or asking the user to reconstruct them, inspect the original tool call arguments and paired results throughout the relevant task segment, including tool observations between the request and answer. Follow generated-file paths and delegated-session references. A bounded summary or truncated displayed output does not establish that the original file or full tool receipt is absent. Treat recovered historical queries and responses as environment evidence; keep later corrections and outcome labels private. Earlier assistant-authored mockups may be legitimate task inputs when the user is asking to evaluate those mockups; distinguish the artifact being evaluated from a leaked evaluation answer.

Separate these records:

- Source trace: historical evidence used to construct the case and verifier.
- Initial history: an explicitly selected prefix supplied to a continuation trial.
- Generated trajectory: the new attempt saved as trial evidence.

For a fresh-start task, recover the original request and contemporaneous inputs. For continuation, identify the exact checkpoint and reconstruct both history and world state at that point. Exclude later answers, corrections, fixes and reviewer diagnoses from subject inputs. A continuation comparison measures behavior given that prefix, not independent end-to-end task performance.

## Reconstruct the starting world

Record the relevant repository revision and uncommitted changes, input files, database/service state, tool contracts, permissions, time assumptions, knowledge and memory versions, and setup/reset commands. Do not use the final fixed checkout as the starting snapshot. Mark each material fact as captured, reconstructed, simulated, or unknown, with evidence and fidelity limits. If required state cannot be recovered, ask whether to supply it or accept a specific controlled simulation; do not call an incomplete reconstruction faithful.

Check the requested runtime against required OS, architecture, binaries, browser/desktop capabilities, services, network policy, resources, and artifact collection. Distinguish the task's world from the provider that runs it. A provider substitution requires compatibility evidence; a shell-only imitation of desktop work changes the tested task. Use a supported Harbor sandbox or a scoped custom adapter only when its required capabilities can be provided.

Recorded responses suffice for independent reads only when valid under the permitted inputs. If new actions affect later observations, implement coherent state transitions and reset, using an installed `simulation-environment` skill if available. Do not serve the original response sequence after a new agent takes a different path. Unsupported operations must be reported as environment limitations, not fabricated successes or agent failures.

## Package the task and configurations

Generate files using the selected Harbor release. Keep private authoring evidence outside the task's agent-visible build context.

| Evidence or decision | Destination |
| --- | --- |
| Request, normal inputs, explicit constraints | `instruction.md` and allowlisted input fixtures |
| Checkpoint-consistent files, services and tools | `environment/` plus supported environment configuration |
| Selected continuation prefix, if any | Supported native or ATIF loading, checked for loss and leakage |
| Observable success and forbidden-action checks | Private verifier logic in `tests/`, with appropriate isolation |
| Reference implementation, when practical | `solution/`, available only to control runs |
| Source pointers, reconstruction limits, case version | Existing authoring/case record outside subject access |
| Model, harness, skills, knowledge/history variants and runtime | Versioned run configurations and referenced fixtures |

Keep task, evaluator and configuration identities distinct. Freeze material files and settings, recording hashes or versions and injection locations. Bundled skills and job-provided skills must not unintentionally collide. Keep the expected outcome fixed across a comparison unless the declared experiment explicitly changes the task contract.

## Convert a collection without losing coverage

For a supplied index or another chat, inspect its current case registry and source links before choosing examples. Account for every reviewed case in one coverage manifest: source ID and trace URL, selected checkpoint, task path or concrete blocker, reconstruction mode, and validation status. Keep unreviewed discovery leads separate from confirmed cases. Group related episodes by conversation and shared artifacts for splits; many excerpts from one conversation are not independent samples. When multiple objections refer to the same request and proposal, retain every source mapping but select one shared checkpoint for execution instead of inflating the trial count.

Recover each case from its original request and tool receipts. A rejection headline is private authoring metadata, not a task instruction or a rubric. Verify the immediate triggering request: a collector's prior-goal pointer can skip intervening instructions or refer to a different artifact. Identify whether the observed objection adds a previously unavailable preference. Grade only what the subject could reasonably infer from its supplied evidence; accept supported alternative decisions. Do not make an implementation or visual task appear replayable by requiring only an essay about the intended result.

When the original environment cannot be restored, preserve its exact missing prerequisites. Offer a clearly labeled decision or planning adaptation if useful, and obtain agreement before treating that changed task as the requested replay. Record the original and adapted contracts separately. If both are built, report their scores separately. A written product decision cannot establish interface quality, implementation correctness, or whether the original failure reproduces.

Use a repeatable generator when many cases share packaging, but author and review case-specific context and success criteria. Keep raw traces, rejection labels, recovery notes, and source titles outside the subject build context. Preserve existing richer tasks instead of replacing image or service evidence with generic text. Validate all generated task configurations and job paths; do not infer suite validity from one working example. Keep packaging, local verifier controls, paid judge calibration, and container trials as distinct per-case statuses. Earlier authorization for a small calibration does not expand into an unbounded suite run.

## Verify and hand off

Before subject runs, exercise setup, tool/service behavior, reset, artifact arrival, and subject/grader separation in the chosen environment. Check that initial history agrees with the actual starting state. Calibrate the verifier against known-good, plausible-bad, and missing or malformed results. Score the outcome and required boundaries, accepting valid alternate paths.

Use the main skill's declared plan, finite run limits, and subscription CLI/API authorization rules for controls and real-agent trials. When reproducing an observed defect, rerun the available baseline configuration and report whether and how often it reproduces; a non-reproduction may reflect stochastic behavior or reconstruction limits. Do not require identical trajectories or treat one baseline rerun as proof of fidelity. Retain successful cases and incident-level splits to limit selection bias and leakage.

Deliver exact commands, pinned versions, case/configuration records, and evidence paths. Distinguish packaged, environment verified, verifier calibrated, and agent trial completed. Report unknown state and unrun checks explicitly. If the requested environment is unavailable, preserve the prepared task and ask about the specific missing prerequisite; do not silently switch providers, install a container platform, or launch a paid runtime.
