# Lightweight domain records

Use the project's existing documentation conventions first. These shapes are optional, not a required file hierarchy.

## Glossary or domain note

```markdown
## Account holder
The person or organization responsible for the subscription agreement.

Distinct from: a user who can access the workspace but does not own the agreement.
Relationship: one account holder may own several workspaces.
Rule: changing the payer does not automatically change the account holder.
Status: proposed; confirm the transfer rule with the product owner.
```

Include only relevant fields. Keep business meaning separate from storage columns or service classes, linking implementation evidence when it explains a mismatch. Preserve agreed synonyms or public API names even if an internal canonical term differs.

## Context map

Create or extend a map only when several contexts actually need their differing language and boundaries explained. For each, identify its responsibility, authoritative concepts, and relationships with the others. Record ownership and translation where data crosses a boundary. Distinguish the observed integration from a proposed one; do not invent events, shared types, or services to fill a template.

## Decision record

A short record can contain the decision, its context, why this option was chosen, and any consequence or rejected alternative worth remembering. Use an existing ADR template, numbering scheme, and status vocabulary when present. Otherwise a descriptive filename and a short Markdown note are enough; check for filename collisions.

Label unaccepted proposals. When a decision changes, link the replacement and preserve the original rationale. An explicitly requested decision record need not pass a separate threshold of irreversibility.
