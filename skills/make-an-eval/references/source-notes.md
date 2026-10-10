# Source notes

Inspected 2026-09-30. These sources informed the workflow; they do not establish that this skill improves performance.

- The installed `skill-improver` skill supplied the bounded comparison loop, critical regression gates, isolated candidates, sealed final test, and promotion boundary. It is an optional dependency and is not bundled here.
- Anthropic's [eval-hillclimb](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/evals/eval-hillclimb.md) motivated explicit optimization direction, a check that the tuned mechanism reaches execution, and measuring stochastic build variation separately from repeated scoring.
- Anthropic's [eval-audit](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/evals/eval-audit.md) informed the shared evaluation-readiness checks for task coverage, measurement defects, and runtime wiring.
- Anthropic's [build-eval](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/evals/build-eval.md) informed incremental result persistence and explicit attempt/resume semantics.
- Lance Martin's [Automating eval design and hillclimbing with Claude](https://claude.dev/blog/automating-eval-design-and-hillclimbing/) informed the sampling guidance in make-an-eval's local benchmark reference, diagnosis before further edits when progress stalls, and checks that changes serve the intended workload.

This adaptation preserves the local subscription-first execution policy, runner independence, and quality/cost/time reporting. It does not import Claude-only commands, fixed report filenames, mandatory approval at each round, or hard-coded prices. Data used repeatedly for candidate selection is validation data here; final test data stays sealed. End-to-end task timing includes retries. Failures and truncated outputs remain visible and follow the declared success contract rather than automatically disappearing from averages. Existing authorization remains valid within its scope.
