---
name: make-it-work
description: Own an outcome end to end when the user says make it work or handle this. Use goal mode, independent reviews, and fixes until the product works.
---

# Make it work

Build the full agreed outcome, prove it works, and fix it until it passes.

## Build

Define what the user needs to accomplish and what useful result would demonstrate success. Map the original requirements to evidence from the actual configured workflow and its downstream result. For new products or uncertain solutions, demonstrate the core benefit with realistic inputs before broad implementation. Build the full agreed outcome and run the implementation checks.

Use goal mode for the whole job, including reviews and fixes. Reuse a matching goal; don't overwrite an unrelated one. If goal mode can't be used, explain why and track progress in the task.

## Review

Once the product is ready to test, assign each review to a separate subagent. Give them the original request, success criteria, and what they need to run the product. Let them judge the result without coaching them toward a pass.

Run reviews in parallel where possible. Reviewers sharing a browser or computer session should take turns.

1. **Synthetic users:** Have simulated users attempt a realistic task from start to finish with representative inputs, without guidance. Can they finish the job, and is the resulting output useful? Record where they get confused, need workarounds, or give up.
2. **Heuristic evaluation:** Check usability, accessibility, and polish using [$ui-lint](../ui-lint/SKILL.md), [$impeccable](../impeccable/SKILL.md), and Nielsen Norman heuristics. Show the specific screen or interaction and the obstacle behind each finding. Preserve approved design choices while fixing the obstacle.
3. **Agentic QA:** Use the browser or computer to test the actual product. For CLI or backend work, run the commands or call the endpoints. Check the main flow, transitions after completed actions, errors, recovery, and whether changes persist. Use [$verify-feature](../verify-feature/SKILL.md), and capture steps and screenshots or logs. Unit tests alone aren't enough.
4. **Slop gate/code review:** Use [$code-review](../code-review/SKILL.md) to find bugs, unnecessary complexity, duplication, dead code, and weak tests. Run existing quality checks; use [$ci-slopgate](../ci-slopgate/SKILL.md) if a gate needs repair.

Adapt reviews to the product's actual surface. Use deterministic checks for fixed contracts, browser automation for repeatable interactions, and agents for exploration and judgment. Reuse existing checks. Don't count an unrun review as a pass.

## Fix and recheck

For each review, record what passed, what failed, and the evidence. Reproduce disputed findings.

For consequential or recurring failures, have verification preserve a replayable regression case using the [failure-to-eval handoff](../skill-improver/references/failure-to-eval.md) when practical. Give reviewers the task, safe starting environment, and evidence needed to run it; keep expected answers and prior diagnoses separate from executors. Reuse relevant cases on the final version. Do not create a suite for every small fix or start a skill-optimization loop unless that work is in scope.

Keep ownership of authorized fixes when invoking other skills: their review reports feed this fix-and-recheck loop. Fix failures that prevent the agreed outcome, including pre-existing defects in that path, then have reviewers recheck the fixes and anything else they affect. Keep repeating until every relevant review passes on the final version. Don't lower the success criteria to get a pass.

If something blocks a review, explain what is missing and keep working on what you can.

When waiting for a PR to turn green, set a recurring 15-minute check-in to inspect the latest checks and fix failures. Stop it once the failures are fixed and the checks pass.

For improvement claims, compare equivalent workloads over the requested scope, including failures and retries; distinguish component gains from whole-job results.

Complete the goal only when the agreed outcome is delivered and the reviews pass. If deployment is part of the job, verify it with [$verify-deploy](../verify-deploy/SKILL.md). Report what works, how it was tested, and any remaining limitations.
