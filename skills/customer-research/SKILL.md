---
name: customer-research
description: Gather and synthesize customer evidence from interviews, surveys, support records, reviews, and communities. Use for voice of customer, ICP research, evidence-based personas, jobs to be done, and qualitative reasons for churn or purchase; use growth for funnel measurement and experiments.
metadata:
  version: 2.0.1-portable
---

# Customer Research

Find what customers actually say, do, struggle with, and value. Preserve the
source behind every material finding so a reader can verify it. This skill can
analyze supplied research, gather public evidence, or combine both; establish
which mode is in scope before proceeding.

If a product-marketing context file is available in the workspace, read it
before asking for facts it already contains. Ask first about the decision the
research should inform, the available evidence, target segment, and desired
deliverable; do not ask a long questionnaire when the request answers these.

## Modes

### Analyze existing assets

For interviews, sales calls, surveys, support tickets, NPS, win/loss notes, or
churn records, extract:

- functional, emotional, and social jobs to be done;
- pains, workarounds, and expectation mismatches;
- trigger events and desired outcomes, retaining customer wording;
- objections, alternatives (including DIY, hiring, or doing nothing), and
  decision criteria;
- role, company, use-case, tenure, and other segment signals.

Categorize tickets before synthesis (for example: bug, confusion, missing
capability, or expectation mismatch). Keep prompted answers separate from
unprompted language and quantitative selections. Do not average distinct
segments or churn causes into one customer story.

### Plan or conduct contextual research

When the request includes observation, interviews or diary research, read [field and longitudinal research](references/field-and-longitudinal-research.md). Use it to connect real episodes, artifacts, task demonstrations and follow-up questions. Preparing a study is not conducting it; contact and recording remain within existing authorization.

### Gather public evidence

Use available web search, page retrieval, or browser tools to find relevant
digital watering holes. Read [source-guides.md](references/source-guides.md)
for source-specific search and extraction guidance. Choose sources that match
the ICP: review sites for product evaluation, Reddit/forums for raw language,
Hacker News and technical communities for developer buyers, LinkedIn and job
postings for role and trigger signals, and app-store or video comments for
consumer workflows.

Search results and snippets are leads, not evidence. Open the source when
possible and record access limitations when it is blocked, truncated, behind a
login, or unavailable. Do not imply that an unobserved comment, feature, or
population exists.

## Evidence capture

Record each item in a quote bank or evidence table:

| Field | Requirement |
|---|---|
| Source | Platform, author or role if public, URL or asset ID |
| Date | Publication, interview, review, or access date as available |
| Verbatim quote | Exact words; use an omission marker rather than silently rewriting |
| Context | Prompt, thread, workflow, rating, or surrounding exchange |
| Signal | Pain, trigger, outcome, alternative, objection, praise, or language |
| Segment | Only what the source supports; leave unknown fields blank |
| Notes | Direct observation, interpretation, access gap, or contradiction |

Keep quotes traceable to a URL plus page/thread/comment location, or to a
transcript/survey/ticket identifier and location. Paraphrase only in a clearly
marked summary. Never invent quotes, review counts, engagement, or prevalence.

## Synthesis

Cluster related evidence by theme, then compare frequency, intensity, source
type, recency, and segment. Counts describe the collected sample; they do not
establish market prevalence. Explain the evidence basis for each conclusion
instead of treating a fixed sample count or numeric confidence threshold as
truth. Mark findings as observed, interpreted, or hypothesis where helpful.

For each important theme, report:

1. a concise summary;
2. the number and kinds of supporting items, without inflating duplicates;
3. representative traceable quotes;
4. who the signal may or may not represent;
5. contradictions, disconfirming evidence, and open questions;
6. the implication for messaging, product, positioning, or further research.

Check common source biases: reviews overrepresent strong experiences, support
records overrepresent problems, public forums skew toward engaged or skeptical
participants, and recruiter or founder posts are not representative of every
buyer. Treat engagement as a prioritization signal, not proof of prevalence.

For a consequential research decision, identify the uncertain behavior that must occur for the proposed benefit to hold, the smallest suitable check, and what result would change the decision. Choose criteria before observing results and explain any numeric threshold rather than inventing a target to make the idea pass. Keep intermediate signals distinct from outcomes: inspect the event definition, population, time window, denominator and sampling before translating a metric into a claim. A request for availability, for example, does not alone prove inability to book. A next-check recommendation does not authorize running an external experiment.

## Personas and JTBD

Build personas or JTBD maps only from the evidence available. Label proxy-based
personas as provisional and show the proxy sources. Do not fill unsupported
demographics, motivations, or buying power. A useful persona includes profile
signals, primary job, triggers, pains, desired outcomes and measures,
objections, alternatives, actual vocabulary, and reachable communities.

## Deliverables

Offer the format that fits the decision: synthesis report, VOC quote bank,
persona or JTBD map, competitive intelligence summary, or research-gap plan.
For copy requests, extract and verify the VOC evidence first, then hand off to
`copywriting` when that skill is available. For competitor comparisons, use
`competitive-analysis` when available. Do not contact people, publish findings,
or schedule monitoring unless it is within the user's existing authorization.
