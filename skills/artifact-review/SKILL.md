---
name: artifact-review
description: Build an interactive site for a creator to inspect artifacts, choose directions, request revisions, and send feedback to the originating task. Use for human review of actual work, not agent-only critique.
---

# Artifact Review

Present the actual work and the judgment it needs. This skill owns the review surface and feedback handoff; the host owns research, generation, implementation, and delivery. Reuse established scope and decisions. Reviewing an artifact does not authorize publishing it or messaging other people.

## Start from the template

Reuse an existing review when available. For a new review, run:

```bash
python3 <artifact-review-skill-directory>/scripts/create_review.py /absolute/review-directory
```

The generator refuses to overwrite a nonempty directory. Populate `artifacts.json` and copy actual media. Read [the template contract](references/review-desk.md) for data fields and serving. Use the bundled shell rather than reinventing its navigation, typography, storage, and submission controls. Preserve existing storage keys, artifact IDs, versions, drafts, and responses when updating a review.

## Visual identity

Read the bundled [visual identity](references/visual-identity.md). It is the default for the review shell; an explicit user direction overrides it. Keep the reviewed product itself in its own design system.

The template supplies Newsreader 500 headings, General Sans body/UI, parchment backgrounds, ivory fields, warm borders, and terracotta accents. Terracotta primary buttons use ivory (`#faf9f5`) text. Theme shared tokens instead of styling controls independently. Use one font family and size across action controls. Within artifact descriptions, use a single body-text style for paragraphs, citations, and bullets: General Sans 16px, weight 400, line-height 1.6. Do not enlarge the first paragraph or shrink and mute later paragraphs; use spacing and the serif heading for hierarchy. Load General Sans through Fontshare; do not publicly self-host it. Verify successful remote font-file responses as well as loaded faces.

## Default review surface

- Desktop: a compact artifact queue beside the selected work. Mobile: horizontal artifact tabs followed immediately by the selected or first unresolved artifact. Never land on a full-screen list of artifact names.
- Header: project title and one **Send to Codex** action, accessible while scrolling. No More menu or default export button.
- Card: one specific question → actual artifact with contextual citations → **Notes or changes** → **Request revision** and **Keep →** (or **Keep selection →**).
- Use a quiet card count in the footer. Preserve tab navigation, browser Back, direct links, reload, and selection across viewport changes. Advance after a recorded response; after the last prepared item show a compact ready-to-send state.
- Include only prepared artifacts requiring judgment. Labels identify their actual type; missing stages do not create placeholder cards.

Images and documents belong in the review. Do not add a separate “Expand image” link beneath an inline image. Interactive product prototypes open separately through **Open prototype**; a screenshot can preview them. Do not replace the working prototype with an iframe, review worksheet, or explanation of what it would do.

Preserve the supplied evidence exactly in meaning. Do not invent participant histories, quotes, preferences, motivations, or outcomes to make sparse notes read like completed interviews. Keep proposed behavior and inferred benefits distinct from observed research. A citation to a newly generated evidence page does not make invented detail supported.

Give compared alternatives equal typography and visual weight; do not style the first as a lead paragraph and diminish the rest. Show alternatives together when comparison is the decision. Default to multiple selection and preserve every selected direction. Use exclusive selection only when the next action actually requires it. Notes must support custom directions, including rejection of every supplied option.

## Remove friction and redundant text

For a text comparison, state each option’s interaction and main tradeoff once, usually in one or two sentences per option. Do not add a head-to-head recap that repeats those points. Let the controls communicate selection and the Notes field communicate custom input; do not explain them again in the artifact prose.

No page-level or card-level More menus. Put important source links beside the claim or description they support. Omit detached source collections and unrelated rationale.

Do not add selection tutorials, workflow narration, scope recaps, repeated option descriptions, generic “illustrative scenario” captions, or permanent local-saving instructions. Do not repeat “Selected” or another saved-state label inside a card when its controls and queue already communicate that state.

Do not duplicate caveats already shown in the artifact. Include a qualification only where its absence would materially mislead the reviewer; keep it with the relevant evidence. Technical verification status belongs in the host's handoff unless it changes the current decision.

Preserve previous versions and their feedback in the project record. Do not expose history controls by default. Present a baseline or version comparison only when judging the change requires it. A requested correction gets one revised result unless alternatives address a real unresolved choice.

## Feedback semantics

**Request revision** handles changes, additional research, and new alternatives through the existing Notes field. Do not add separate Request research, New option, or generic Add comment buttons beside it. **Keep** records acceptance and any optional note; **Request revision** records a change request without approval. Draft text and checked options alone are not approval.

Annotations are an optional extension when an image point, passage, or video timestamp provides useful precision. Pair anchors with artifact IDs and versions; retain whole-artifact notes. Use an available host annotation surface or the optional `comments-layer` skill where installed and appropriate. The optional `review-actions` helper is for custom hosts, not part of the default proposal flow. Only add dismiss/archive for optional work with a working undo/revisit path; never treat dismissal as approval.

Persist input before navigation and retain it on failures. Materially changed artifacts receive a new version; prior responses remain attached to what was reviewed. Preserve all chosen options and free-text intent in the host handoff.

## Send feedback to the originating task

In Codex, inspect `codex queue --help`. If supported, start the bundled server with `--thread <originating-task-UUID>`. Use its fixed-task bridge rather than stopping at localStorage. See [the bridge contract](references/review-desk.md).

Save an immutable feedback snapshot and send its reference to that existing task. Keep the destination and command fixed server-side. Report success only after acknowledgment. Deduplicate identical snapshots, preserve uncertain-delivery receipts, and never automatically retry an uncertain send. A queued message is not proof that revisions were completed.

When dispatch is genuinely unavailable, use **Save feedback** and explain the limitation after use. Show saving, success, or recovery text only when relevant. Saved requests must never appear as completed agent work.

Verify a newly wired bridge separately from mocked UI tests. A request to wire submission permits one clearly marked verification-only snapshot to the originating task; it must contain no invented approvals and request no product edits. Do not repeatedly send live tests for styling or documentation changes.

## Verify and deliver

Use [the regression scenarios](references/regression-scenarios.md). Run the real-template browser check when changing its behavior or styles; run bridge tests when changing dispatch. Inspect each distinct card at desktop and narrow widths, including important outcome states. Confirm:

- The artifact and question appear immediately on mobile; sticky controls do not obscure them.
- Fonts, button colors, spacing, and contextual links match the identity and template.
- No More menus, duplicate request actions, repeated saved-state labels, or unnecessary captions have returned.
- Multiple selections, custom notes, Back, reload, resize, completion, and failed-save recovery preserve intent.
- Optional controls are tested only when actually present; do not add them to satisfy a checklist.

Return the working review URL and a brief account of what changed. Distinguish local saving, acknowledged dispatch, and completed downstream work. Continue the host's existing task rather than restarting discovery or expanding its authorization.
