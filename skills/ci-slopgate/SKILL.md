---
name: ci-slopgate
description: Design or repair a CI gate that prevents measurable code slop from increasing while keeping normal feature work green. Use for complexity, oversized files/functions, duplication, dead-code, or ineffective-test gates.
---

# CI slop gate

Implement or repair the gate only when asked. For assessment-only requests, return the design and proof plan. Read the repository's default branch, CI workflows, language config, source/test/generated/vendor roots, and existing lint jobs first. Reuse an existing job and installed tool; do not add a duplicate workflow or custom parser when Ruff, the compiler, or another stable tool already provides the signal.

Collect a few recurring, concrete review corrections or copied anti-patterns before choosing new rules. For each, first ask whether a simpler type, API, module boundary, or canonical example can make the mistake hard to express. If the pattern remains possible and a checker can identify it reliably, encode a narrow static rule and show the offending location and preferred fix. Keep guidance in rules, skills, or a style guide for judgments that cannot be checked precisely; do not treat a review bot's opinion as a hard lint failure. Do not impose another team's architectural conventions, such as banning all comments, without local evidence that the rule solves a real problem.

Hard-block deterministic signals that name an offender: existing linter complexity/function-size rules, unused imports, and a measured file ceiling. For whole-tree duplication or line/complexity burden, compare the candidate with the live base using the same checker and exclusions. Treat total production-line growth, unused functions/exports, model-scored slop, and test counts as advisory unless the repository has demonstrated a low false-positive rule. Test usefulness requires fail-before, mutation, or equivalent evidence; line counts and test ratios prove nothing.

Keep the base branch green without granting new debt. Measure current offenders before choosing ceilings. Exclude generated, vendored, migration, fixture, snapshot, and lockfile paths explicitly. If an override is required, demand a non-empty reason, print the failed metric and reason, and do not rewrite the threshold.

Prove the actual CI wrapper exits nonzero for planted complexity/file/duplication failures, passes unchanged and valid small changes, and preserves correctness checks. Restore temporary fixtures and run the repository's exact gate command. Report blocks, advisory signals, changed files, and pass/fail proof.
