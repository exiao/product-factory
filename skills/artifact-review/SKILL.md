---
name: artifact-review
description: Build a concise interactive review site where creators compare, choose, annotate, request further work on, and dismiss AI-produced artifacts. Use for collecting human judgment on work, rather than agent-only quality critique.
---

# Artifact Review

Build the review site, not a prose questionnaire. Start from the actual artifact and unresolved judgment. Preserve the creator's work, choices and authorization. The host workflow owns research, generation, execution and its completion criteria; this skill owns presenting the work and carrying the creator's response back to it.

## Build the site

Read the artifact and existing project context first. Reuse an existing site and its design when available. For a new site, build a small runnable page in the project's review directory. Use the portable [action bar](assets/review-actions.js) and [styles](assets/review-actions.css) for applicable secondary actions. Supply the host’s chosen actions explicitly; the helper adds none by default. Keep approval and revision controls with the host’s existing feedback field. Serve the site, exercise it and return its actual URL. Do not stop at instructions or a mockup when a working site was requested.

Keep each card to the artifact, one short question and response controls. The question must name the object and decision clearly enough for a first-time reader; “What should we explore?” alone is insufficient. Keep documents, images and other reviewable content inside the card; launch interactive product prototypes separately as described below. Show alternatives together when comparison is the decision. Use real excerpts or before/after images instead of slogans, abstract diagrams or descriptions of what a prototype might do. A visual earns space only when it clarifies the choice. Put source material and rationale behind disclosure when they are not needed to judge. Retain visible limitations when they change the decision, particularly prepared samples presented near generation controls.

Remove repeated vision statements, eyebrows, progress narration, scope recaps and prose paraphrases of options. A normal feed contains only prepared decisions that need this person; a gallery of available mechanisms is a separate reference, never a mandatory questionnaire. Preserve back navigation and previous answers without displaying JSON receipts or a separate saved-answer dump.

For a proposal card, default to question → artifact → Notes or changes → optional Evidence → footer. Place Back and the card count on the footer’s left, and revision and primary actions on the right; keep the title’s width available. Put evidence qualifications with their evidence, while keeping decision-critical limitations beside the artifact. Adapt this arrangement when the medium or an established site requires it.

For product prototypes, launch a separate standalone product experience in its own tab or window. The review card provides an **Open prototype** link and collects judgment afterward. A screenshot may preview the product, but it does not replace the launchable experience. Do not substitute a worksheet, configuration questionnaire, embedded review widget, or iframe for the actual product experience. Keep review navigation, progress and approval controls outside the prototype's working surface. Preserve the user's work when returning to review and include relevant prototype state in the submitted feedback.

## CTA contract

Choose actions for the actual judgment; do not stamp the same action bar onto every card. Use one primary next action and only secondary actions that add a distinct capability. Keep them quiet in one footer. Omit unavailable navigation and put export at page level.

- For an editable proposal with an open feedback field, use **Keep and continue** and **Request revision**. The field already supplies comments; omit a duplicate Add comment control. Revision requests do not approve the proposal. Text in an optional notes field must not disable approval: Keep saves the approval with its note; Request revision asks for a change. Let the explicit action determine intent.
- Use **New option** for genuinely distinct alternatives, **Research further** for missing evidence, and **Request revision** for changing the current artifact. Reuse visible feedback instead of opening a second input form.
- Use **Add comment** when annotation adds a distinct capability, such as a note anchored to an image or passage. Keep it in a small nonmodal popover, not a sidebar.
- Use **Dismiss/Archive** only when removing an optional item from attention is meaningful; provide undo/revisit. Do not hide a prerequisite decision behind Dismiss or let dismissal count as approval.
- Remove incidental scope notes, instructional subtitles and About-this-example prose. A consequential boundary belongs in the artifact being reviewed or its own decision, never in small print that approval silently accepts.

A successful approval must show the next available review artifact, preserve Back and reload behavior, and identify the next stage. If agent work is required first, explain exactly what is saved and how the user resumes it. Do not imply generation is running or the workflow has advanced when only a response was saved.

