# Reduction review regression cases

Use when evaluating changes to the skill, not during ordinary PR reviews. These
cases check decisions, not whether the report repeats the skill's headings.
They do not establish a general improvement rate.

Give a fresh evaluator only `SKILL.md`, the case prompt, and the input snapshot.
Keep the scoring notes, later revisions, prior reviews, and expected reductions
out of its context. Use read-only isolated snapshots; no network, credentials,
pushes, merges, or production requests are needed. The coordinator scores the
result afterward. Do not reward a particular helper name or line-count target.

## Case A: Working implementation with duplicated responsibilities

Source: Bloom PR #2669 before its review reductions, commit
`7a70f365e`, base `d6a411a0b`, in the Bloom repository. A temporary detached
worktree at the head preserves imports and caller context. Do not pull or update
this historical fixture. If the commits are unavailable, mark the case unavailable
rather than substituting the already-reduced implementation.

Evaluator prompt:

> Use the supplied code-review skill for a read-only review of the change from
> d6a411a0b to 7a70f365e. The requested outcome is direct Cerebras Qwen 3.8 27B
> gathering with GPT-OSS fallback, for both native tools and JSON planning.
> Preserve existing public behavior. Review the gatherer adapter, its callers,
> configuration, and tests; report correctness and simplification findings.
> Do not inspect later commits or prior reviews. Do not read env files or call
> providers. If a check cannot run, identify the limitation rather than claiming
> it passed.

Coordinator scoring (withhold from evaluator):

- Identifies shared provider selection across native/JSON calls as a concrete
  alternative, rather than merely asserting that both paths need an adapter.
- Identifies duplicated SDK argument reconstruction and repeated test setup;
  proposes consolidation while preserving distinct routing/error cases.
- Names preservation checks for explicit model overrides, missing-key fallback,
  schema compatibility, and no replay after a streamed event. Does not propose
  removing required fallback or relying on unavailable SDK behavior.
- Separates bug findings from simplification, and distinguishes proposed checks
  from executed evidence. A list of filenames or “no blocking issues” alone fails.

Historical comparison for the coordinator only: the later reviews removed 42
lines of test scaffolding, then another 20 production and 45 test lines. These
figures are evidence that a smaller implementation existed, not scoring quotas.

## Case B: Small implementation with no justified cut

Create a temporary repository with an empty committed base and these staged files:

`symbols.py`:

```python
def unique_symbols(symbols: list[str]) -> list[str]:
    """Preserve first-seen order of already-validated symbol strings."""
    return list(dict.fromkeys(symbols))
```

`test_symbols.py`:

```python
from symbols import unique_symbols

assert unique_symbols([]) == []
assert unique_symbols(["MSFT", "AAPL", "MSFT"]) == ["MSFT", "AAPL"]
assert unique_symbols(["aapl", "AAPL"]) == ["aapl", "AAPL"]
```

Evaluator prompt:

> Use the supplied code-review skill for a read-only review of the staged change.
> Return distinct, already-validated symbol strings in first-seen order, preserving
> case. The input may be empty and must not be mutated. Run the available check
> when useful. Do not edit files or inspect other review cases.

Coordinator scoring (withhold from evaluator): retain the standard-library
implementation unless there is a demonstrated improvement preserving the full
contract. An unordered set, case normalization, erased regression coverage, or
new abstraction to manufacture a reduction fails. `python test_symbols.py` is
an executable check; comparing output to the rubric is coordinator work.

## Recording a run

Record the skill version/hash, case revision, evaluator model, observed findings,
checks actually run, and pass/fail/partial outcome outside the skill entrypoint.
A successful single run is a bounded smoke test, not proof that all future
reviews will simplify correctly. To measure improvement, compare the old and
candidate skills on the same cases with independent evaluator contexts.
