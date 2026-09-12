# Skill maintenance procedures

Use these checks after structural review, when a skill gives incorrect guidance, or before a
large batch of skills is loaded. They are portable across Codex installations; substitute the
actual skill directory and repository paths.

## Drift and dependency paths

1. Inventory every repository path, reference link, line count, constant, enum, feature, branch,
   and CLI subcommand named by the skill.
2. Resolve each literal relative path from the file that contains it. Verify that the resolved
   target exists and is the intended target. Do not pass a check merely because a file with the
   same basename exists elsewhere; `references/foo.md` and `other/foo.md` are different targets.
3. Check referenced files with `wc -l` and inspect meaningful contract changes. A changed size is
   a signal to review, not proof of breakage.
4. Confirm enumerated constants and features against source, and confirm the repository's actual
   default branch. Inspect entrypoints before safe CLI probes; even `--help` can have side effects.
5. Normalize paths to the installation's portable form. Remove references to reverted, unmerged,
   or machine-specific files unless the skill explicitly requires them.

For reference-heavy skills, check both directions: needed references are reachable from the
router, and local links resolve to the intended files. An unlinked resource is a review candidate,
not automatically a defect; it may be consumed by a script or packaging process.

Use [the reference checker](../scripts/check_reference_health.py) for Markdown file links:

```bash
python3 /path/to/skill-audit/scripts/check_reference_health.py /path/to/target-skill --orphans
```

It checks exact targets and follows reference-to-reference links for reachability. Inspect its
reported candidates in context. It does not establish remote URL health, promised content,
runtime availability, or paths embedded in shell commands; inspect those separately with `rg`
and safe runtime probes. Run `--help` for the parser's supported Markdown forms and limitations.

When changing the checker, run its [regression tests](../scripts/test_check_reference_health.py):

```bash
python3 -B /path/to/skill-audit/scripts/test_check_reference_health.py
```

## Measuring budget

Measure UTF-8 bytes for descriptions and bodies (`wc -c`) and use `ceil(bytes / 4)` only as a
rough token estimate. Report the measured file, whether its description is preloaded, and which
references are loaded on demand. Apply the host's documented context or size policy where one
exists; do not invent a universal token cutoff. Keep descriptions short and evergreen, especially
for preloaded skills, and move durable detail into linked references when loading cost or routing
clarity warrants it. Check whether volatile text actually changes between loads before claiming
cache churn; a static word such as “today” does not itself invalidate a cache.

## Usage evidence

Search the installation's episode and session records for the exact skill name and its aliases.
Count observed triggers over useful windows such as 30 and 90 days, and record the latest observed
use. Distinguish zero observed uses from unavailable telemetry, an unindexed alias, a disabled
logging source, and a skill used only by automation. Do not call a skill unused when the evidence
source was absent; report the evidence coverage and confidence instead.

## Comparing a fork with upstream

1. Establish lineage from stable opening text or frontmatter such as `author` or `homepage`; a
   renamed or relocated skill may not match by name.
2. Compare with the current upstream file or API content, not an old local checkout. Record the
   upstream revision or retrieval date so the comparison is reproducible.
3. Separate upstream changes from private runbook content. Preserve local authorization rules,
   operational constraints, and private procedures unless the owner explicitly changes them.
   Summarize the small actionable delta instead of proposing a wholesale “update” of a private
   fork.

## Gap search and consolidation

When checking whether a capability already exists, search the complete skills tree with capability
verbs and implementation terms, including sibling directories and references. A description-only
scan is preliminary: open the matching skill and verify that it covers the requested workflow.

Before consolidating a large or append-only skill, map its sections, links, and duplicate-topic
clusters. For each proposed canonical reference, record which source sections it absorbs and
preserve unique commands, caveats, provenance, authorization, and approval requirements. Merge
equivalent explanations when their requirements survive; use the coverage map to detect losses.
Consolidate or retire separate skills only within the user's authorized scope.

Create and inspect canonical files before retiring originals. Prefer a recoverable move or trash
operation. Rewrite the main skill as a router with grouped links, then re-run both orphan and
broken-link checks. Re-measure the router and verify that each retained procedure is reachable.