Do not manufacture a forced choice. Exploration defaults to selecting any useful directions, including all; use single selection only when the next action truly requires mutually exclusive alternatives. Explain a real constraint briefly when it forces a tradeoff. Offer a visible free-text path for the creator's own direction or correction, usable with several options or without choosing a supplied option. Comments supplement this path; a generic comment button alone does not replace an open answer. Carry the full selected set and free-text intent through the next step, artifact revisions, persistence and export; do not silently reduce it to the first selection or merge distinct directions.

The primary action answers the actual question: choose an option, keep an edit, rank priorities, rate against a named criterion, or confirm a concrete recommendation. Do not add a redundant confirmation for a reversible local selection. Keep a path to reject all options or ask for another. Name any consequential action explicitly; review approval is not permission to publish or send messages.

Use native buttons and labeled fields, keyboard access, visible focus and useful empty/error states. Popovers dismiss with Escape and return focus to their trigger. Do not call interactive comment forms tooltips in their accessibility semantics; use a labeled nonmodal dialog.

Show a minimal position indicator (for example, 1 / 2) when several review cards are available. Count actual prepared cards in the current review batch, not imagined future stages or total project completion. Update it on forward/back navigation and restore it on reload.

## Connect responses to the work

For visual iteration, keep feedback anchored to the visible work: an image point or region, a page element, or a video timestamp or range. Pair each anchor with the artifact ID and reviewed version, and retain free-text feedback for whole-artifact changes. Use the optional `comments-layer` skill for supported static-page and image annotations when available and useful; otherwise use the host’s supported annotation controls. Its bundled controls do not provide video time anchors; capture those in the host review record alongside a playable clip, or accept a timestamped note without claiming a timeline tool exists. Preserve audio when sound or timing is being judged.

After the host applies a revision, present the actual updated artifact and retain access to the reviewed baseline and its feedback. Use side-by-side views or a version toggle when comparison helps, with comparable framing and scale. Show playback for changes involving motion or sound. Keep prior annotations attached to their original version; explicitly remap them only after verifying their target in the revision. Do not replace a visual revision with a prose description or mark a saved request as implemented. A specific correction needs one revised result; create alternatives only when the creator has a meaningful unresolved choice.

Use stable artifact IDs and versions. A response updates the associated artifact, scope, next task or review status; it must not silently attach to regenerated work. If the source changes materially, preserve the earlier response and request renewed judgment only where it is invalidated.

Wire callbacks to the actual authorized workflow when available. If only local storage is available, label extended-work actions **Request new option** or **Request research** and explicitly report **Request saved**, not research completed or an option generated. Persist requests and comments, export them with the project record, and disclose that the agent must read that record to act. Do not silently use localStorage as an agent communication channel. Handle failures without losing input or claiming success. Archive and dismiss remain local reversible status changes unless the host explicitly implements otherwise.

For an authorized handoff back to the host agent, provide one page-level **Finish review** action. Save a stable feedback snapshot, send its reference to the existing originating thread through an available verified connector or CLI, and show success only after dispatch is acknowledged. Keep destination and command fixed on the server; do not accept arbitrary thread IDs or shell commands from the browser. Prevent duplicate sends of the same snapshot, preserve uncertain-delivery receipts, and do not automatically retry an uncertain send. Verify the receiving-thread dispatch separately from mocked UI tests. A queued message is not completed downstream work.

## Verify before presenting

Personally inspect every distinct rendered card and important outcome state at the intended viewport. Check whether the artifact, judgment and consequence can be understood without accompanying narration. Exercise the controls actually present: primary choice, further-work request, comment, Escape/focus return, dismiss/archive, undo/revisit, reload and export or connected execution. Check error preservation and that dismissal leaves underlying work unchanged. Test against real examples; a valid form or successful save is not proof of useful judgment or creative quality.

Use the applicable [regression scenarios](references/regression-scenarios.md) when changing review controls or handoffs. For an end-to-end workflow claim, verify both receiving-task dispatch and the resulting artifact update; otherwise report only the demonstrated boundary.

Report only what actually works and the remaining execution boundary. Keep the final handoff short: review URL, what changed, and any essential limitation. A critique from this site feeds the host's next revision; it does not reset its larger task or authorize unrelated changes.
