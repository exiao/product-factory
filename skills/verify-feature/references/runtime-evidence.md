# Runtime evidence

For each verification, record:

- diff/commit and the changed surface;
- build or start command and the route/CLI request used;
- exact capture command, viewport/device, auth state, seed data, and wait time;
- observed result and at least one edge or failure probe;
- surfaces and account states not tested.

For visual changes, use the same method for baseline and candidate and combine them into one comparison artifact. For interactions, the artifact must perform the target action and capture its result. A screenshot of a visible control does not prove its handler works. If a baseline cannot build, state the failure and downgrade the claim accordingly. Keep evidence local unless publishing was explicitly requested.
