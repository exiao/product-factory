---
name: artifact-review
description: Build a concise interactive review site where creators compare, choose, annotate, request further work on, and dismiss AI-produced artifacts. Use for collecting human judgment on work, rather than agent-only quality critique.
---

# Artifact Review

Build the review site, not a prose questionnaire. Start from the actual artifact and unresolved judgment. Preserve the creator's work, choices and authorization. The host workflow owns research, generation, execution and its completion criteria; this skill owns presenting the work and carrying the creator's response back to it.

## Build the site

Read the artifact and existing project context first. Reuse an existing site and its design when available. For a new site, build a small runnable page in the project's review directory. Use the portable [action bar](assets/review-actions.js) and [styles](assets/review-actions.css) as a starting implementation of the required secondary actions. Serve the site, exercise it and return its actual URL. Do not stop at instructions or a mockup when a working site was requested.

Keep each card to the artifact, one short question and response controls. Keep the artifact inside the card; show alternatives together when comparison is the decision. Use real excerpts or before/after images instead of slogans, abstract diagrams or descriptions of what a prototype might do. A visual earns space only when it clarifies the choice. Put source material and rationale behind disclosure when they are not needed to judge. Retain visible limitations when they change the decision, particularly prepared samples presented near generation controls.

Remove repeated vision statements, eyebrows, progress narration, scope recaps and prose paraphrases of options. A normal feed contains only prepared decisions that need this person; a gallery of available mechanisms is a separate reference, never a mandatory questionnaire. Preserve back navigation and previous answers without displaying JSON receipts or a separate saved-answer dump.

## CTA contract

Every active review card exposes these three secondary actions, in a consistent compact action row. Do not hide them in an overflow menu or replace them with generic chat:

| Action | Label and behavior |
|---|---|
| Extend the work | **Research further** when missing evidence could change the judgment; **New option** when the presented alternatives are insufficient. Use both when both are useful. Capture an optional specific request; keep existing work and choices. Return a new sourced finding or a distinct option when execution is connected. |
| Comment | **Add comment** opens one small anchored popover beside the widget. One entry point per widget, not separate text/image buttons or a full sidebar. Associate the comment with the artifact ID and version. Preserve drafts, replies and resolution where the task needs them. |
| Remove from attention | **Dismiss** removes a pending card from the current feed; **Archive** retains completed work outside it. Neither approves, rejects or deletes the underlying artifact. Provide immediate Undo and a way to revisit archived cards. |

Do not manufacture a forced choice. Exploration defaults to selecting any useful directions, including all; use single selection only when the next action truly requires mutually exclusive alternatives. Explain a real constraint briefly when it forces a tradeoff. Offer a visible free-text path for the creator's own direction or correction, usable with several options or without choosing a supplied option. Comments supplement this path; a generic comment button alone does not replace an open answer. Carry the full selected set and free-text intent through the next step, artifact revisions, persistence and export; do not silently reduce it to the first selection or merge distinct directions.

The primary action answers the actual question: choose an option, keep an edit, rank priorities, rate against a named criterion, or confirm a concrete recommendation. Do not add a redundant confirmation for a reversible local selection. Keep a path to reject all options or ask for another. Name any consequential action explicitly; review approval is not permission to publish or send messages.

Use native buttons and labeled fields, keyboard access, visible focus and useful empty/error states. Popovers dismiss with Escape and return focus to their trigger. Do not call interactive comment forms tooltips in their accessibility semantics; use a labeled nonmodal dialog.

## Connect responses to the work

Use stable artifact IDs and versions. A response updates the associated artifact, scope, next task or review status; it must not silently attach to regenerated work. If the source changes materially, preserve the earlier response and request renewed judgment only where it is invalidated.

Wire callbacks to the actual authorized workflow when available. If only local storage is available, label extended-work actions **Request new option** or **Request research** and explicitly report **Request saved**, not research completed or an option generated. Persist requests and comments, export them with the project record, and disclose that the agent must read that record to act. Do not silently use localStorage as an agent communication channel. Handle failures without losing input or claiming success. Archive and dismiss remain local reversible status changes unless the host explicitly implements otherwise.

## Verify before presenting

Personally inspect every distinct rendered card and important outcome state at the intended viewport. Check whether the artifact, judgment and consequence can be understood without accompanying narration. Exercise primary choice, further-work request, comment, Escape/focus return, dismiss/archive, undo/revisit, reload and export or connected execution. Check error preservation and that dismissal leaves underlying work unchanged. Test against real examples; a valid form or successful save is not proof of useful judgment or creative quality.

Report only what actually works and the remaining execution boundary. Keep the final handoff short: review URL, what changed, and any essential limitation. A critique from this site feeds the host's next revision; it does not reset its larger task or authorize unrelated changes.
