# Inert feature probe

When tests are green but the feature may have no production effect, trace the wiring in both directions:

1. Identify the real input produced by the application or user.
2. Follow it through the changed code to the caller and final surface.
3. Confirm the changed branch is reachable with current flags, schemas, permissions, and data.
4. Trigger it through the public surface and capture the changed output or state.

An uncalled helper, default-off flag, rejected enqueue input, or fixture-only path is not proof of a working feature. Report the exact missing producer, caller, or runtime condition.
