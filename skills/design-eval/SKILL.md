---
name: design-eval
description: Evaluate and fix rendered interfaces using Nielsen Norman usability heuristics. Check unnecessary text, competing actions, and product versus review commentary. Use as the completion pass for design-mode and design-iteration, or for focused design cleanup.
---

# Evaluate, fix, recheck

Inspect the interface, fix confirmed problems in the source, and verify the saved result before handoff. Unnecessary reading and competing actions count as defects even when every button works. An explicit assessment-only request ends with findings and leaves the artifact unchanged.

Work from settled decisions about the audience, task, visual direction, design system, and medium. Preserve required content, established behavior, business rules, and accessibility. Work within the affected flow and its related states; changes to product direction or publishing need their own authorization. Callers reference this skill's shared rules and reuse one completed pass for the final revision.

## Inspect the experience

Open the rendered artifact and relevant source. Identify the person's current task, the product's useful contribution, and the next decision. Inspect relevant populated, empty, selection, preview, loading, error, and recovery states. Reuse evidence that still matches the source; refresh stale captures.

Read the [usability checklist](references/usability.md) and check all ten Nielsen Norman heuristics. Apply its psychological guidance where relevant. Keep the checklist's coverage record in working evidence, including untested states and reasons. The checks belong to this pass; a separate audit, study, or user-facing scorecard is unnecessary unless requested.

Resolve friction through behavior, grouping, and clear controls before adding explanation. Preserve status feedback, recognizable context, error prevention and recovery, and task-specific help. A usability finding does not automatically require more text or a confirmation dialog.

## Remove unnecessary work and text

For each heading, instruction, caveat, status, container, and action, ask: **What becomes harder to understand, do, recover from, or judge correctly if this disappears?** Name the consequence in this state and check whether the interface already communicates it. Generic reassurance or completeness is not enough. Remove elements with no distinct contribution before adding features or compressing the layout.

Apply this test across the affected flow. Preserving behavior does not require preserving incidental copy. By default, remove redundant labels, instructions that repeat controls, design-process commentary, and caveats explaining that a person's own notes are subjective. Retain exceptions for explicit requirements or a specific misunderstanding the interface would otherwise allow.

- **Challenge decorative text.** Inspect eyebrows (small labels above headings), subtitles, section introductions, and helper sentences for a distinct contribution. Remove copy that repeats nearby content, fills whitespace, or exists only to create another typographic tier. Retain eyebrows that establish useful context, such as a publication section or object category, when that context is not already clear. Restore hierarchy through placement, spacing, and typography after removal; preserve explicit briefs, established systems, accessible names, and necessary instructions.
- **Check for an unnecessary promotional wrapper.** In apps, tools, visualizations, and motion studies, remove unrequested heroes, slogans, and promotional sections that delay the task or content. Marketing and editorial surfaces may need these elements to communicate their intended message; evaluate them against that purpose rather than imposing a universal ban.
- **Keep useful assistance.** Preserve readable labels, empty-state guidance, actionable errors, consent, and meaningful consequences. An empty editor that no longer helps with the task is not an improvement.
- **Show tools when needed.** Keep the current task prominent and occasional tools discoverable. Merge duplicate actions only when the remaining path supports the same task and input methods. Record whether a feature was removed or moved into disclosure.
- **Separate product use from design review.** Put rationale, implementation details, research qualifications, and change logs in the handoff or a requested review surface. Keep prototype controls outside the apparent product UI and out of presentation/export views.
- **Explain simulation clearly.** Use one concise prototype disclosure. Add local wording when needed to prevent a specific misunderstanding, such as mistaking fixed advice for analysis of an upload or simulated checkout for a charge. State the relevant consequence without repeating caveats or hiding limitations.

Check the remaining hierarchy, grouping, typography, imagery, contrast, wrapping, and control placement against the accepted direction. Preserve useful grouping and avoid decorative nesting. Remove filler metrics, claims, or screens added merely to suggest completeness. Judge whether the person can complete the task, rather than targeting a word count, control count, or emptier screenshot.

For substantial visual revisions, obtain one fresh-context rendered critique when delegation is available and authorized. Give the reviewer the task, audience, aesthetic, references, and artifact without prior verdicts or implementation rationale. Follow session model preferences and disclose self-performed review. The primary agent must still inspect the rendered result.

## Fix and confirm

Record each defect's element or state, user impact, and smallest useful fix. An observed in-scope defect is sufficient reason to act; another user complaint is unnecessary. Preserve a comparable baseline and edit the source in its native medium.

Inspect the saved revision at representative desktop/mobile or native sizes, including a short mobile viewport when relevant. Exercise changed interactions, check assets and runtime errors, and reload where persistence is expected. Reproduce reported interaction failures before calling them bugs. Use [render verification](references/render-verification.md) for web and SVG checks. Screenshots establish appearance; interaction claims need observed behavior. For static artifacts, inspect the rendered output and mark unavailable interactions untested.

When controls move or disappear, check findability, keyboard dismissal, and focus returning to a visible, relevant control. For temporary proposals, verify that dismissal preserves the original and that acceptance and undo work.

Use one batch of evaluation and fixes, followed by one confirmation within the caller's review budget. Recheck failed heuristics against the saved revision and update the evidence. Inventory the remaining eyebrows, subtitles, section introductions, helper sentences, and caveats in the affected states; apply the necessity test to each and fix repeated instances of the same problem. Confirm in the saved render that removed copy has not been replaced by equally redundant wording and that the task remains understandable. Keep that inventory in working evidence.

Stop when identified issues are resolved. A remaining material defect warrants a targeted fix and recheck, even after confirmation. If access or scope prevents completion, report the specific gap and impact.

## Handoff and specialist help

Use [interaction-design](../interaction-design/SKILL.md) for unresolved behavior, copywriting (optional, when installed) for substantive copy revision, and [ui-lint](../ui-lint/SKILL.md) for code rules or formal UX assessment. For a formal design review, read its [question and assumption framework](../ui-lint/references/review-framework.md): full reviews cover every question with status and source; focused reviews name their coverage. Ask only for missing information that would change the decision.

Return the revised artifact with the changes, checks, and remaining limits, reusing the caller's change log. Distinguish observed behavior from simulated reactions and judgment. Reduced clutter alone does not prove improved human usability.
