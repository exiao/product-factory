# Harbor implementation reference

Official trajectory, skill and sandbox docs checked 2026-09-28. Harbor 0.23.0 CLI confirms `run -p -a -m`, `--load-trajectory`, and `task init`; its installed source confirms public network defaults and JSON-first reward parsing. Recheck relevant docs and installed CLI before generating a task; documentation can describe a newer release.

- [Task structure](https://docs.harborframework.com/core-concepts/tasks/overview): task files, environment, grader, and artifact transfer; navigation links to installation and RewardKit guidance.
- [Create a task](https://docs.harborframework.com/tutorials/create-a-task): authoring instructions, environment, solution and tests.
- [Create a RewardKit verifier](https://docs.harborframework.com/tutorials/create-a-verifier-with-rewardkit): native criteria and scoring integration.
- [Run a job](https://docs.harborframework.com/core-concepts/jobs/run-a-job): saved configurations, controls and results.
- [Separate verifier](https://docs.harborframework.com/core-concepts/tasks/separate-verifier): independent image and artifact transfer.
- [Loading trajectories](https://docs.harborframework.com/core-concepts/jobs/loading-trajectories): replay a prior run with `--load-trajectory`.
- [Job skills](https://docs.harborframework.com/core-concepts/jobs/skills): `--skill` local/Git injection and provenance lock.
- [Task skills](https://docs.harborframework.com/core-concepts/tasks/skills): bundled skill directory requirements.
- [Custom sandboxes](https://docs.harborframework.com/core-concepts/sandboxes/custom-sandboxes): `BaseEnvironment` lifecycle/exec/file-transfer.
- [Official source](https://github.com/harbor-framework/harbor): resolve version-specific behavior against the release/tag actually used.

## Version and environment check

```bash
command -v harbor
harbor --version
harbor --help
harbor run --help
```

Use only supported subcommands. Current [official task-creation guidance](https://github.com/harbor-framework/harbor/blob/main/skills/create-task/SKILL.md) uses `harbor task init "org/task-name"`; verify `harbor task init --help`. Other doc pages show `harbor init --task` or older `harbor tasks init` forms. Prefer the installed version's canonical command. Likewise, generate `task.toml` with the selected release instead of mixing legacy `version` metadata with newer `schema_version` examples. If unavailable, record the docs schema targeted and leave compatibility untested. The documented install is `uv tool install harbor`; install only within task scope, and retain an existing pinned project version.

For offline fixtures, explicitly configure an appropriate network policy supported by the selected version/provider; the current environment baseline defaults to public. Account for agent installation and model access instead of assuming every phase can be offline.

Check the selected runtime independently (for Docker, `docker info`), including daemon availability. CLI import/help does not prove container execution. Start with local execution and one task; do not silently substitute a billable cloud runtime.

## Files and runtime boundary

A conventional task has `instruction.md`, `task.toml`, `environment/Dockerfile`, `tests/test.sh`, and optionally `solution/solve.sh`. Build only agent-visible files into the environment. Avoid copying the task root into the image. With the default shared verifier, Harbor stages tests at runtime; oracle solutions are staged for oracle runs. Use absolute container paths in entrypoints.

Make the output contract agree across instructions, agent workspace, artifact collection and verifier. If grading `/app/answer.md`, require the agent to write that file; a final chat message alone does not satisfy the contract. Replace generated placeholder instructions, Dockerfiles and test scripts before calling a task implemented. Save the resolved job configuration, pin material runner/agent/verifier versions, and distinguish version tags from immutable image digests.

For robust grading, treat agent-owned code, files, and logs as untrusted evidence. When isolation matters, verify that the installed version supports a separate verifier environment. Explicitly transfer required artifacts and build the grader into its own image according to that version's docs; do not assume the entire agent workspace is copied. Test both artifact arrival and missing artifacts. A shared container is not a strong anti-tampering boundary.

In Harbor 0.23.0, `[verifier].environment_mode = "separate"` enables a fresh verifier environment. A dedicated `tests/Dockerfile` must bake in `/tests/test.sh` and its dependencies; tests are not additionally uploaded to that image. Copy trusted references into its build context and verify hashes. An artifact's `source` is its restored verifier path; `destination` only controls host storage. For example, `{source = "/app/answer.md", destination = "answer.md"}` restores `/app/answer.md`. Declare only needed artifacts so agent-written files cannot replace trusted grader inputs.

Configure network policies per phase: setup may need dependency downloads, while subject execution should allow only required model/service access. Verify that the selected provider enforces those policies. Do not describe an instruction saying “do not browse” as network isolation.

## Trajectory loading and reconstruction

See [trace-to-Harbor reconstruction](trace-to-harbor.md) for the full workflow; this section covers Harbor controls. Inspect the source format and sandbox-file dependencies; ask the user about consequential gaps that inspection cannot resolve.

Per [Loading trajectories](https://docs.harborframework.com/core-concepts/jobs/loading-trajectories): a task's `trajectory.json` is ATIF. `harbor run --load-trajectory` accepts ATIF `.json` and native `.jsonl`, with Codex/Claude support; native replay requires the same agent. Format conversions can omit system messages, non-text content, and agent-specific data. Neither path restores sandbox files. The `load_trajectory` job option cannot be combined with `user_agent`. Verify the flag name and supported formats against the installed CLI before use.

Load only the reviewed prefix ending at the selected checkpoint. Inspect converted content for later answers or fixes and verify solution/grader files are absent from subject access in a fresh run.

## Skills: job injection versus task bundling

Job-level injection per [Job skills](https://docs.harborframework.com/core-concepts/jobs/skills): `--skill` accepts a local path or Git URL, uploaded to `/harbor/skills` or `environment.skills_dir`. When multiple skills share a name, the last one wins. The run records a provenance lock with content hashes. Task-level bundled skills per [Task skills](https://docs.harborframework.com/core-concepts/tasks/skills): setting `environment.skills_dir` does not copy files; the directory must actually exist in the environment. Verify that the selected agent discovers those skills. For non-Docker runtimes, see [Custom sandboxes](https://docs.harborframework.com/core-concepts/sandboxes/custom-sandboxes) (`BaseEnvironment` lifecycle/exec/file-transfer). Inspect skill sources, target paths and name collisions; ask when the intended effective skill remains ambiguous.

## Reward and diagnostics

Write exactly one reward format in `/logs/verifier/`: scalar `reward.txt` or numeric-metric `reward.json`. Current [verifier source](https://github.com/harbor-framework/harbor/blob/main/src/harbor/verifier/verifier.py) reads JSON first, but older tutorial text disagrees; never depend on both existing. Clear stale reward files within this dedicated output directory before each grading attempt, and write the final reward atomically after evaluation completes. Keep diagnostic strings in a separate report.

For a normal task failure, write the corresponding numeric score and explanatory evidence. For a grader crash, missing dependency, or judge outage, record an evaluator error and inspect how the selected Harbor release reports it; do not manufacture zero reward and call that a measured task failure. If an existing harness mandates a sentinel score, preserve an explicit error status and exclude it from success-rate calculations. Do not use a catch-all shell trap that converts every process error into task failure.

Use the quality criteria and explicit critical-failure rule from the declared plan. Keep cost and time as separate reported dimensions even when Harbor requires a primary quality reward. RewardKit can aggregate multiple criteria; inspect the configured rule and returned metrics instead of treating any nonzero field as success. Keep rubric anchors and grading-only credentials out of the agent environment. Resolve credentials through an approved environment mechanism; never put literal keys in TOML.

## Commands and evidence

After stating the main skill's bounded plan, verify flags and agent names against the installed release and proceed under its subscription CLI and API authorization rules. These commands illustrate individual controls and trials; run the configurations and case count from that plan:

```bash
harbor run -p /absolute/path/to/task -a oracle
harbor run -p /absolute/path/to/task -a nop
harbor run -p /absolute/path/to/task -a AGENT -m MODEL
```

`nop` is a no-op control; verify its availability before use. If unavailable, use a supported equivalent that leaves the starting state untouched. Choose the actual authorized agent/model, not the placeholder values above. Inspect result artifacts and verifier logs, not just CLI exit status. Preserve the output directory printed by the run and the resolved configuration.

For 0.23.0, `harbor run --config job.json --print-config` resolves configuration without running trials; `--dry-run` performs preflight and can expose a missing runtime. Validate the task with the installed loader as well. Neither check substitutes for an actual environment run. If a runtime is unavailable, finish the task package and independently authorized local verifier checks, then report container execution as blocked.

For each run record task content/version, agent/model, Harbor/runtime versions, the full configuration identity from the main skill (including harness settings, skill hashes, knowledge/memory versions and history prefix), outcome reward, task/evaluator/environment status, and measured duration, usage, and attributable cost, with unavailable values explicitly marked. Retain tool/retry costs and link results to raw records for the quality/cost/time charts described in the main skill. Oracle, no-op, and real-agent checks answer different questions; keep their results separate. Local calibration cannot establish that container setup, artifact transfer, network policy, or real-agent execution works.
