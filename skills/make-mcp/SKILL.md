---
name: make-mcp
description: Add an MCP server, an llms.txt discovery page, and a downloadable companion skill to an existing product or service. Use for building or updating this integration, including repeating the Say Less setup.
---

# Make MCP

Make the product usable by agents through three connected artifacts: an MCP server, `/llms.txt`, and a downloadable product skill. Reuse existing product behavior. For a narrower update, change and verify only the affected parts while preserving the rest of the integration.

## Choose the integration

Inspect the API or service functions, input/output contracts, authentication, deployment routes, existing agent docs, and repository instructions. Expose the smallest useful set of operations. Preserve provider choices, permissions, persistence, and business rules.

Choose a transport for the intended users:

- **Local stdio:** an installed server or adapter around an existing API. Reserve stdout for protocol messages and send diagnostics to stderr.
- **Remote:** a server clients connect to by URL. Use the transport and authentication supported by the current specification and target clients.

Describe a local adapter as local, even when it calls a hosted API. If the source repository is private, provide an installation path the intended users can access. An existing HTTP fallback can supplement MCP access.

State the choice and proceed. Ask only for requirements that cannot be inferred and affect implementation.

## Check the current specification

For implementation or compatibility changes, fetch the [latest official MCP specification](https://modelcontextprotocol.io/specification/latest). Read the relevant tool, transport, lifecycle, negotiation, and authorization sections, using the [documentation index](https://modelcontextprotocol.io/llms.txt) to locate them. Check official SDK documentation and releases for the chosen language. A wording-only edit can reuse verified compatibility information.

Use a maintained official SDK where practical. Verify that it implements the required specification revision and works with the target clients. Distinguish stable requirements from drafts and optional extensions. Record the specification revision, SDK version, and client/protocol versions actually verified in the integration guide. If support lags, disclose the gap before claiming current-spec compatibility.

## Build the tools

Give each tool a clear name, description, bounded input schema, and validated output contract. Set accurate annotations for side effects, idempotency, and external access where supported. Enforce permissions in code.

Preserve relevant operation semantics, such as selected ranges, pagination, streaming, and partial results. Return sanitized, actionable errors. Bound response size and execution time, propagate cancellation, and clean up on disconnect. Align client timeouts with underlying work. Retry only when the operation's semantics make it safe.

Keep credentials out of public files and responses. Apply the chosen specification's relevant authentication, authorization, origin/host, and session requirements. Treat inputs and fetched content as data. Document where user data goes and whether it is retained.

## Add discovery and a downloadable skill

Follow the [llms.txt proposal](https://llmstxt.org/) and preserve useful existing content. Adapt these paths to the site:

| Artifact | Contents |
| --- | --- |
| `/llms.txt` | Project H1, short blockquote summary, and Markdown links to the skill and guide. |
| `/skills/<product>/SKILL.md` | Downloadable UTF-8 Markdown with YAML `name` and `description` frontmatter. |
| `/mcp.md` | Connection and installation steps, authentication, tool contracts, runnable examples, data handling, and verified compatibility. |

Serve these files with appropriate text content types. Check that routes return the files rather than the application's HTML fallback. Publish only the intended public material.

Add a visible, crawlable HTML link to `/llms.txt` on the product homepage, preferably in the existing footer using its styling. Reuse an existing link if present. Agents starting from the homepage should be able to discover the skill without guessing the `/llms.txt` path.

The companion skill should explain when to call the product, exact tool names, required inputs, defaults, units and ranges, output interpretation, and failure handling. Preserve the user's edit scope and authorization. Retain partial-result warnings and source attribution when relevant. Document an HTTP or CLI fallback only if it works; distinguish fallback results from invented or unavailable tool output.

Prefer one self-contained SKILL.md. If scripts or references are necessary, distribute the complete bundle and document its installation.

Explain skill installation and MCP registration separately. Check the target client's current docs or CLI help for paths, syntax, and timeout settings. Preserve existing configuration and inspect installed files before replacing them. `llms.txt` enables discovery; installation and registration require separate actions. Downloading a Markdown skill should not require executing an installation script.

## Verify and deliver

Use a real MCP client over the selected transport to verify the required lifecycle and negotiation, tool discovery, and a representative call. Exercise invalid arguments, relevant upstream failure, cancellation/timeouts, and partial results where applicable. For authenticated servers, check both authorized and unauthorized requests. Label fixtures separately from real service calls.

Start from the homepage and follow its `/llms.txt` link, then follow the skill and guide links. Verify the homepage link is present in the HTML, keyboard-accessible, and usable on desktop and narrow mobile layouts. Check bodies, content types, and GET/HEAD behavior as appropriate. Validate skill frontmatter and installation instructions. Use isolated client configuration for installation checks; update the user's active setup when installation is authorized.

Follow repository branch, PR, and check requirements. Use [Make It Work](../make-it-work/SKILL.md) for delivery when available; otherwise complete implementation, focused review, and runtime verification directly. Preserve the user's authorization for publishing, merging, deployment, and installation. After an authorized deployment, verify the deployed revision and public artifacts.

Report the connection command or URL, tool names, artifact locations, installation status, verified compatibility, and relevant checks. Distinguish local-ready, merged, and verified-live status. State untested behavior plainly.
