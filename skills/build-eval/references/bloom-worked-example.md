# Worked example: evaluating Bloom's investing assistant

This is a historical example from 2026-10-12, not a prescribed rubric, model ranking, case count, or spending authorization. It demonstrates a useful evaluation workflow and the limits found during execution.

## Task and user standard

The user wanted Bloom's real chat responses evaluated and improved, with the parent assistant reviewing the answers. Existing Markdown scenarios and real-chat inputs supplied tasks such as comparing investments, understanding earnings, asking about an unspecified idea, and researching an onboarding stock without assuming ownership.

The shared rubric covered clarity, utility, and accuracy, with case-specific requirements layered on top. A pass required all applicable criteria. A missing source could be acknowledged honestly, but that did not automatically satisfy a request for sourced research. Human ratings were not collected. The parent assistant both developed candidates and judged them with identities visible, so these are provisional, non-blind AI judgments.

The user explicitly authorized requested `llm_tests` API spending below $20. That permission belonged to this task. The existing two-stage application used its configured model APIs; replacing it with a standalone subscription chat would have changed the subject. No additional model-judge calls were needed.

## One failure, from request to correction

Request: “Compare AAPL and MSFT as investments.”

The case required a comparison across at least two dimensions with specific data for each company. The shared accuracy criterion also required the conclusions to agree with the evidence.

| Captured fact | AAPL | MSFT |
| --- | ---: | ---: |
| Price-to-earnings ratio | 38.96 | 29.88 |
| Revenue growth, last 12 months | 14.2% | 17.8% |

The baseline answer referred to “Apple’s lower earnings multiple,” then displayed rounded P/E values of 39.0 for AAPL and 29.9 for MSFT. Later prose correctly favored Microsoft's lower P/E. The answer contained a direct contradiction despite covering multiple dimensions and presenting a readable table.

The parent judgment marked accuracy and overall success as failed. A grader checking only for a comparison, a table, or the presence of correct numbers could miss this. The controlling evidence was the company-to-metric mapping and the direction of the comparison, not which stock the reviewer preferred overall.

Candidate instructions asked the synthesizer to bind figures to company, metric, units, and period, then check the inequality. A Luna configuration still reversed the conclusion on a later run. The selected C9 configuration combined revised synthesis/gathering instructions, Sol with low reasoning, and a 15-second first-token timeout. It correctly distinguished Microsoft's lower earnings multiple from Apple's stronger cash-generation measures. This was a bundled configuration comparison, not proof that one prompt sentence or model alone caused the gain.

## Why complete evidence mattered

The experiment captured the actual request, full answer, gathered data, exact synthesis inputs, tool events, returned model identities, usage, and timing. Every grade linked to its runtime record. The ordinary CI judge received the answer and tool names, which was insufficient to establish whether figures or citations matched retrieved evidence.

Three measurement issues surfaced:

- Local search lacked `SERPER_KEY`; its empty results looked like searches that found no corroboration. Both configurations used the corrected environment in subsequent live comparisons. That repair was not credited as a candidate improvement.
- Early replay code froze initial gathering but allowed escalation to reach live retrieval. Those attempts were preserved and replaced with runs that froze both paths.
- A later readiness audit reproduced `Incomplete Markdown scenario: MEM-2` in the standard loader. The experiment's explicit case files had run, but that did not establish that the normal CI suite could load its maintained document.

## Selection and separate claims

All 23 previously exposed cases became development data for the additional variants. C8 passed fresh validation, then regressed on the final IRA case: it asked for a tax bracket without explaining Roth versus traditional accounts. C8 was rejected. Those cases became development data before C9 was revised; C9 then used new validation and final groups.

| Observed comparison | Baseline | C9 |
| --- | ---: | ---: |
| Original 23 cases, matched recorded-evidence replay | 18/23 | 22/23 |
| Four new live validation cases | 3/4 | 4/4 |
| Four new live final cases | 3/4 | 4/4 |
| Median synthesis/orchestration time on the original replay set | 2.51s | 3.03s |
| Reported upstream inference subtotal for that replay set | $0.00384345 | $0.2279025 |

Two baseline attempts in that replay comparison lacked usage receipts; an exact cost ratio was not established. Across both experiment rounds, reported inference totaled approximately $1.84, with conservative exposure plus contingency of $12.55. Those figures are not the exact bill: some attempts lacked receipts, one early nested call was unmetered, and data-provider charges were not itemized.

C9 passed 34 of 35 expanded development replays. The frozen citation case still lacked required URLs. Its valid portfolio allocation in replay did not establish a live fix: baseline and C8 had timed out during live portfolio retrieval. Keep that integration limitation visible rather than converting the replay pass into a claim that the whole product works.

A previous 81-word answer failed an 80-word requirement. It remained a format failure, distinct from the financial contradiction. Neither requirement was waived to improve the score. Targeted repeat generations checked the inconsistent comparison, sentence count, and IRA behavior; they did not increase independent case coverage.

The run also exposed a process weakness: the initially declared 120-execution limit was extended to 180, with 174 executions completed in the second round. Preserve this history as a deviation to learn from. Future plans should distinguish batch estimates from hard caps before running; remaining spending allowance alone does not authorize extending a hard cap.

## Reusable workflow and evidence pointers

Reuse the workflow: real task and runtime, explicit user criteria, complete attempts, failure diagnosis, a bounded revision, separate replay/live measurements, and fresh confirmation. Do not copy the investing criteria into unrelated tasks or treat these small, repeatedly selected sets as production accuracy estimates. No configuration was deployed by this experiment.

The source records live under `<Bloom checkout>/llm_tests/experiments/2026-10-12-hill-climb/`. The baseline checkout was commit `ba6ba87ceda398b0049f86249aba48102377521d`.

- `manifest.json`, `grades.json`, and `results/baseline-replay-TC-3-1.json`: original conditions, baseline judgment, and contradictory answer.
- `round2/c9.json` and `round2/results/c9-replay-TC-3-1.json`: exact selected configuration and revised answer/evidence.
- `round2/decisions.json`, `round2/grades.json`, `round2/manifest.json`, and `round2/summary.json`: rejected candidates, criterion judgments, consumed holdouts, limit revision, and counts.
- `spend-ledger.json` and `round2/report.html`: cumulative model receipts and the inspectable report.

These are local historical artifacts, not bundled skill fixtures or publicly accessible verification records. The excerpts and measurements above are a self-contained account; raw traces and credentials are not included in this public repository. If unavailable, report that limit rather than claiming a fresh verification from this narrative. Keep their diagnosis and grades outside a subject's inputs when reusing the cases.
