# Course scope and evidence

Snapshot: 23 November 2026. This is an independent learning companion for WHU Foundations of Finance, based on the supplied 2025–2027 teaching archive. It is not an official announcement or a prediction of future questions.

## Included

Seven teaching areas are included: Value; Bonds; Neoclassical finance and portfolios; CAPM; Derivatives and exchange rates; Blockchain/cryptoassets; Behavioral finance. The numbered course companion, extended chapter 12, competency map, and worked practice are bundled. Topics are available for explanation, application, misconception checks, retrieval practice and mixed assessment. The exact leaves and source locators are in curriculum.json and coverage.md.

The archive includes lecture decks, formula references, key terms, review sessions and historical assessments. The latter informed the range of skills and numerical conventions; original exam text and answer keys are not bundled. The 2027 folder contains inherited context and a prior Value pilot; its folder name does not by itself establish a new finalized curriculum. The full-course Markdown located during this audit is under 2026, not 2025. The learning edition extends it without overwriting the original.

## Course coverage versus exam coverage

The syllabus limits exam relevance to what was actually covered in class. Archived slides and a broad formula reference cannot prove every oral inclusion or exclusion for a future cohort. Therefore all evidenced topics remain available for learning; the plugin does not promise that any individual topic will or will not appear in a future exam. If an instructor supplies an explicit, dated scope update, record the affected competency IDs and cohort in a `scope_override` in the learner's passport. Do not treat a student's guess as an authoritative exclusion, or generalize an exclusion from a single practice paper.

Default progress includes the full bundled curriculum. If a student explicitly requests a narrower goal, show both that goal's progress and full-course untested coverage; never silently relabel a narrowed score as full-course readiness. The deterministic score uses the full map. An instructor-authorized exam-only subset needs a separately labelled recalculation, not deleting unseen topics.

## Boundaries

The following are outside the default learning objectives: deriving Black–Scholes, stochastic calculus, multi-period option trees, advanced Greeks/volatility calibration, a full multifactor asset-pricing course, coding a quadratic-programming optimizer, full corporate-finance/WACC/M&A models, trading signals as investment advice, crypto protocol engineering and current market predictions. Black–Scholes and constrained optimization are mentioned conceptually in lectures; this does not establish a derivation or programming requirement. One-period binomial replication and broader option combinations are included because the supplied formula/course/review material supports them.

Treat requested extensions as extensions, explain that they do not change the FoF progress denominator, and answer if appropriate. Corporate Finance is a separate subject. A missing topic in this package is a coverage limitation, not evidence that it is excluded from every FoF class.

## Source interpretation

Newest explicit course scope updates take priority for the relevant cohort. For concepts use the lecture evidence together with the formula reference, checking assumptions rather than reproducing errors. Summaries and old assessment solutions are supporting material. For important known conflicts:

- **Duration:** standard annual-effective yield sensitivity uses Dmod=DMac/(1+y). Some legacy worked solutions use -DMac*delta-y. Name the requested approximation; do not merge them or assert the two are equal.
- **Risk-free model:** a historical low-risk EURIBOR proxy with observed volatility is not a literally zero-volatility model asset. State the idealized assumption when applying the CML.
- **Risk and rationality:** the slide argument uses concavity and distributional assumptions. Rationality alone does not force risk aversion, and expected-utility theory does not universally reduce to mean and variance.
- **Crypto:** public chains are usually pseudonymous, hashing is not encryption, and proof of history is an ordering mechanism used alongside consensus. Historical rewards, supplies and energy figures are not present-day facts.
- **Performance:** forecast alpha, realized return differences, and a raw regression intercept are different quantities. Beta matching is not state-by-state payoff replication.

No current prices, dates, administrative exam rules or external service connections are required to learn from this package.
