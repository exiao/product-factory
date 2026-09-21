# Other trace sources: documentation directory

Use this directory after the user selects a fallback source, or identifies one
in the request. These are official documentation entry points, checked on
2026-09-21, not integrations or promises of session-export support. Read the
chosen provider's current docs to learn its supported inspection method and
access requirements. Do not browse every provider or build adapters in advance.

| Source | Official documentation |
| --- | --- |
| Hermes Agent (Nous Research) | [Hermes Agent docs](https://hermes-agent.nousresearch.com/docs/) |
| OpenClaw | [OpenClaw docs](https://docs.openclaw.ai/) |
| OpenCode | [OpenCode docs](https://opencode.ai/docs/) |
| Grok | [Grok API docs](https://docs.x.ai/overview) |
| Muse / Muse Code (Meta) | [Meta Model API and Muse Code docs](https://dev.meta.ai/docs/overview) |
| Cursor | [Cursor docs](https://cursor.com/docs) |
| Traces.com | [Traces docs](https://traces.com/docs) |
| Arize / Phoenix | [Arize AX docs](https://arize.com/docs/ax), [Phoenix docs](https://arize.com/docs/phoenix) |
| Langfuse | [Langfuse docs](https://langfuse.com/docs) |
| LangSmith | [LangSmith observability docs](https://docs.langchain.com/langsmith/observability) |
| Braintrust | [Braintrust docs](https://www.braintrust.dev/docs) |
| Another source | Ask for the product name or official documentation URL, then read its docs. |

A model name does not identify the application that stored its conversation.
For Grok or Muse, distinguish the coding agent, consumer chat app, API, and any
third-party host. If the user means another product named Hermes or Muse, ask
for its URL instead of applying these links. API documentation does not establish
access to consumer chat history. For Arize, clarify AX versus Phoenix when needed.

Find the documented read/list/search/export route for the chosen product and
version, using existing access and the requested project/time scope. Verify
pagination, retention, truncation, and whether an export includes full messages
and tool events. If only metadata is available, label that limitation rather
than reconstructing missing conversation text. Never invent a vendor's storage
path, database schema, command, or endpoint from another vendor's conventions.
