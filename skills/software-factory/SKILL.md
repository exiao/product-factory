---
name: software-factory
description: Coordinate product discovery through implementation and verification, or perform a focused comparison, evidence trace, or artifact review. Use for unresolved product decisions; clear contained fixes go directly to the relevant implementation skill.
---

# Software Factory

Turn product judgment into an implemented and verified outcome without losing agreed intent between steps. The user's current instructions take precedence. Preserve authorization, scope and settled decisions; this skill does not authorize additional publishing, deployment, spending or messages.

## Choose the scope

Commands below are conversational operations, not shell commands or standalone skills. Infer the operation from ordinary language; users need not memorize names.

- **Focused request:** run only the selected operation on the named artifact. Read its linked playbook and relevant specialist guidance. Do not launch discovery, maps, prototypes or implementation as a side effect. Review-only work reports findings without editing. A request to revise or fix authorizes the bounded change and appropriate verification.
- **Delegated outcome:** use [product workflow](references/product-workflow.md) when audience, promise, behavior or direction is unresolved. Start by stating or reusing the short vision. Sequence work by dependencies and uncertainty, reuse agreements, and continue through the authorized finish line. An intermediate focused operation does not cancel the larger assignment.
- **Settled implementation or clear fix:** go directly to the relevant design, implementation or verification skill; do not reopen discovery.
- **Advice or bare invocation:** recommend up to three context-relevant next operations and explain the leading choice. Advice does not execute them. If the surrounding conversation already supplies an actionable request, follow it rather than showing a menu.

## One useful loop, removal first

For prototype work, define one core loop per direction: starting material → product contribution → useful result → accept or revise. Reuse the settled loop and name what to remove before adding capabilities. Research findings describe the domain; they do not automatically become features, screens, personas, or separate prototypes. Keep only what the loop needs for its outcome, meaningful control, accessibility, and recovery. Grouping or hiding a capability does not justify building it.

Demonstrate the useful transformation on concrete starting material before broad UI investment, using the workflow's worked-sample guidance when output quality matters. Preserve the contribution when simplifying: fewer controls alone cannot make an unhelpful mechanism useful. Carry the loop and exclusions through handoffs and judge the result, not the number of working controls. Stop at the agreed finish line; further breadth needs a task-based reason.

Explicitly requested alternatives remain separate focused experiments. Preserve requested product scope and established behavior; a local improvement does not authorize deleting unrelated features. This is a decision rule within existing work, not another document, discovery phase, or approval gate.

## Operations

| Operation | Kind | Result and guidance |
|---|---|---|
| `recommend [project/artifact]` | Advise | Current decision, recommended next operation and why; [focused work](references/focused-work.md) |
| `compare [approaches]` | Evaluate | Same-input worked comparison, tradeoffs and smallest useful test; [focused work](references/focused-work.md) |
| `trace [promise/artifact]` | Inspect | Links from problem and evidence through intervention, criterion and observed result; [focused work](references/focused-work.md) |
| `critique [idea/storyboard]` | Inspect | Identify unexplained benefits and hidden work; propose a test; [focused work](references/focused-work.md) |
| `question`, `check`, `reframe` | Inspect / Revise | [$people-problems](../people-problems/SKILL.md) |
| `inspect`, `critique`, `audit` | Inspect / Revise | [$interaction-design](../interaction-design/SKILL.md) |
| `sharpen`, `assess`, `define` | Revise / Evaluate | [$acceptance-criteria](../acceptance-criteria/SKILL.md) |
| `develop [product]` | Coordinate | [Product workflow](references/product-workflow.md) |

A lens reveals something about the current artifact; an action changes it. Choose from the user's intent. For example, “highlight hidden user work” annotates the current flow; “remove the unnecessary setup step” calls for a scoped revision. Preserve the original object and show the affected portion, a before/after excerpt, or an annotated screenshot instead of replacing whole documents unnecessarily. Keep observations separate from suggested changes.

## Preserve evidence across operations

Use the existing project record for scope, decisions, criteria, artifacts and open questions. No new schema, dashboard or duplicate ledger is required. Give problems and criteria stable identifiers when they must survive multiple handoffs; reuse existing IDs and source links.

Carry reported experience, observed behavior, inference and simulation as distinct evidence types. Approval selects a direction; it does not verify an assumption. Passing a narrower technical check does not pass the full user promise. Check the underlying source or execution result before strengthening a claim; if unavailable, retain uncertainty.

Keep idea generation flexible within the agreed person, input and outcome. Use tools for checkable facts, artifact existence and executed behavior; use anchored judgment for usefulness and design. A model-written explanation or valid format is not proof. Do not add a model call for a task that an existing deterministic tool already performs adequately.

## Hand off and show progress

At a consequential handoff, include only what the next operation needs, inline or in the existing record:

- Source artifact or version and the specific target/operation.
- Agreed outcome, constraints, exclusions and settled decisions.
- Result or localized change, linked evidence and criterion status where relevant.
- Remaining uncertainty and the next useful operation or unresolved user decision.

Link back to raw evidence rather than passing only a summary that may have lost attribution. Missing evidence remains missing. Keep unrelated content and approved criterion wording intact.

Lead a checkpoint with the current artifact, what changed, the question still open and the recommended next step. Ask only for consequential unresolved choices that have not been delegated. Updates need no response, settled decisions need no repeated approval, and silence is not agreement. Continue independent authorized work while a required decision is pending. Stop focused work at its requested result; stop delegated work at the agreed verified finish line.
