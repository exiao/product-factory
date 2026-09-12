# Focused navigation testing

Use a tree test to investigate labels and hierarchy independently of visual layout; use first-click testing for the entry point on an actual screen. Use a rendered task walkthrough when layout, content, execution or feedback may explain the issue. These methods answer different questions from visual desirability.

1. Define a meaningful goal and legitimate destinations. Check whether multiple routes can satisfy it before treating one designer-preferred route as the only correct answer.
2. Write a short scenario in the user's language without giving away the menu label or control being tested. Pilot ambiguous instructions; keep pilot changes distinct from measured sessions.
3. Match audience experience to the decision. Keep existing-product familiarity separate from prospective-user interpretation. Specify the starting point, task order and relevant previous exposure. Counterbalance independent tasks or use separate sessions when learning could bias results; preserve sequential tasks when continuity matters.
4. Capture first click, chosen path, backtracking, final destination, assistance, abandonment and explanation as available. Define direct/indirect success and keep it separate from completion of the underlying product action. An inaccessible tool or prototype limit is not a participant failure.
5. Report task-level counts with denominators and the common alternative destinations. Inspect whether errors suggest a label problem, hierarchy problem, competing destination or misleading task. Do not pool unlike cohorts or tasks into a reassuring average.
6. Check the resulting change in the actual interface when visual placement or action effects matter. A correct tree destination does not demonstrate that the real task works.

Synthetic navigation runs generate hypotheses and can expose executed product behavior; their counts are not human findability estimates. Do not add a tree test to an already settled small UI change solely to complete a process.
