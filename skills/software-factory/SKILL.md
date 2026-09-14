---
name: software-factory
description: Run product work through a fixed sequence from vision and research to prototypes, implementation and verification; also support focused operations on individual artifacts. Use for unresolved product decisions; clear contained fixes go directly to the relevant implementation skill.
---

# Software Factory

Turn product judgment into an implemented and verified outcome without losing agreed intent between steps. The user's current instructions take precedence. Preserve authorization, scope and settled decisions; this skill does not authorize additional publishing, deployment, spending or messages.

## Choose the scope

Commands below are conversational operations, not shell commands or standalone skills. Infer the operation from ordinary language; users need not memorize names.

- **Focused request:** run only the selected operation on the named artifact. Read its linked playbook and relevant specialist guidance. Do not launch discovery, maps, prototypes or implementation as a side effect. Review-only work reports findings without editing. A request to revise or fix authorizes the bounded change and appropriate verification.
- **Delegated outcome:** use [product workflow](references/product-workflow.md) when audience, promise, behavior or direction is unresolved. Start by stating or reusing the short vision. Follow the default sequence below, reuse agreements, and continue through the authorized finish line. An intermediate focused operation does not cancel the larger assignment.
- **Settled implementation or clear fix:** go directly to the relevant design, implementation or verification skill; do not reopen discovery.
- **Advice or bare invocation:** recommend up to three context-relevant next operations and explain the leading choice. Advice does not execute them. If the surrounding conversation already supplies an actionable request, follow it rather than showing a menu.

## Default sequence

For a product outcome, follow this sequence in order. Read [product workflow](references/product-workflow.md) for execution detail and the linked specialist skills at their stages. Focused operations above remain available when the user asks for a specific step; do not turn a product assignment into a menu of optional operations.

| Stage | Required result before advancing |
|---|---|
| 1. Vision | Person, situation, promised outcome, scope and exclusions. |
| 2. Research and problem framing | Linked desk research, human problem statements and grounded empathy maps. Present the problem checkpoint; resolve consequential audience or job ambiguity. |
| 3. Outcome criteria | Observable success criteria and the evidence needed to judge them. |
| 4. Alternatives and storyboards | Different mechanisms for an unresolved direction, illustrated storyboards, and a same-input worked sample when output quality matters. Present the direction checkpoint; use the user's selection or an explicitly delegated choice. |
| 5. Interaction prototype | One core loop, exclusions, wireflow and a working clickable low-fi prototype with simulated behavior labeled. |
| 6. Prototype study and revision | Synthetic UX walkthrough of the first usable prototype, annotated screenshots for visual products, fixes and affected-interaction rechecks. Present the first-prototype checkpoint before substantial polish. |
| 7. Design and detailed criteria | Refined design and behavior, error and recovery criteria before implementing each slice. |
| 8. Build and verify | Implement, review, exercise the real workflow against the original criteria, fix and recheck; report evidence and limits. |

Start at the earliest incomplete stage. A stage is satisfied only by an inspected artifact or evidence covering the current scope; naming it in a plan does not complete it. Reuse sufficient work by linking it, without regenerating it or asking for approval again. At handoffs, state the stage, its result and the next stage in the existing record; no separate tracking system is needed.

The required outputs are not discretionary suggestions. Do not skip or replace one merely because another experiment seems more informative. Honor an explicit user omission or scope change, and stop at a requested earlier deliverable. If an output cannot be produced, disclose the gap and continue independent work without claiming that stage complete or starting work that depends on it. Journey mapping remains optional for sequence and handoff questions; strategy, commercial validation and desirability work supplement this sequence when their stated conditions apply.

Checkpoints are progress updates unless a consequential unresolved choice requires the user's answer. Delegation authorizes choosing within scope; it does not erase required outputs. A focused request during ongoing product work returns to the next incomplete stage afterward unless the user changes the assignment.

## One useful loop, removal first

For prototype work, define one core loop per direction: starting material → product contribution → useful result → accept or revise. Reuse the settled loop and name what to remove before adding capabilities. Research findings describe the domain; they do not automatically become features, screens, personas, or separate prototypes. Keep only what the loop needs for its outcome, meaningful control, accessibility, and recovery. Grouping or hiding a capability does not justify building it.

Demonstrate the useful transformation on concrete starting material before broad UI investment, using the workflow's worked-sample guidance when output quality matters. Preserve the contribution when simplifying: fewer controls alone cannot make an unhelpful mechanism useful. Carry the loop and exclusions through handoffs and judge the result, not the number of working controls. Stop at the agreed finish line; further breadth needs a task-based reason.

Explicitly requested alternatives remain separate focused experiments. Preserve requested product scope and established behavior; a local improvement does not authorize deleting unrelated features. This is a decision rule within existing work, not another document, discovery phase, or approval gate.

## Review artifacts with the user

Use [artifact-review](../artifact-review/SKILL.md) when creating an interactive site for the user to judge generated work. It owns concise artifact-centered cards, question-specific primary controls, and the always-available further-work, comment and dismiss/archive actions. Software Factory retains the fixed stage order, project record and execution responsibility. Specialized review mechanisms remain available without becoming a mandatory questionnaire. Carry responses back into the artifact and next authorized step; a local save alone is not executed work.

## Operations

| Operation | Kind | Result and guidance |
|---|---|---|
| `recommend [project/artifact]` | Advise | Current decision, recommended next operation and why; [focused work](references/focused-work.md) |
| `compare [approaches]` | Evaluate | Same-input worked comparison, tradeoffs and smallest useful test; [focused work](references/focused-work.md) |
| `trace [promise/artifact]` | Inspect | Links from problem and evidence through intervention, criterion and observed result; [focused work](references/focused-work.md) |
| `critique [idea/storyboard]` | Inspect | Identify unexplained benefits and hidden work; propose a test; [focused work](references/focused-work.md) |
| `question`, `check`, `reframe` | Inspect / Revise | [$people-problems](../people-problems/SKILL.md) |
| `inspect`, `critique`, `audit [flow/surface]` | Inspect / Revise | [$interaction-design](../interaction-design/SKILL.md) |
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
