# From source material to a local benchmark

Use when building a benchmark from source material. Keep the existing runner and layout when suitable.

## Find representative instances

Name the repeating task and use the supplied scope to find instances in files, chat, or repo history. For fixes, capture the input revision before the fix; the fix and reviewer response are outcome evidence, not normal subject inputs. Record the exact revision or document version, relevant location, and why the example belongs. Stay within the supplied source scope.

Gather what an instance normally arrives with: prompt, files and formats, approximate size, permitted tools, and expected answer or artifact. Extract good and weak behavior from accepted work, corrections, rejections, and the user's stated criteria. A historical answer is evidence, not automatically the only valid answer. Compute checkable results and record their derivation; label inferred keys and plausible mistakes as proposals.

Choose categories that exercise different requirements or failure modes. Include ordinary work, hard cases, and clean/no-action cases when relevant. If there is only one real instance, begin there and state the coverage limit. Mark generated stand-ins and synthetic cases separately from observed work. Group related revisions, duplicates, and examples from the same incident into the same split to avoid leaking development examples into held-out tests.

Separate targeted regression cases from representative coverage in selection records and reporting. Do not build the entire suite from one model's failures. Explain why challenging cases matter independently of that model's score, and label inferred difficulty until reviewed. Production traffic can underrepresent valuable tasks users avoid because they expect failure; add justified challenge cases without presenting their frequency as observed traffic.

## Keep a small preparation record

Reuse existing records or one compact manifest; do not require a multi-document preparation package. Retain the task and proposed conditions, source paths and versions, provenance, subject/grader roles, candidate cases, cited outcome evidence, and development/held-out split. Keep these supporting details behind the results surface.

Keep source files with descriptive names, grouped by useful kinds. Redact when enough; generate stand-ins only when needed and preserve the structure and messiness that make the task difficult. Create every referenced fixture and record how redaction, summarization, or other changes affect the test. Preserve originals locally when permitted; keep private sources and traces out of version control unless explicitly intended.

The authoring records can contain answers. Never hand the authoring directory to the subject. Build each subject environment from an explicit input allowlist, with grader evidence, keys, follow-up fixes, and calibration examples outside its readable context. Folder names alone do not isolate data: check actual filesystem mounts, tool access, retrieval sources, and prompt assembly. Worked examples may be supplied only when declared part of the tested condition and separate from test answers.

## Design and execute here

Write a short concrete plan in the existing record: selected seed IDs, task wording, categories, output expectations, criteria with evidence, any proposed levels/weights or critical failures, evaluator choice, runtime, split, factors varied/held fixed, quality/cost/time measurements, and bounded pilot size. State the plan and proceed without confirmation for subscription CLI jobs or already authorized API jobs; follow the main skill's spending rules for other APIs. Use weights only when an aggregate is useful; otherwise report each criterion separately. Mark proposed criteria and unresolved decisions.

Choose verification according to the required outcome:

| Outcome | Inspectable evidence |
| --- | --- |
| Text, labels, analysis over frozen material | Saved answer against cited facts and an anchored rubric |
| Spreadsheet, document, slides, or another file | Actual produced file, relevant structure/content checks, rendering or human/model review where needed |
| Code or tool actions | Execution, tests, traces, and resulting state in a safe repeatable environment |

Produced files do not automatically require Harbor; use it when isolation or repeatable tools/state helps. Do not turn “tests pass” into “code looks correct” to fit an answer-only grader. If the needed runtime is unavailable, preserve the original criterion as untested; propose a narrower test with explicit exclusions instead of claiming equivalence. Freeze external facts unless freshness itself is being tested; record how time-dependent answers will be verified.

Follow the main skill's setup, calibration, and trial steps. If blocked, finish independent preparation and report the missing dependency.

## Preflight and local handoff

Check the generated eval using its actual loader and runtime, not just the manifest:

- Every referenced input and evidence path resolves; cited locations support the key and belong to the frozen version.
- Files can be read in the selected runtime. Inspect extracted content for lost tables, sheets, truncation, or unsupported formats; record any transformations.
- Subject-visible prompts, files, and tools contain only allowed inputs. Verify answer/evidence separation in a fresh subject environment.
- Commands resolve local dependencies, paths, and resets; outputs and grades are retained with versions. Run controls and a bounded real trial when available; distinguish packaging checks from scoring validity.

Deliver the local eval path, exact generation/grading/review commands, actual pilot results, and limitations. Use the main skill's review instructions for the handoff.
