---
name: marketing-loops
description: Design and set up recurring marketing checks and workflows with explicit triggers, saved state, deduplication, and stop conditions. Use for marketing automation, recurring reviews, ad-fatigue monitoring, content refresh, or retention watches; not one-off strategy work.
---

# Marketing loops

Define a repeatable job that produces a useful decision or authorized action. Separate how often a loop checks from what evidence makes it act. Reuse the user's desired outcome, cadence, budget, sources, and authorization; do not turn a one-off request into a scheduled job.

Read [loop design and examples](references/loop-design.md) to select a workflow. Before scheduling, specify purpose, inputs, cadence/timezone, trigger, body, validation, state, action scope, output, and stop conditions. Match cadence to data latency and the time needed for a meaningful sample. A requested periodic digest can run on cadence; an alert should notify only on meaningful changes, completion, failure, or required user action.

Read [state and recovery](references/state-and-recovery.md) for deduplication, uncertain writes, partial failures, and restart behavior. Keep state in the current project or an existing supported state store. Never write loop state into global assistant memory or assume a Hermes configuration path exists.

Use currently available tools and installed skills for the body. Tool availability, account access, and data freshness are preconditions to execution. Design a small bounded first run; inspect its actual output before calling the loop operational. Installing this skill does not schedule anything.

For an explicitly requested recurring task, inspect existing automations and update a matching one rather than creating a duplicate. Use Codex's available automation tool and follow its schema; prefer a task-attached heartbeat unless the user requests standalone runs. Put a cohesive, human-readable job description in the saved prompt, including evidence checks, state location, and notification intent. Do not substitute shell cron or invent tool names if the scheduling capability is unavailable; deliver the complete loop specification and state that scheduling is blocked.

Drafting, monitoring, and reporting do not authorize sending, publishing, changing ads, or spending. Preserve any explicit autonomous-action scope and limits already given; ask only for missing authorization needed by the concrete action. A planning request is not a reason to ask permission for hypothetical future actions. Never promote a draft-only loop into an executing one because previous runs succeeded.

Deliver the saved automation identity when created or updated, the actual state/output paths, what the first run established, and anything still unverified. If only the specification is complete, say so. Keep routine unchanged runs quiet unless periodic reports were explicitly requested.
