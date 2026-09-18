# Review regression scenarios

Run `node scripts/check-desk.cjs` for the actual default template plus `python3 scripts/check-server.py` for sibling isolation/request boundaries and `python3 scripts/check-handoff.py` for dispatch fixtures. Set `NODE_PATH` to an existing Playwright installation and `PLAYWRIGHT_CHANNEL=chrome` to use installed Chrome. These checks send no live task messages. `check-actions.cjs` covers only the optional custom-host annotation helper; it is not a requirement to add that helper to a review.

Use the cases affected by a change; these are reusable checks, not additional user approval gates. Use isolated records and explicit test markers. Never send test feedback to a live task without authorization.

| Scenario | Required observable result |
|---|---|
| Keep a proposal with an optional note | Keep remains enabled; artifact, version, approval and note survive Back and reload. |
| Request revision using the open field | One field supplies the request; the proposal remains unapproved and dependent work does not treat it as accepted. |
| Explore two directions plus a custom instruction | Both selections and the full instruction survive navigation, persistence, submission and the host’s next artifact. Also allow custom direction without a supplied selection. |
| Review a prerequisite proposal | No Dismiss or duplicate Add comment; revision remains available. |
| Annotate or dismiss an optional artifact | Show only the actions supplied by the host; Escape returns focus, failed saves retain input, and dismiss has host-provided undo/revisit. |
| Send a review batch | Save a stable snapshot and show dispatch success only after the connector acknowledges queuing the snapshot. Repeated sends do not duplicate it; uncertain delivery is preserved rather than automatically retried. Unsaved text must not disappear. |
| Continue after feedback | The receiving host reads that snapshot, respects artifact versions and explicit intent, updates the appropriate artifact and presents the next unresolved judgment. A delivery receipt alone does not pass this case. |
| Review a fresh project with older related material available | Begin with unapproved current-scope framing; older approvals do not settle this project. Dependent detail cards wait for unresolved prerequisites. |
| Artifact-type labels | Desktop and mobile rows identify the actual artifact type; “Problem statement” displays as “Problem.” Repeated types have distinct short subjects, and opening a row shows the matching artifact. Missing stages do not create placeholder rows. |
| Default desktop queue plus active artifact | Queue and active artifact appear together; selecting a queued item loads it as active. |
| Mobile artifact-first view | The first unresolved or selected artifact is visible immediately, below compact navigation; Send remains available. |
| Artifact switching preserves drafts | Notes survive navigation tabs, browser Back, reload and resize. |
| Reload and viewport changes preserve selection | Reload and viewport changes keep the selected item. |
| Response advances prepared queue | A response advances to the next prepared item; the last item shows a compact ready-to-send state. |
| Sticky header and focus | Sticky header never obscures the heading or actions, and focus lands on the expected control. |

Check a proposal at desktop and narrow widths: self-contained question, actual artifact, response field, supporting evidence and footer. The count must not crowd the title. Inspect contextual citations in the description; no More menus or separate research-request controls should appear. Retain a link or capture for the observed result and state which scenarios were actually exercised.
| Shared typography | Every visible action and form control uses the same computed font family and control size, including further-work actions. |
| Minimal surrounding copy | No persistent process-status paragraph, selection tutorial or inline history block before Notes. No repeated recorded-state labels or generic scenario captions. A decision-critical qualification is not duplicated when the artifact already communicates it. |
| Submission uncertainty | Same snapshot is not resent after timeout or ambiguous acknowledgment; edits create a new snapshot and do not reclassify draft notes as approvals. |

| Unified revision | Requests for research, alternatives and changes all use Notes + Request revision; no redundant request buttons. |
| Contextual evidence | Important source links appear beside the supported description, not in a More section or detached source list. |

| Identity | Newsreader headings and General Sans controls; ivory text on terracotta CTAs. Verify font network delivery when changing font loading. |
