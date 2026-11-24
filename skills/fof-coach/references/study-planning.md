# Adaptive study planning

## Interview before assigning dates

Read the existing learning protocol first. Ask only for constraints not already known. Start with one short, personalized question; collect these points over a few turns or a compact grouped reply:

1. When is the exam or learning deadline, in the student's local timezone? If not known, create an **undated provisional plan** and flag what will change once the date is known.
2. Which days and how many realistic minutes can the student study? Ask about unavailable dates and preferred block length; never infer that every evening is free.
3. What has already been covered, what feels difficult, and is there a recent diagnostic/protocol? Self-report is useful for choosing questions, not assigning mastery.
4. Offer to run or refresh `fof-diagnose` before finalizing priorities. If declined, base the first plan on labelled self-report and reserve an early diagnostic/check block. Do not require the learner to repeat answers already in the protocol.

Also accommodate language, accessibility, calculator confidence and a specific learning goal when relevant; do not force an extensive questionnaire. All skills may ask focused follow-ups when a missing individual constraint affects the next step. Keep diagnostic questions separate from scheduling questions.

## Build a feasible plan

Use actual attempts, the curriculum prerequisite graph and the deadline. Separate **learning**, **retrieval review**, **mixed practice** and **mock assessment**. Repair weak prerequisites before tasks that depend on them. Allocate spaced reviews (suggested 1/3/7/14-day ladder) and mixed recall, not only rereading. Use an early broad diagnostic to avoid overfitting to the latest practiced topic. Include utility/EMH, FX, crypto and the full behavioral glossary in the coverage check.

For each block show date or provisional order, minutes, competency IDs and plain topic names, activity, concrete task and success criterion. A criterion can be “explain the date of the perpetuity value and solve a fresh delayed-payment task without hints.” Merely spending 30 minutes does not establish mastery. The seven-area readiness index stays separate from whether the calendar plan is on schedule.

Verify total daily minutes against the student's budget, exclude unavailable dates, keep all preparation blocks before the exam, and leave recovery space if the time permits. Do not promise full mastery when capacity is insufficient. Show uncovered objectives and the tradeoff: narrower priority coverage, more time, or a longer horizon. Ask which to choose when it materially changes the plan. A partial feasible plan with visible gaps is better than an impossible full syllabus squeezed into a weekend.

No exam date is needed to begin useful learning. Without it, show a sequence with review intervals and explicitly avoid invented calendar dates. If the deadline has passed, ask for the new goal rather than scheduling in the past. Date-only deadlines mean preparation ends the preceding day unless the student specifies otherwise.

## Persist and adapt

Write `Learning-Protokoll/LERNPLAN.md` and `plan.json`, with created/updated dates, constraints, evidence basis and version. Keep prior revisions as events. Every other skill reads these before choosing work, completes only work actually done, and records deviations.

After a difficult task or failed retrieval, schedule repair plus a new check and move dependent blocks within remaining capacity. After strong independent recall, reduce redundant repetition and use the time for untested/weak areas. After a missed session, rebalance future work without treating absence as incorrect answers. Ask again if the deadline or availability changes. Preserve completed history, and show the one or two meaningful plan changes rather than reprinting the whole plan each turn.

These are local planning files, not reminders or automatic tasks. Do not create a calendar event, send a message or schedule an automation unless separately requested. Plain-language planning and native Markdown/JSON files are sufficient; no external planner plugin is required.

## Plan data

Use `schema_version: 1`, `plan_id`, `version`, `updated_at`, `deadline` (ISO date or null), `timezone` (known zone or null), `basis` (observed diagnosis/self-report/provisional), `constraints` (availability and exceptions) and `blocks`. Each block has `id`, `date` (ISO date or null), `minutes`, `competencies`, `mode`, `task`, `success_criterion` and `status` (planned/in-progress/completed/deferred). Preserve the block ID when rescheduling the same work. Completed work also needs its linked learning event; the plan alone is not evidence of competence.
