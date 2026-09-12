# Experiment records, candidate pools, and review

Use this reference when an experiment needs comparable runs, checkpoint recovery, multiple candidates, or a shareable local review. Small edits do not require an experiment. The helper analyzes recorded evidence; it does not launch agents, choose a provider, or install a skill.

## Freeze the comparison

Record the task, skill/resource hashes, model and reasoning settings, tool availability, fixture revision, rubric version, budget, train/validation/test membership, repetitions, critical cases, minimum paired observations, and minimum useful gain before running. A minimum useful gain is a product decision, not a significance threshold. Keep the execution request separate from expected answers and diagnosis notes.

A useful directory has `manifest.json`, immutable baseline/candidate snapshots, executor inputs, raw outputs/traces, a run ledger, and a checkpoint. Store task-specific artifacts in the current project, not inside the installed skill. Save authorizations and restrictions as part of the manifest without credentials. A candidate includes its references and scripts; hashing only SKILL.md misses behavior changes.

## Results schema and analyzer

[review_results.py](../scripts/review_results.py) accepts this JSON shape. Scores are normalized rubric scores in [0,1]; `passed` is the independently defined task pass condition. `critical` cases must pass, even when the baseline also failed them. Every successful run needs an evidence path or identifier.

```json
{
  "schema_version": 1,
  "baseline": "base",
  "candidates": ["base", "candidate-a"],
  "min_pairs": 1,
  "min_mean_gain": 0.05,
  "cases": [
    {"id": "training-case", "split": "train", "repetitions": 1},
    {"id": "validation-case", "split": "validation", "critical": true, "repetitions": 1}
  ],
  "runs": [
    {"candidate": "base", "case": "training-case", "repeat": 0, "status": "ok", "score": 0.4, "passed": true, "evidence": "outputs/base-training.txt"},
    {"candidate": "candidate-a", "case": "training-case", "repeat": 0, "status": "ok", "score": 0.7, "passed": true, "evidence": "outputs/a-training.txt"},
    {"candidate": "base", "case": "validation-case", "repeat": 0, "status": "ok", "score": 0.5, "passed": true, "evidence": "outputs/base-validation.txt"},
    {"candidate": "candidate-a", "case": "validation-case", "repeat": 0, "status": "ok", "score": 0.8, "passed": true, "evidence": "outputs/a-validation.txt"}
  ]
}
```

This tiny example demonstrates the file format, not adequate evidence for a general improvement claim. Include `tokens`, `cost`, and `seconds` when measured. Missing fields are reported as missing measurements. Use `error` or `skipped` status for incomplete execution; do not convert infrastructure failure into a model score of zero or omit it silently. Declare expected repetitions in advance so missing runs remain visible.

From the installed skill directory:

```bash
python3 -B scripts/review_results.py /path/to/run/results.json --json-out /path/to/run/review.json --html-out /path/to/run/review.html
```

Use fresh output paths; the helper refuses replacement. It validates inputs, compares the same validation case/repeat pairs, rejects failed critical cases, marks incomplete evidence inconclusive, and reports a descriptive gain. `eligible_for_review` means the predeclared descriptive threshold was met; it does not mean statistically significant, ready to deploy, or authorized to install. Open the evidence files and inspect the actual outputs before deciding. The local HTML view is generated without remote assets or external publication.

The helper deliberately excludes sealed test runs from candidate selection and trigger metrics. Compare final baseline/selected-candidate test outputs separately after selection; report any regression without tuning against that test set.

## Multiple candidates

Use a training score vector with one component per matched case/repetition. A candidate dominates another only when it is at least as good on every component and better on at least one. The helper reports the nondominated training frontier; incomplete candidate vectors are excluded. A frontier member is not necessarily globally better and does not automatically deserve more execution budget.

Choose parents on training evidence and diagnosis, reserving validation for the predeclared decision. If sampling by tasks won, record the RNG seed, weighting rule, and selected parent. Merge candidates only when changes address compatible failures; run the merged artifact as a new candidate rather than averaging parent scores. Keep critical constraints visible in every merge.

## Statistical gates

Do not copy a sequential acceptance script merely because it uses a named method. Repeated peeking, adaptive candidate selection, correlated repeats, and reusing validation examples can invalidate an inference. Per-candidate error control is not automatically experiment-wide control. Use a validated project implementation only after checking its assumptions, candidate-budget allocation, dependence handling, and negative controls. Otherwise report descriptive paired results and uncertainty. No PACE or other statistical guarantee is claimed by the bundled analyzer.

## Checkpoint and resume

Checkpoint the schema/rubric version, immutable artifact hashes, split IDs, completed and pending run keys, candidate lineage, rejected changes/reasons, resource usage, remaining budget, and selected candidate if any. Write checkpoints atomically. On resume, verify hashes and configuration before skipping a run; existence of an output filename is not proof of completion. Preserve split membership and rejected edits. A changed rubric or fixture requires a new comparison or explicit reruns, not a silent merged score history.

For mining past runs, use the runtime's authorized export or project trace files. Record source session/run IDs and redact unrelated private content. A textual mention of a skill is not proof that it was invoked. Deduplicate similar failures, preserve representative raw artifacts, and separate optimization cases from held-out checks. Do not import a Hermes database path into a Codex workflow.

## Regression checks

The [test file](../scripts/test_review_results.py) exercises missing evidence, critical failures, test isolation, trigger accounting, and malformed records:

```bash
python3 -B scripts/test_review_results.py
```
