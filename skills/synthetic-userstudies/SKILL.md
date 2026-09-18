---
name: synthetic-userstudies
description: "Simulate persona interviews, research panels, product walkthroughs, and multi-turn users of AI products. Use for explicitly synthetic or simulated research; findings are hypotheses, not customer evidence."
---

# Synthetic UX research

Use role-play to explore assumptions, rehearse interviews, and anticipate friction. Label sessions, characters, transcripts, and quotes **SYNTHETIC**. Generated stories and reactions are hypotheses, not customer observations or evidence of demand.

## Frame the study

Reuse the brief. State the decision, audience, situation, and uncertainty the study should address. Ask only for missing context that would change the study; otherwise state assumptions. Use the four Ps to organize available context:

- **Persona:** goals, circumstances, alternatives, constraints, and experience.
- **Problem:** the proposed unmet need, including whether it matters.
- **Promise:** the proposed outcome, if known.
- **Product:** the artifact or features, if known.

For problem discovery, Promise and Product may remain unknown; do not autofill them merely to start. Keep solution details out of the participant brief until introducing a concept. Choose personas by relevant behavior and circumstances; do not infer competence, trust, or needs from identity alone. Use stable `persona_id` values and distinct invented names, following [schema.md](references/schema.md).

For each persona, state how they arrived, what they already know or have done, and their relevant lifecycle state, such as first visit, return, trial ending, cancellation, or win-back. Define what would satisfy their goal in this situation, without prescribing a design or forcing dissatisfaction. In discovery, this can describe a satisfactory current workaround; it need not assume a product exists.

For panels, explain the distinct situation or constraint each persona covers and name material gaps left untested. Choose the smallest panel that covers the decision; overlapping concerns are valid. Include lifecycle and access differences when relevant rather than defaulting to first-time users or a fixed roster.

Choose the requested mode below and state the research phase from [principles.md](references/principles.md). For any requested scores, define one shared rubric. Label them subjective role-play ratings, never measured probabilities.

## Evidence and recommendations

Keep four sources distinct: supplied research with citations, observed interface behavior with reproduction evidence, simulated reactions, and analyst inference. Describe supplied observations as reported unless independently inspected. Reserve "reproduced" for actions executed and observed in this session. A visible paywall establishes an interface state; it does not establish deception or measured abandonment.

Agreement across personas remains a recurring hypothesis. It does not establish prevalence, confidence intervals, conversion, willingness to pay, or a winning variant. External research can support a mechanism without validating this product or audience. A funnel drop alone does not establish its cause.

For consequential recommendations, use the [simulation-quality review](references/simulation-quality-review.md) before synthesis. Give the hypothesis, supporting evidence and limits, a plausible alternative explanation, and the next real-world check. State what result would change the recommendation. Prioritize by consequence, audience relevance, and uncertainty. Fix reproduced defects within existing authorization; keep unverified reactions provisional. Preserve source labels in reports, empathy maps, journey maps, and storyboards. When a study informs an empathy map, link each simulated note to its persona and session and keep its SYNTHETIC label visible. Published first-person statements remain attributed reported evidence; do not mix them into a fictional participant’s testimony.

## Visual studies

For app/site walkthroughs, rendered variant comparisons, and gate reviews, deliver **actual screenshots annotated in the persona's voice**. Follow [screenshot-annotations.md](references/screenshot-annotations.md), including its delegated-review brief and coverage check. Text-only interviews, nonvisual artifacts, and explicit format requests keep their appropriate format.

Start with an unguided first-screen impression. Before revealing the intended promise or coaching the next action, ask what the product is for, its main benefit, and what the persona would do next. Compare the response with the agreed product vision; if the brief already disclosed the answer, use fresh participant context or label the response informed. When recall matters, ask what stands out after the walkthrough without restating the pitch. These simulated answers suggest comprehension or focus issues; they do not prove customer understanding or memory. For redesigns, compare the available original on the same task. Have each persona inspect the actual image before attaching reactions to controls, copy, or regions. Lead with a readable annotation board and short synthesis. No findings is a valid result; do not manufacture complaints.

