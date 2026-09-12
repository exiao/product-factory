---
name: domain-modeling
description: Define and refine a project's business concepts, shared terminology, relationships, lifecycle rules, and context boundaries; record meaningful architectural decisions. Use for domain models, glossaries, overloaded terms, ubiquitous language, context maps, and ADRs. Not a mandatory stage for routine implementation or ordinary dictionary definitions.
---

# Domain modeling

Make the project's language and business rules precise enough that people and code mean the same thing. This skill changes or documents the domain model; reading an existing glossary does not require a separate modeling exercise. Use program-design for code structure and implementation slices when needed.

## Start with the existing model

Read the relevant project glossary, domain documentation, decision records, and code before inventing terms or files. Reuse the repository's names and documentation locations. A file named CONTEXT.md may serve another purpose; do not replace or narrow it to fit this skill. Create a glossary, context map, or decision record only when there is useful resolved content and the task calls for recording it. A discussion or read-only review need not write files.

Identify the business concept behind a term, its boundaries, relationships, ownership, and meaningful states. Distinguish domain concepts from incidental implementation details. Include a general concept such as money or time when the project's particular meaning, precision, or rules matter; it need not be unique to this business.

## Sharpen through examples

Surface overloaded or conflicting terms with a concrete example. For instance, an account holder, a bill payer, and a user may be different people. Propose a definition and test cases that distinguish the concepts rather than merely choosing a more polished label.

Test relevant relationships and invariants: can one order have several shipments; can cancellation be partial; which context owns a customer's billing address; what happens after a state transition? Include counterexamples and exceptions that materially affect the model. Invented scenarios are probes, not reported business facts.

Compare intended behavior with code, tests, and actual observations where available. Record a discrepancy as a discrepancy: code establishes current implementation, not necessarily the correct business rule. Do not silently rewrite the glossary to bless a bug or claim the implementation changed because the documentation did.

Resolve factual questions from available evidence. Ask the user only when a material business meaning or choice remains unsettled, providing a recommendation and its consequence. Keep alternatives or unresolved terms marked as proposed. Do not reopen settled definitions without new evidence.

## Record the useful result

Keep definitions concise but include examples, exclusions, relationships, or lifecycle rules when a short noun definition would hide an important distinction. Prefer one canonical term within a context; retain external aliases when customers, integrations, or another context legitimately use them. The same word can mean different things in different contexts. Define translation and ownership at the boundary instead of forcing one global vocabulary.

Update agreed or evidence-backed definitions in the appropriate existing document while preserving unrelated material. Separate proposed changes from accepted definitions and distinguish domain rules from technical decisions. See [record formats](references/record-formats.md) for optional lightweight shapes; existing project templates take precedence.

Record an ADR when a decision's tradeoff, constraint, rejected alternative, or consequence will matter to future maintainers. Hard-to-reverse or surprising choices deserve particular attention, but these are judgment cues, not an all-or-nothing test that overrides a requested ADR. Do not turn every library choice into a record. Preserve decision history; supersede an old decision rather than silently rewriting its rationale.

Conclude with the resolved model, significant code/documentation mismatches, and remaining questions. For documentation updates, link the changed files. Domain modeling does not by itself authorize code refactors, external actions, or broader implementation.
