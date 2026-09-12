# Review playbooks

## Dashboard and internal tools

Read the code first, map the relevant routes and data flows, and inspect empty and populated states separately. Then assess widget relevance, hierarchy, density, filter placement, actionability, and cross-page links. Group by user job rather than database table. If a page represents a pipeline, make stages visible and link upstream inputs to downstream output.

## Jobs-to-be-done redesign

List what users come to do, then identify the frequent glance path and deeper work path from evidence; do not assume an 80/20 usage split. Generate structurally different approaches when the current page serves too many jobs. Score each on glance support, work support, jobs intentionally dropped, and cognitive load. Wireframe the winner with realistic content, empty/populated/interactive states, and click-through behavior before implementation.

## Information architecture

Map every old route to a user job. Use roughly three to five primary jobs, scoped sub-tabs, and view toggles for the same data at different zoom levels. A data source is usually a sub-view, not a top-level feature. Keep existing URLs when possible and produce an explicit old-to-new mapping so no destination disappears.

## Charts and metrics

Use a donut only when two or three categories literally form the headline. Prefer sorted horizontal bars for four or more categories or long labels; grouped bars compare series, stacked bars emphasize totals, lines show continuous trends, and bars show discrete periods. Do not use color for decoration. An insight card must reference current data and draw a non-obvious conclusion; hardcoded methodology belongs in help text.

## Fast layout options

When the user explicitly asks for layout choices, skip a discovery interview and use the requested medium, or show a few labeled ASCII wireframes for quick textual exploration with realistic content, interaction notes, and honest pros/cons. Make the structures materially different rather than changing only color or card count.

## Component specifications

For an AI-readable component spec, document four views: final rendered example, geometry and alignment anchors, semantic zones, and a decoration-free structural wireframe. Include tokens, responsive rules, content limits, interaction states, and accessibility. Treat example values as local conventions, not universal laws.