If capture or image inspection is unavailable, name the gap and provide scoped text findings. Never substitute a generated mockup for the actual screen or claim prose is an annotated screenshot.

## Interviews

Read [principles.md](references/principles.md), [schema.md](references/schema.md), and the participant prompt in [prompts.md](references/prompts.md). Use [questions.md](references/questions.md) to seed phase-appropriate questions, then follow the conversation. Simulate specific episodes, actions, competing priorities, and consequences. Allow indifference, uncertainty, satisfaction with an existing workaround, or no relevant experience. Do not turn the participant into a helpful product adviser.

For an interactive interview, show compact character JSON. Keep replies conversational and separate them from three neutral suggested follow-ups using the schema. Step out of character when asked to change context, inspect the character, or summarize; resume only when continuation is intended.

For "conduct/run the interview," ask and answer up to six turns by default, respecting the requested length or interruption. Stay in problem discovery unless concept reactions are requested. End with hypothesized patterns, illustrative synthetic quotes, counterexamples, and useful next real-user questions. Batch reports should lead with decision implications, a compact persona table, decisive excerpts, and differences between personas. Keep full transcripts as supporting detail unless requested; omit per-excerpt follow-up suggestions.

For requested autofill, follow [prompts.md](references/prompts.md). Return 1–3 provisional suggestions for the user to choose or edit. Do not replace the agreed brief merely because alternatives were requested.

## Variant panels

Compare the exact supplied or observed names, copy, or UX alternatives. State missing context instead of inventing shipped behavior. Choose personas for meaningful differences in goals, alternatives, experience, time pressure, trust, language, or access needs. Two may suffice; add more only for distinct coverage. Include a plausible satisfied user or non-problem case alongside relevant skeptics.

When delegation is available and authorized, give each persona the same variants, task context, and output format in a self-contained brief. Otherwise conduct the persona sessions one at a time. Keep their answers and the researcher's preferred conclusion out of each other's context. Vary presentation order where practical. Separate sessions reduce contamination but remain simulated perspectives.

For names, capture unaided meaning before revealing the product description, then assess fit using the same description for every name. If the context was already revealed, label reactions informed or use a fresh persona context. Explore existing alternatives, reasons to investigate, and choosing none.

For each variant, record a short reaction, interpretation, simulated action, and reason or uncertainty. Use a consistent format:

`VARIANT | INTERPRETATION | SIMULATED ACTION | REASON / UNCERTAINTY`

Report conditional preferences, tradeoffs, and counterexamples. Do not declare a winner by vote. Localization role-play may suggest wording concerns; consequential language judgments need competent language review.

When comparing product concepts, distinguish appeal from incremental value over the current alternative: what the persona already does, what remains satisfactory, what work or outcome would change, and any switching burden. A familiar, highly ranked concept may duplicate an existing solution. Keep these assessments synthetic unless supported by real evidence.

## Walkthroughs

Use for apps, onboarding, courses, or documents people move through. Establish audience competence, prerequisites, and the intended task. Before judging completion, identify whether screens are independent alternatives or sequential steps, what is scripted, and the intended stopping point. Missing production capabilities and hypothetical expectations are separate from failures within prototype scope. Do not invent cross-variant handoff requirements. If scope is unclear, make the assessment conditional.

Assign full paths when continuity matters. For long artifacts, divide work into coherent sections, carry prerequisite and state context across boundaries, and check handoffs. Cover waiting, retry, abandonment, and recovery where relevant without expanding the requested scope. Carry task-relevant situational constraints from the brief, empathy map, or criteria into the walkthrough. State which conditions were actually exercised and which were only imagined; verify the decisive action and recovery where execution is available. Keep hypothetical constraints labeled and avoid imposing a standard device or context checklist.

At each meaningful step, record the task and expectation, exact source or state, observed response, simulated reaction, suspected friction, alternative explanation, and proposed check. Verify objective failures with tools before calling them bugs. Investigate a relevant access barrier even if only one persona encounters it; assess its relevance to the intended audience and verify it independently.

