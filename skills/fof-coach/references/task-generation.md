# Generating new exam-style tasks

fof-practice, fof-review and fof-mock write **new** tasks by default. Use bank items only when the learner explicitly asks for them, during the fixed diagnostic placement, or as a fallback when a fresh task cannot be verified. The bank in [numerical-exercises.json](numerical-exercises.json) stays the checked reference for method and conventions.

## What a Foundations of Finance exam task looks like

Mirror the house style of recent course assessments, without copying their text or numbers:

- **One running story per sheet.** A single protagonist (a recent WHU graduate) carries through every section; each section opens with two to four sentences that move the story on and supply all data. The story is light and a little absurd, the finance is exact.
- **Section blueprint for a full 90-minute / 90-point simulation** (as in 2026; the current cohort's structure may differ): Value 16 · Bonds 16 · Portfolio theory 17 · CAPM 16 · Derivatives 16 · Blockchain/crypto 6 · Behavioral finance 3. Shorter sets keep the proportions roughly and say which areas they leave out.
- **Closed answers only.** The exam runs in ANS, so every exam-style item has exactly one correct answer that can be checked automatically. Allowed formats are listed below; nothing else goes into a mock or an exam-style sheet.
- **Item formats, mixed within a section:**
  1. Calculation with a bold target ("calculate the **NPV of Project X**"), points in brackets, *final answer rounded to 4 decimals, no rounding of intermediate values*.
  2. Fill-the-gap sentence with options in brackets: "Ben should ___ (proceed / not proceed) because the NPV is ___ (positive / negative / zero)."
  3. Single-choice with exactly four statements; one correct, three plausible distractors built from real misconceptions (see each chapter's misconceptions and [assessment.md](assessment.md)).
  4. True/false statements, each with one unambiguous truth value; never "it depends".
  5. Multi-part chains (a)(b)(c) where later parts reuse earlier results, e.g. bond prices → duration → immunizing weights → amounts invested.
- **One field, one result.** Each numeric field asks for exactly one number in a stated unit and form (e.g. "as a decimal", "in EUR"). A task that needs two numbers has two fields. Fill-the-gap gaps take one option from the list given in brackets. No "explain", "discuss" or "justify" items, no free-text answers, no multiple-select.
- **Conventions stated in the task:** return observations use the population formula (divide by n) and say so; annual compounding unless the story names a payment frequency; name the duration type explicitly (Macaulay or modified); options are European unless stated; give a short formula hint where the course did (e.g. MVP weight) when the item tests application rather than recall.
- **Data tables:** 4-year return tables (e.g. 2022–2025) for two stocks plus an index; cash-flow timelines with year and period rows; bond tables with face value, coupon, frequency and maturity.
- **Typical chains per area:** NPV → decision gap-fill → annuity/equivalent cash flow → growing perpetuity → IRR concept MC · bond prices → Macaulay duration → immunization weights and amounts → coupon/duration MC → CDS spread vs rating MC · mean/vol → covariance/correlation → MVP weights → MVP return/vol → diversification MC · beta → CAPM return → alpha gap-fill → replicating portfolio of risk-free asset and market → second stock's beta/alpha and buy/sell decision · fair futures price → cash-and-carry arbitrage with observed price → put-call parity / protective put / collar payoffs and break-even → strategy MC · crypto concept MCs · behavioral bias identification from mini-cases.

## Open questions

Open prompts ("explain why", "what would happen if") are useful for understanding and the Socratic dialogue may use them in practice and review. Every time one is posed, add one short line such as: *Exam format note: in the exam this is asked only in closed form (number, single choice, true/false or fill-the-gap), since it runs in ANS. The open version is for understanding.* Never put open items into a mock. When useful, follow an open question with a closed exam-style version of the same idea.

## Story bank

Reuse or remix freely; invent new ones in the same spirit. Keep every company, fund, bank, index and island **fictional**, even when its name winks at a real WHU initiative.

**Recurring cast and places (from recent course stories):** Ben, a WHU graduate who founds *Burgplatz Brewing Co.* (tropical IPAs, served in carafes) in the Caribbean and later runs a floating brewery; *Campus for Finance Capital Partners*, "a leading bank in the industry"; a competitor called *Europa Sport Global Advisory* / *Europasport Ventures*; the *Caribbean Beverage Index (BIX)* or a *WHU Index* as market portfolio; rum, tequila, tonic and soda stocks; the fictional island of *Aperitivo* with its own stock exchange; a graduation-ball start-up, an alumni reception financed by a bond, a carefully hedged cocktail cart, a "last round" of behavioral mini-cases.

**WHU world to draw on** (real context, fictional finance):
- Campus: Vallendar, Burgplatz, the Rhine and the Upper Middle Rhine Valley (UNESCO World Heritage), Koblenz at the meeting of Rhine and Moselle, Marienbergpark, the 24/7 library; the Düsseldorf campus on the Rhine.
- Campus for Finance: student association since 2001, runs the WHU New Year's Conference (January, investment banking focus), WHU Investment Banking Days in Frankfurt, the WHU Private Equity Conference (March) and Private Equity Days in Munich. Story hooks: a speaker's honorarium as a perpetuity, conference ticket revenue as an annuity, an LBO-flavoured NPV case, a PE fund's carry as an option payoff, sponsorship deals priced with CAPM.
- WHU Euromasters: Europe's biggest sports event for business schools, sports competitions plus theme parties. Hooks: jersey and equipment orders hedged with forwards or FX forwards, tournament-day weather as states of the world, team-transfer "betas", party-ticket pricing.
- IdeaLab! (WHU Founders' Conference): start-ups pitching to VCs, a natural home for NPV/IRR, multiple IRRs and term-sheet options.
- SensAbility (WHU Impact Summit): sustainable funds, green bonds, ESG portfolio constraints.
- WHU Students Help: charity-concert proceeds invested for a community project (annuity due dates, immunization of a known future payment).

Avoid making real people the protagonists, inventing financial facts about real organizations, or anything mean-spirited about student groups. Do not reproduce original exam wording, numbers or answer options.

## Generation procedure

1. **Pick the target** from the study plan and passport: competency IDs, difficulty (easy recall → standard exam → stretch), and format. Ask the learner when it matters and is unknown (topic, length, timed or untimed, German or English, "same story as last time?").
2. **Choose the story beat** and continue an ongoing story within a session or mock. Record the story so the next task can continue it.
3. **Design clean but not trivial numbers.** Choose inputs so results are finite and economically sensible: positive prices, a discount rate above growth for perpetuities, liability duration between the two bond durations for immunization, no arbitrage-violating option prices unless arbitrage is the point, variance > 0, short-sale weights only when the item allows them. Change at least the numbers and story compared with any bank or earlier task.
4. **Solve it before showing it.** Compute every requested field with full precision and round only the final answers. Use host code execution with [fof_calc.py](../scripts/fof_calc.py) when available (`python fof_calc.py <function> '<json args>'`, `python fof_calc.py --help`), otherwise compute twice by independent routes (e.g. formula and cash-flow table; parity and replication). If the two routes disagree, fix the task or discard it. Never present an unverified generated answer as checked.
5. **Write the task** in the house style above: story, data table, numbered items with points, explicit rounding and conventions. Hold the solution, the answer key per field and the distractor rationale privately for grading; do not print them before the attempt.
6. **Log it.** Record the task in Learning-Protokoll as `source: generated`, with story, inputs, competency IDs, answer key and verification route, so a later session can re-grade or reuse the story. A generated task counts as a new task family for evidence purposes only if its method differs from or its inputs are genuinely new to the learner.

## Quality checklist before presenting

- All data needed is present; nothing depends on the story's jokes.
- Every requested field has exactly one correct answer: one number at 4 decimals, one correct option among four, one truth value, or one option per gap.
- No open, free-text or multiple-select item is in an exam-style sheet; an open practice question carries the exam format note.
- Units, compounding, n vs n−1 and the duration type are stated.
- MC distractors are each wrong for a specific, teachable reason.
- The item tests the competency the plan asked for, not an excluded or advanced extension unless labelled.
- Difficulty and time fit the request (≈ 1 point per minute in a timed mock).
