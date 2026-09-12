# Character and session schema

## Character

Use this compact shape when establishing an interview character. Keep `persona_id` stable and unique within the study, including follow-up panels. Omit irrelevant fields. Do not invent demographics to imply representativeness.

```json
{
  "label": "SYNTHETIC",
  "persona_id": "p1",
  "name": "fictional name",
  "situation": "task and circumstances",
  "entry_context": "how they arrived and what they already know or have done",
  "session_state": "relevant lifecycle state, if applicable",
  "acceptance_criteria": ["what would satisfy their goal in this situation"],
  "goals": ["desired progress"],
  "current_alternatives": ["existing workaround or substitute"],
  "constraints": ["relevant time, knowledge, access, or resource constraint"],
  "known_context": [{"detail": "supplied information", "source": "brief or research reference"}],
  "invented_assumptions": ["details introduced for this simulation"],
  "unknowns": ["material information not supplied"]
}
```

Use distinct display names when inventing a panel; retain supplied names and disambiguate duplicates with IDs. Carry the same ID into transcripts, annotations, and synthesis. For batch panels, summarize this schema in a persona table. Preserve consistency across turns. Do not make the character's problems fit the proposed product by construction. Add voice, occupation, location, or identity only when supplied or relevant, labeling invented details. A fictional language or accessibility profile is a perspective to investigate, not evidence from that community.

## Suggested questions

Separate participant role-play from researcher guidance:

```text
SYNTHETIC PARTICIPANT: [reply]
---
Suggested questions:
1. [neutral follow-up]
2. [neutral follow-up]
3. [neutral follow-up]
```

Keep questions concise, phase-appropriate, and responsive to the last answer. Do not constrain them to an arbitrary word count or steer discovery toward validating the Promise/Product. A requested output format takes precedence.

## State

Track the agreed brief, decision and uncertainty, phase, character assumptions, researcher/participant turns, and any separate observed evidence. Preserve source and uncertainty labels in summaries and downstream artifacts.