For live persona walkthroughs, follow [embodied-persona-live-browser.md](references/embodied-persona-live-browser.md). For agent-executed tutorials, also read [walkthrough-demo-dependency-checklist.md](references/walkthrough-demo-dependency-checklist.md). A mental trace identifies risks; it does not prove execution failed.

For independent tasks, record relevant prior exposure and moderator help. Earlier tasks may teach a destination or term; a screen reset alone does not erase that knowledge. Use fresh participant context or counterbalanced task order when first-attempt findability is the question. Preserve learned state when continuity is the question, and report these conditions separately.

For time-spanning scenarios or studies used to evaluate the simulator itself, read [temporal studies and archive comparisons](references/temporal-and-archive-studies.md). Do not add a longitudinal protocol to a simple screen review.

## Multi-turn users of AI products

When testing how an AI product clarifies and carries out a user's task through conversation, follow [multi-turn collaboration](references/multi-turn-collaboration.md). Run the simulated user against actual target responses when execution is available; keep private persona context separate from the target and verify the resulting work independently. A researcher interviewing a fictional participant remains an interview; ordinary screen reviews do not require this mode or Harbor.

## Adversarial walkthroughs

Use when explicitly asked to test as a skeptical, impatient, or reluctant user. Follow [adversarial-walkthrough.md](references/adversarial-walkthrough.md): one relevant persona, one concrete task, explicit abandonment triggers, then an assessment outside the role-play. Successful paths and no material findings remain valid outcomes. Ordinary walkthroughs do not become adversarial by default.

## Gates and paywalls

Use for one blocking flow. Inspect the trigger, preceding action, exact copy, price and conditions, and escape or recovery path. Label mockups as proposed flows. If analytics are accessible within scope, check event definitions and funnel denominators before interpreting drop-off. Missing analytics do not block a labeled simulation.

Choose personas by relevant constraints and alternatives. For each, record the expectation, exact triggering copy, synthetic reaction and action, and hypothesized reason. Consider misunderstood actions, unclear terms, price/value mismatch, premature gating, technical failure, missing prerequisites, and legitimate access requirements. Compare remedies against those causes and product constraints; moving the gate is only one option.

For live verification, use [predict-then-reproduce-live.md](references/predict-then-reproduce-live.md). Report reproduced states separately from proposed psychological or conversion effects. If the surface is unavailable, deliver offline findings and name the missing evidence.

## Retest after changes

When evaluating a revision, reuse the same persona IDs, tasks, success criteria, and comparable starting states. Record the versions, screenshots, and relevant environment or model changes. Use fresh participant context so prior answers do not steer the retest. Disclose differences that limit comparison; matching personas does not make generated responses deterministic.

Compare the changed screen separately from later steps. Report how many sessions reached each screen alongside its friction findings. More downstream complaints may reflect more sessions getting there, a regression, or both. Inspect the relevant states before deciding. Counts describe these synthetic runs, not customer prevalence or conversion.

For apparent failures, distinguish a reproduced product defect, an accessibility barrier, an executor or provider error, a prototype limitation, and an unverified reaction. Check the screenshot, available accessibility information, and action result before declaring a feature missing. A failed tool action is not proof the product failed. Verify completion against the agreed end state; the persona saying "done" is insufficient.

Keep all attempts, including failed runs and retries, with their status and evidence. Report incomplete pairs and infrastructure errors separately; do not select only the best run per persona. Summarize what changed, what was reproduced, what remains uncertain, and the next real-user check. Retest disputed findings within scope rather than running batches until a preferred result appears.

## Tools and scope

Use tools exposed in the current session and read the active browser tool's documentation before operating it. Example recipes are not API contracts. Keep actions within existing authorization; role-play does not authorize sign-in, personal-data submission, messages, publishing, deployment, or spending. If a required surface is unavailable, state the limitation and continue useful offline work.

Maintain the brief, character assumptions, research phase, and separate researcher/participant histories across turns and handoffs. Preserve source and uncertainty labels in summaries and handoffs; a hypothesis remains a hypothesis when drawn in a map or storyboard.
