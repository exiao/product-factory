# Review regression scenarios

For the bundled helper, the optional browser check requires Node.js, the `playwright` package and its Chromium browser. Reuse an existing runtime by setting `NODE_PATH` to its packages directory. Otherwise install Playwright in a temporary test directory with `npm install playwright` and `npx playwright install chromium`, then point `NODE_PATH` at that directory’s `node_modules`. Run `node scripts/check-actions.cjs` from this skill directory. This check runs locally and sends no task messages.

Use the cases affected by a change; these are reusable checks, not additional user approval gates. Use isolated records and explicit test markers. Never send test feedback to a live task without authorization.

| Scenario | Required observable result |
|---|---|
| Keep a proposal with an optional note | Keep remains enabled; artifact, version, approval and note survive Back and reload. |
| Request revision using the open field | One field supplies the request; the proposal remains unapproved and dependent work does not treat it as accepted. |
| Explore two directions plus a custom instruction | Both selections and the full instruction survive navigation, persistence, export and the host’s next artifact. Also allow custom direction without a supplied selection. |
| Review a prerequisite proposal | No Dismiss or duplicate Add comment; revision remains available. |
| Annotate or dismiss an optional artifact | Show only the actions supplied by the host; Escape returns focus, failed saves retain input, and dismiss has host-provided undo/revisit. |
| Finish a review batch | Save a stable snapshot and show dispatch success only after the connector acknowledges queuing the snapshot. Repeated sends do not duplicate it; uncertain delivery is preserved rather than automatically retried. Unsaved text must not disappear. |
| Continue after feedback | The receiving host reads that snapshot, respects artifact versions and explicit intent, updates the appropriate artifact and presents the next unresolved judgment. A delivery receipt alone does not pass this case. |
| Review a fresh project with older related material available | Begin with unapproved current-scope framing; older approvals do not settle this project. Dependent detail cards wait for unresolved prerequisites. |

Check a proposal at desktop and narrow widths: self-contained question, actual artifact, response field, supporting evidence and footer. The count must not crowd the title. Inspect expanded evidence as well as the initial view. Retain a link or capture for the observed result and state which scenarios were actually exercised.
