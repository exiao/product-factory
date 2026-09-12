---
name: ci-slopgate
description: Design or repair a CI gate that prevents measurable code slop from increasing while keeping normal feature work green. Use for complexity, oversized files/functions, duplication, dead-code, or ineffective-test gates.
---

# CI slop gate

Implement or repair the gate only when asked. For assessment-only requests, return the design and proof plan. Read the repository's default branch, CI workflows, language config, source/test/generated/vendor roots, and existing lint jobs first. Reuse an existing job and installed tool; do not add a duplicate workflow or custom parser when Ruff, the compiler, or another stable tool already provides the signal.

Hard-block deterministic signals that name an offender: existing linter complexity/function-size rules, unused imports, and a measured file ceiling. For whole-tree duplication or line/complexity burden, compare the candidate with the live base using the same checker and exclusions. Treat total production-line growth, unused functions/exports, model-scored slop, and test counts as advisory unless the repository has demonstrated a low false-positive rule. Test usefulness requires fail-before, mutation, or equivalent evidence; line counts and test ratios prove nothing.

Keep the base branch green without granting new debt. Measure current offenders before choosing ceilings. Exclude generated, vendored, migration, fixture, snapshot, and lockfile paths explicitly. If an override is required, demand a non-empty reason, print the failed metric and reason, and do not rewrite the threshold.

Prove the actual CI wrapper exits nonzero for planted complexity/file/duplication failures, passes unchanged and valid small changes, and preserves correctness checks. Restore temporary fixtures and run the repository's exact gate command. Report blocks, advisory signals, changed files, and pass/fail proof.
