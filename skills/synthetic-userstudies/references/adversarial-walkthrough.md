# Adversarial walkthrough

For visual study delivery, use [persona screenshot annotations](screenshot-annotations.md): preserve the action/evidence record below, and anchor synthetic reactions to the actual captured states.

Stress-test a real task with a plausible skeptical user, then separate observed friction from role-play. This is synthetic research, not customer testimony. Keep the challenge relevant to the task, without demographic stereotypes or a requirement to find faults.

## Set a fair challenge

Use one consistent persona and one core task unless the user requests broader coverage. Define the user's relevant experience, available time, access needs, trust concerns, current workaround, and reason to try the product. Ground these in the brief; label invented constraints. Age, gender, and other identity traits do not establish competence or patience.

State the task's success condition and plausible abandonment triggers before testing: an unclear charge, inability to recover entered work, an inaccessible control, or a time limit appropriate to the situation. Compare the flow with the existing workaround when evidence is available; do not invent a faster baseline. Skepticism does not mean deliberately ignoring clear instructions or acting incompetently.

## Attempt the task

For a reachable app, follow [the live-browser walkthrough](embodied-persona-live-browser.md). Local development, staging, and deployed environments are all valid within the user's scope. Use an appropriate existing test state; a fresh or expired-account state can expose different friction, but testing does not itself authorize registration, account changes, payment, or submission of personal data.

Attempt the core task rather than tour every feature. Cover entry and empty state, terminology, navigation, required steps, waiting, and error recovery where they affect that task. Observe readability and accessibility barriers when relevant. Record meaningful detours and steps; no universal click-count threshold establishes a defect. Elapsed time from agent/tool latency is not a measurement of human completion time.

For material observations, record the initial state, action, expected result, actual result, and screenshot or other reproducible evidence. Capture the synthetic reaction separately. Inspect console errors when available and useful for explaining an observed problem, not as a compulsory operation on every page. If an abandonment trigger occurs, record where the persona would stop; label any further diagnostic exploration as outside the persona's completed attempt.

Do not manufacture obstacles. A successful task, a clear recovery path, or no material finding is a valid result. An unavailable app produces an explicitly offline assessment, not a claimed live test.

## Step out of character and assess

A brief in-character reaction is optional unless requested. Label any quote synthetic; frustration or colorful language is not evidence of severity. Assess each material complaint using these distinctions:

| Finding | Required support | Next action |
|---|---|---|
| Reproduced defect or barrier | Observed state plus reproduction evidence; an access barrier need not affect every user | Propose or make an authorized focused fix |
| Plausible UX friction | Observed interaction plus a clearly labeled interpretation of its consequence | Prioritize by task impact, audience relevance, and uncertainty; name a real-user check |
| Preference or unsupported reaction | Personal taste, an assumption, or a complaint without supporting observation | Keep provisional or omit from recommendations; do not disguise it as a bug |
| Product opportunity | A proposed capability with a clear relationship to the intended task | Evaluate the benefit and tradeoff separately from defect severity |

For each consequential finding, consider a plausible alternative explanation, available recovery, and the smallest useful correction or validation. Do not dismiss a legitimate access need because it occurs in one persona or because most users can proceed. A feature request is not automatically a high-priority ticket. Compare real observations with known issues afterward to avoid duplicates; an existing issue does not establish its prevalence or prove neglect.

## Deliver the result

Report the persona/task and assumptions, environment and state tested, completion or abandonment point, observed evidence, simulated interpretation, and prioritized next actions. Include what worked when that informs the decision. State what remains untested; never turn a fictional quote into a customer quote or an abandonment hypothesis into a measured conversion effect.

Draft ticket-ready findings locally when useful. Creating external tickets or sending findings requires authorization for that action. An authorized ticket should include reproduction evidence, impact, and an actionable correction or validation step; a synthetic quote may illustrate the issue but cannot substantiate it. Keep the report proportional to the findings rather than filling a ticket quota.
