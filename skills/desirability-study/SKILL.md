---
name: desirability-study
description: Evaluate design and concept desirability using reaction words, with optional personal-relevance and adoption probes. Use to compare visual directions or explore audience fit while separating appearance from desire to use; supports explicitly synthetic participants.
---

# Desirability Study

Capture how a design comes across through shared reaction words. For broader desirability questions, separately explore personal relevance and conditional willingness to adopt.

## Frame

Reuse the audience, decision, and supplied designs. Establish whether the study concerns visual appearance or the broader product experience. Inspect the actual stimuli: screenshots can support appearance judgments; claims about the experience require the relevant flow or session material.

For “would this audience want it?” questions, include a neutral proposition brief covering the benefit, required setup, recurring effort, dependencies, price or subscription, and current alternatives where material. Verify existing-product facts; label proposed conditions and unknowns. If only an advertisement is available, limit conclusions to first impressions and leave adoption unresolved.

Include relevant experiential qualities such as fun, satisfying, rewarding, motivating, helpful, and supportive of creativity, alongside contrasting reactions. Keep these associations distinct from usability goals such as effectiveness, efficiency, safety, utility, learnability, and memorability. Participants can describe perceived usability, but establishing those goals requires appropriate task evidence. For an unbuilt concept, report anticipated experience.

Record intended brand attributes before analysis, keeping them out of participant-facing instructions until selections are complete. Use supplied participant responses when available. Generate participant reactions only when synthetic research is requested or established in context; otherwise prepare the study or analyze available responses. Label synthetic sessions and invented persona assumptions.

Choose the method for the decision: reaction words address perceived qualities; unaided interpretation addresses name meaning; first-click or tree testing addresses navigation findability. Use [interaction-design's navigation testing reference](../interaction-design/references/navigation-testing.md) when the unresolved question is where people expect to find a capability. Do not substitute word selections for task performance.

Record whether the stimulus is visual, verbal, combined, or an experienced flow, along with its version and relevant exposure conditions (such as crop, language, order and prior use). A combined stimulus supports reactions to the combination; it does not isolate the effect of copy or visual treatment. When preparing new collection, pilot unfamiliar word choices before the main comparison and preserve the shared vocabulary once collection begins; disclose later revisions. For existing response sets, analyze the vocabulary used and report any limitations without requiring a new pilot.

## Synthetic participants

Use [synthetic-userstudies](../synthetic-userstudies/SKILL.md) for persona construction, stable persona IDs, and simulation-quality review. Choose the smallest panel covering meaningful differences in needs, routines, alternatives, and experience. Demographics alone do not determine technology interest or desire. Keep this skill's word-association visual as the primary output.

Run each persona in a separate subagent with fresh context (`fork_turns: "none"` when supported). Supply a self-contained brief containing only that persona, neutral study instructions, the actual stimuli or accessible artifact paths, the shared reaction-word set, and the response format. Keep the parent conversation, intended brand attributes, preferred conclusions, and other participants' responses out of the brief. Each subagent must inspect the supplied stimulus before reacting.

Return `persona_id | design_id | exposure stage | selected words | participant explanations | uncertainties`; for broader studies also return `personal relevance | current alternative | conditional choice | decisive tradeoff`. Keep neutral follow-up questions in that participant's own session. The parent collects responses and performs cross-participant analysis after independent selections are complete. Use fresh participant sessions for retests. If isolated subagents are unavailable, report that limitation rather than presenting same-context role-play as isolated research.

## Run

- Use one balanced set of positive, neutral, and negative reaction words across comparable designs. A short, study-specific set of roughly 15–25 words is usually sufficient. Match words to the scope; appearance-only studies need appearance-relevant vocabulary. Identify an adapted set as adapted.
- Present designs under comparable conditions. For separate sessions, vary design and word order where practical and keep other participants' answers out of context.
- Check comprehension of the selectable reaction words before selection; record unfamiliar wording in the stimulus separately. Ask participants to select up to five words that best describe each design. Preserve their selections and any unfamiliar or inapplicable terms.
- Probe the important selections neutrally: “What in the design made you choose that word?” Capture the participant's meaning, the exact element or moment, and any tension between words. Let them clarify or revise their selection without coaching toward the intended positioning.

For broader desirability studies, first preserve the initial word selections, then deliver the proposition brief in a follow-up to each isolated participant. Keep later-stage material out of the initial subagent context. Ask:

- “Where would this fit into your day, if anywhere?”
- “What do you currently do instead, including doing nothing?”
- “Given these benefits and commitments, would you choose this, your current approach, or neither? Why?”
- “What, if anything, would change your choice?”

Record any changed associations separately. For consequential additions, removals, or changes in meaning, ask what specifically prompted the change and what the word means to the participant. Indifference, rejection, interest, and unresolved choices are all valid; probe benefits and burdens without assuming either should dominate.

## Report

Lead with a word-association visual tied to the particular design or concept. For one audience, show its selected words; for two audiences, show shared and distinctive words in a Venn diagram or equivalent grouping; for multiple designs, show comparable word groups beside each stimulus. Make any rule for selecting top words explicit. Keep explanations and recommendations secondary, using a compact table only when useful.

Compare reactions against the intended attributes after collecting selections. Distinguish participant explanations from analyst interpretations. Highlight the strongest mismatch, meaningful disagreement, and a concrete revision to explore. Keep full response records secondary.

Separate stated objections from evidence that a remedy would change the choice. When several conditions are introduced together, attribute reactions to the combined proposition and retain the participant's explanation. To explore a proposed remedy, vary that condition while holding the others fixed; a synthetic response remains a conditional hypothesis.

For broader studies, place a compact `Appearance | Personal relevance | Conditional adoption` readout beside the word visual. Positive adjectives can coexist with no desire to use. State which dimensions remain untested, and distinguish reported or simulated choices from actual adoption. Tie each proposed change to the relevant dimension rather than treating a visual improvement as a solution to weak relevance.

For multiple participants, calculate word-selection frequencies from recorded selections, showing the denominator for each design or segment. Synthetic frequencies describe those simulations, not customer prevalence. Perceived qualities such as trustworthiness do not establish actual trust, usability, demand, or conversion. Explain conditional preferences rather than declaring a winner from word counts alone.

Retest revisions with the same vocabulary, audience definition, and comparable exposure; use fresh context for synthetic participants. Note changes that limit comparison.

Method reference: [NN/g: Using the Microsoft Desirability Toolkit to Test Visual Appeal](https://www.nngroup.com/articles/microsoft-desirability-toolkit/).
