# Runtime evidence

For each verification, record:

- diff/commit and the changed surface;
- build or start command and the route/CLI request used;
- exact capture command, viewport/device, auth state, seed data, and wait time;
- the attached video when recording was available, otherwise the screenshot and why video was unavailable; include the local path when saved;
- observed result and at least one edge or failure probe;
- surfaces and account states not tested.

For visual changes, use the same method for baseline and candidate and combine them into one comparison artifact. For interactions, the artifact must perform the target action and capture its result. A screenshot of a visible control does not prove its handler works. If a baseline cannot build, state the failure and downgrade the claim accordingly. Keep evidence local unless publishing was explicitly requested.

For a substantial UI branch, the scenario list should follow the changed journeys rather than a flat page list. Include the entry point, relevant error or permission branches, side effects, and the destination or persisted state that completes each journey. A diagram is optional when a concise outline makes the path clear.

For a long QA pass, keep a durable scenario record with the tested revision and environment, each scenario's pending/passed/fixed/blocked status, evidence path, and next action or decision for blocked work. Mark a scenario fixed only after an authorized change is verified on the real surface. Create the record when the scenario list is chosen, then update it after each result so another session can resume. On resume, rerun scenarios whose evidence no longer applies to the current revision or starting state; do not silently promote an old pass to a current verdict. Use the project's existing report format when available.

If a lazy-loaded or scroll-animated page produces an incomplete full-page screenshot, use the settled-slice recovery in [render verification](../../design-review/references/render-verification.md) for both baseline and candidate. Inspect the stitched result before using it as evidence and record the capture method.
