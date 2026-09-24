# Usability checklist

Use this checklist on every design-review pass, within the affected journey and states. It adapts Jakob Nielsen's [ten usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) and the supplied *Psychological design ux usability heuristics.pdf*: Nielsen's summary is on page 2 and the psychological checklist is on pages 3–7. Use observed task needs to decide which changes each heuristic warrants.

## Nielsen Norman's ten heuristics

| ID | Heuristic | Check in the actual interface |
|---|---|---|
| H1 | Visibility of system status | Trigger loading, saving, completion, and failure. Can the person tell what happened and whether an action is still running? |
| H2 | Match between system and the real world | Do terminology, sequence, units, and control mappings fit the person's task rather than implementation concepts? |
| H3 | User control and freedom | Exercise back, cancel, dismiss, and relevant undo. Can people leave unwanted states without losing work or getting trapped? |
| H4 | Consistency and standards | Compare related states and platform conventions. Do labels, locations, icons, and action meanings remain predictable? |
| H5 | Error prevention | Try likely invalid input and costly mistakes. Do validation, defaults, constraints, or proportionate confirmation prevent harm before commitment? |
| H6 | Recognition rather than recall | Are choices, current context, selected modes, and needed prior input available at the point of use without memorization? |
| H7 | Flexibility and efficiency of use | Can new users find the basic path and repeat users complete frequent work efficiently? Preserve useful keyboard and touch paths. |
| H8 | Aesthetic and minimalist design | Apply the entrypoint's necessity test. Does supporting content compete with the task, and does removal preserve useful guidance? |
| H9 | Help users recognize, diagnose, and recover from errors | Cause a relevant failure. Is the problem understandable, the next action workable, and existing input preserved when possible? |
| H10 | Help and documentation | At a real point of uncertainty, is concise, task-specific help findable? Are its steps actionable without a long tutorial? |

Prefer actual behavior for interaction claims. Screenshots can establish visible labels and layout, but cannot prove saving, undo, validation, keyboard access, or recovery. For modes, check whether the same action changes meaning and whether the active mode is visible where the person is working.

## Working evidence and fixes

Use one compact row per heuristic: `ID | state and observation/evidence | status | fix and confirmation`. Reuse the caller's evidence or change log. Combine related defects under one fix tagged with the relevant IDs instead of creating duplicate work.

- **PASS:** observed evidence supports the check in the scoped states; not a product-wide guarantee.
- **FAIL:** a demonstrated defect or clear visible mismatch needs a scoped fix.
- **WATCH:** a plausible concern needs better evidence; identify what would resolve it.
- **UNTESTED:** relevant behavior or state was not exercised or accessible. Say why.
- **N/A:** genuinely outside the affected task, with a concrete reason. Missing access is UNTESTED, not N/A.

Prioritize blocked tasks, unintended consequences, and difficult recovery before minor friction. Preserve established business rules and explicit requirements; a smoother imagined path alone does not authorize changing them. Use safeguards proportionate to consequence: do not add confirmation dialogs to every reversible action. Minimalism does not override the other nine heuristics. If a short label, status, or instruction prevents a specific mistake, retain it or replace it with an equally understandable affordance.

Carry findings into the design-review's fix-and-confirm pass and update the same evidence rows. Report material fixes and remaining issues; show the full matrix when requested or useful for a formal review. Heuristic coverage alone establishes neither accessibility conformance nor how real people use the product.

## Useful psychological checks from the supplied PDF

The following task checks adapt the supplied seven-page PDF. Use the relevant rows and attach findings to the matching heuristic. Page and item numbers preserve the source for each adaptation.

| Situation | Review prompt and source | Related heuristics |
|---|---|---|
| Setup, forms, or optional tools | Can safe defaults and progressive disclosure remove unnecessary work while retaining discoverability? A concrete example may explain an unfamiliar input better than extra prose. Page 3, items 01.01–01.06. | H5, H6, H7, H10 |
| Dense screens or unfamiliar controls | Do interactive elements look actionable? Can people scan meaningful groups and finish the current task without juggling unrelated work? Pages 3–4, items 01.04 and 02.01–02.04. | H4, H6, H8 |
| Error-prone or consequential actions | Anticipate mistakes, preserve undo/recovery, and make consequential corrections visible. Break work into steps only when that reduces an actual error burden. Page 4, items 03.01–03.06. | H1, H3, H5, H9 |
| Multi-step tasks, comparisons, or returning to work | Keep the facts needed for the current decision available, even when they appeared on an earlier screen. Page 4, items 04.01–04.02. | H6 |
| Notifications, transitions, and asynchronous results | Make important changes noticeable where the person is working. Avoid irrelevant interruptions and offer detail on demand. Page 5, items 06.01–06.05 and 07.02–07.03. | H1, H8 |
| Unfamiliar terminology, metaphors, or workflows | Compare the interface with the person's known mental model. Use existing research or mark an assumption; explain novel behavior at the relevant moment rather than asserting it is intuitive. Page 6, items 09.01–09.05. | H2, H4, H10 |
| Visual grouping and status encoding | Keep related information near its controls, maintain readable text and appropriate contrast, and supply a non-color cue for meaning conveyed by color. Pages 6–7, items 10.01–10.05 and 10.07. | H1, H4, H6 |

The PDF's numeric memory/social limits, line-length claims, photo-angle preference, and persuasion suggestions need task-specific evidence. They do not require adding social features, alerts, or commitment steps. Base changes on observed needs, the design system, and applicable accessibility requirements.

## Sources

- Jakob Nielsen, [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/), Nielsen Norman Group; official page checked September 16, 2026.
- User-supplied Psychological design UX usability heuristics PDF, pages 2–7. The summary above works without access to the original file. Page 2 is an image; text extraction omits its heuristic summary.
