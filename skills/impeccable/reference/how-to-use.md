# How to use Impeccable

Read this for workflow advice, command selection, or examples of effective requests. Advice alone does not run setup, write context files, or change project defaults. For execution, follow SKILL.md and the selected command reference; this guide is not an extra checklist.

## Give it context once

Use `$impeccable init` to capture audience, user goals, constraints, and product truth in PRODUCT.md. For an existing visual identity worth keeping, use `$impeccable document` to record DESIGN.md and its token sidecar. Review the result: accidental inconsistencies should not become design rules. Reuse current context instead of repeating setup for every task.

Missing PRODUCT.md does not block a narrow refinement of existing UI. Missing DESIGN.md does not authorize a redesign; existing components and rendered pages remain evidence. Setup and prerequisites are defined in [init.md](init.md) and [new-work.md](new-work.md).

Choose the mode for the surface: Persuade for deciding and acting, Operate for completing tasks, Read for understanding, Experience for encountering the work itself. A dashboard and its marketing page can have different modes.

## Choose the smallest useful workflow

| What you need | Request |
|---|---|
| Diagnose an unclear design problem | `$impeccable critique <surface>` |
| Improve a known issue | Describe the outcome directly, or use `layout`, `typeset`, `distill`, or `clarify` |
| Resolve a feature's flow before building | `$impeccable shape <feature>` |
| Replace the visual identity | Explicitly ask for a redesign and name the product facts and behavior to preserve |
| Compare alternatives on a running web page | `$impeccable live` |
| Finish an implemented flow | `$impeccable polish <surface>` |
| Find accessibility, performance, or responsive defects | `$impeccable audit <surface>` |

These are alternatives, not a sequence to run on every task. Critique and audit report findings; shape plans. If you want implementation too, say so, for example: “Critique this screen, then fix the highest-impact problems within the existing design.” Polish preserves the identity; it is not a shortcut for redesign.

## Choose code-first or mockup-first deliberately

For routine product UI and extensions of an established system, recommend **code-first**: work in real components and inspect the running result. For a new visual identity or an ambitious marketing surface, consider **mockup-first** (comp-first): compare visual directions before translating the approved image into code. That translation and fidelity review take additional time.

These are recommendations, not new defaults. Honor the user's request and saved preference. For new work with image generation available, an unset buildPath currently defaults to comp-first. Say “Use code-first and save that preference for this project” to choose a durable default; [init.md](init.md#step-5-record-workflow-defaults) defines how it is recorded. Ordinary refinements do not need a new direction round.

## Write a useful brief

Name the target, user outcome, what must stay, and evidence the agent can inspect. Distinguish review from implementation.

> $impeccable improve the billing settings screen so users can understand their plan and change payment details. Preserve our typography, colors, factual copy, and save behavior. Follow the existing account settings screen. Build directly in code, fix the highest-impact usability problems, verify the main task on desktop and mobile, and show before/after screenshots.

Give concrete feedback: “Keep the clearer comparison, but restore the billing toggle above it” is more actionable than “make it better.”

## Verify the experience

Use the real task and relevant states, sizes, and input methods as evidence. A clean detector scan is not a design verdict. Follow the selected playbook's bounded verification; do not add repeated scans or an unrelated command chain.

For web projects, `$impeccable hooks status` checks configuration; installation alone does not establish that hooks run. Follow [hooks.md](hooks.md) for setup and Codex approval. The bundled detector and live overlay are web-only. Native apps use platform-specific audit/adapt guidance and simulator or device evidence.

Further guidance: [official workflows](https://impeccable.style/docs/).
