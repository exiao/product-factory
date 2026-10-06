---
name: confirm-understanding
description: Check a coding agent's interpretation of a task against evidence and user intent, resolving consequential assumptions before dependent work. Use for task clarification; a full unknowns interview is optional.
---

# Confirm understanding

Establish what the user actually wants before spending effort on a mistaken interpretation. Reuse the request, relevant context, and already accepted decisions. A clear task needs a brief restatement, not another approval ceremony.

## Make the interpretation inspectable

Summarize the intended outcome, problem, and proposed approach in two or three sentences. Name the person or audience when relevant, the starting material, expected result, scope and exclusions, and how the result will be judged. Do not turn a proposed implementation detail into a requirement.

Identify consequential assumptions and what supports them. Separate a supported requirement from an inference. Check the proposed approach against the source material; agreeing with the user's suggested solution does not prove it addresses their problem. Give a concrete reason when evidence challenges a premise.

## Resolve what matters

Ask the smallest set of questions whose answers could change the outcome, scope, success criteria, or authorization. Batch related questions through the runtime's asynchronous question tool when available; otherwise ask together in the conversation. Offer plausible choices and room for the user's own answer. Continue independent authorized work while a required answer is pending.

Use a small example, diagram, wireflow, or existing artifact when it makes a disagreement easier to judge. Do not build an unsolicited prototype or full option set just to clarify a simple task. If broad blind spots are the explicit question, use [explore-unknowns](../explore-unknowns/SKILL.md); defining measurable success can use [acceptance-criteria](../acceptance-criteria/SKILL.md).

Update the interpretation when the user corrects it, including affected downstream decisions. Silence is not agreement. Reuse explicit prior answers and delegated choices; ask again only when new evidence materially invalidates them. Reversible implementation choices within accepted scope do not require repeated confirmation.

## Hand off the agreement

Keep the resolved outcome, boundaries, criteria, and open questions in the existing brief or task record. Return a proposed record for read-only work. Link relevant evidence rather than rewriting a context inventory. If required uncertainty remains, identify dependent work that cannot proceed and finish independent work.

The result is an agreed or evidence-supported task interpretation, with unresolved assumptions visible. It is not verification that the planned product will work or that the user authorized publishing, spending, deployment, or messages.
