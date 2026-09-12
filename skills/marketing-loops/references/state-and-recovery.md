# State and recovery

Use the existing project convention or a small project-local state file such as marketing/loops/creative-review.json. Store the schema version, last successful check, source cursor/window, handled item/action keys, cooldowns, pending actions, and output references needed for this loop. IDs and hashes may still identify people; minimize and protect them as appropriate. Never log credentials or unnecessary message/customer content.

A watermark alone cannot prevent duplicate external actions. A crash can happen after the action succeeds but before the local file is updated. For each action use the provider's documented idempotency key if supported, record intent and result, and reconcile pending outcomes on restart. Without reliable idempotency, inspect remote state before retrying. An ambiguous result stays pending; do not blindly repeat it or call it a failure.

Keep checks and actions distinct. Advance source cursors only across a completely processed range or retain failed-item IDs for recovery. Account for late-arriving events using an overlap window plus deduplication. Mark an item handled after its required durable output or verified external result exists, not merely after starting work.

Prevent overlapping runs with the scheduler's supported control or an appropriate lock. Write state atomically and avoid two runs overwriting each other's progress. If a lock looks stale, verify whether a prior run is still active before removing it. Corrupt or missing state is a recovery condition, not permission to replay historical actions.

On the first run, establish the bounded baseline the user requested. Do not silently backfill all historical contacts or reset suppression lists. Preserve opt-outs and relevant cooldowns across resets; never expire them merely to reduce file size. Backfill should be explicit and first preview what would change.

Record run time, source freshness, checked/completed/error counts, actions actually verified, and evidence paths. A zero-action run may be healthy. Reconsider a loop when its outputs are consistently unused, its signal is too sparse, or maintenance exceeds its value. Data/auth/budget failures should preserve completed evidence and stop dependent actions; notify only when meaningful or action is needed.
