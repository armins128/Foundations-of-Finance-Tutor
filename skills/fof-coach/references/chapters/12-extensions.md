# 12. Complete-course extensions and clarifications

This chapter fills gaps found by comparing the existing course context with the six lecture decks, the 2025 key terms, review sessions and the formula reference. It is an explanatory learning edition. Source locators below identify archive documents; students do not need those documents to use this chapter. Formal derivations beyond the supplied course are not assumed.

## 12.1 Efficient markets

The efficient-market hypothesis describes which information is already reflected in prices. **Weak efficiency** concerns past prices/returns and challenges systematic excess returns from technical analysis. **Semi-strong efficiency** includes all public information, such as published earnings. **Strong efficiency** includes private information as well. These are nested information sets, not three levels of guaranteed investment safety.

An unexpected announcement can move an efficient price sharply: information changing is compatible with efficiency. An occasional successful investor is also compatible with luck. Test a claim of outperformance against its risk, information available at the time, costs and a suitable benchmark. Behavioral observations can challenge an assumption without proving that an exploitable strategy survives trading costs and risk adjustment.

Lecture language sometimes condenses rationality, concavity, normality and mean-variance choice into one chain. These are distinct assumptions. Rational preferences alone do not force risk aversion or prove market efficiency. Source: 2026 Neoclassics pp. 2–6; 2025 Key Terms pp. 1–2.

## 12.2 Expected utility, certainty equivalents and risk attitudes

For mutually exclusive states j with probabilities p_j summing to one and terminal wealth W_j, expected wealth and expected utility are different objects:

\[
E[W]=\sum_j p_j W_j,\qquad E[U(W)]=\sum_j p_j U(W_j).
\]

An increasing utility function ranks more wealth above less wealth. A **certainty equivalent** CE solves U(CE)=E[U(W)]. For U(W)=ln(W+1), W must exceed -1 and CE=exp(E[ln(W+1)])-1. For a stated function U(W)=a-exp(-W/b), b>0, invert it as CE=-b*ln(a-E[U(W)]). Include initial wealth consistently if the question specifies it; utility of a bare payoff and utility of total wealth are not interchangeable.

Define the monetary **risk premium** as E[W]-CE. With strictly concave increasing utility and nondegenerate risk, it is positive; with linear utility it is zero; locally convex utility can imply risk seeking and a negative premium. Jensen's inequality gives E[U(W)]<U(E[W]) in the strict concave case. Do not mistake an expected utility number for currency or an expected return.

The lecture's named choice axioms are dominance, completeness, transitivity and independence. Completeness permits ranking alternatives; transitivity makes rankings internally consistent; dominance rejects an inferior outcome in every state; independence preserves a preference when both lotteries are mixed with the same third lottery in the same proportion. Independence does not mean statistically independent asset returns. The broader formal expected-utility representation also has regularity assumptions; do not present this short slide list as a complete mathematical theorem.

Source: 2026 Neoclassics pp. 6, 8–13; 2025 review pp. 14–15. Original numerical practice: Q14.

## 12.3 Mean-variance preferences and feasible portfolios

The course uses U approximately equal to mu-b*sigma^2, with positive risk-aversion parameter b. The scale matters: returns in decimals and returns in percentage points require compatible b. At fixed utility, mu=U+b*sigma^2; the indifference curve is upward and convex when horizontal risk is standard deviation. Higher b asks for more expected return to accept a given variance. This curve is not the wealth utility function: a convex indifference curve is compatible with concave wealth utility.

Without a risk-free asset, an interior optimum is where the highest attainable indifference curve touches the efficient frontier. With a frictionless risk-free asset and a tangency portfolio, investors choose a mixture along the relevant capital-allocation line. Calling that portfolio the market portfolio uses additional CAPM equilibrium assumptions. A cash-market proxy with small observed volatility is not the idealized model's zero-volatility asset.

The portfolio problem is to minimize w' Sigma w for a target expected return, with sum w_i=1 and the stated constraints. Negative weights are short positions or liabilities. Adding a no-short-sale rule or maximum weight shrinks the feasible set and cannot improve the best mathematical frontier with the same information. The 2025 deck explicitly illustrates unconstrained, long-only and 20%-cap portfolios; understanding the effect is supported course material. Implementing a many-asset quadratic solver is not required by this learning package. MVP is the minimum-risk point, not generally the investor's highest-utility point. Source: 2026 Neoclassics pp. 9–11, 23–30; 2025 Neoclassics pp. 27–37.

## 12.4 Probability states versus return observations

For equally weighted observed returns r_1,...,r_n, the course's population convention is mu=(sum r_t)/n and variance=(sum (r_t-mu)^2)/n. For unequal-probability states, use the probabilities instead:

\[
\mu_A=\sum_j p_j R_{A,j},\quad
\sigma_A^2=\sum_j p_j(R_{A,j}-\mu_A)^2,\quad
\operatorname{Cov}(A,B)=\sum_j p_j(R_{A,j}-\mu_A)(R_{B,j}-\mu_B).
\]

Correlation divides covariance by sigma_A*sigma_B if both volatilities are positive. Do not divide by n a second time after probability weighting. Expected return and covariance can be negative; variance cannot. A tiny negative numerical variance from floating point should trigger a precision check before taking a square root, rather than being described as negative risk.

A return in percent points is 100 times a decimal return; its variance and covariance scale by 10000. Correlation and beta remain unchanged if both relevant series are scaled consistently. Use a price-plus-dividend return when a dividend is present. Arithmetic means describe the one-period expected return; geometric accumulation is a different calculation. Source: 2025 review pp. 19–25; 2026 formula reference section 3. Q16–Q20 give worked examples.

## 12.5 Risk decomposition and regression

In R_i=a+beta_i R_M+epsilon_i with residual uncorrelated with the market:

\[
\beta_i=\frac{\operatorname{Cov}(R_i,R_M)}{\sigma_M^2},\qquad
\sigma_i^2=\beta_i^2\sigma_M^2+\sigma_\epsilon^2.
\]

Systematic variance is also rho_iM^2*sigma_i^2. Systematic standard deviation is abs(beta_i)*sigma_M=abs(rho_iM)*sigma_i; residual standard deviation is sigma_i*sqrt(1-rho_iM^2). These standard deviations do not add; their squares do. A beta-zero asset can have residual risk. A beta-matched combination of market and cash matches systematic exposure; it does not replicate residual payoffs state by state.

For an excess-return regression R_i-rf=alpha+beta*(R_M-rf)+epsilon, the intercept has the CAPM benchmark-alpha interpretation under the stated specification. A raw-return regression's intercept a generally differs: with a constant rf, alpha=a-(1-beta)*rf. The forecast-return gap from the SML is an ex-ante comparison, whereas a realized return surprise may be noise. Source: 2026 Neoclassics pp. 39–47; 2025 review pp. 22–25. Q21–Q25 provide practice.

## 12.6 Exchange rates and parity relations

Always define the quote in words. Let S be **domestic currency units per one foreign currency unit**. A rise in S means the foreign currency appreciates and the domestic currency depreciates.

For the same basket costing P_D domestically and P_F abroad, absolute purchasing power parity gives S_PPP=P_D/P_F. Convert the domestic basket to foreign currency by dividing by observed S. A basket's foreign-price premium relative to the foreign basket is (P_D/S)/P_F-1. Statements about an overvalued currency must identify the currency, quote direction and benchmark: if S is below S_PPP, the domestic currency buys more foreign currency than the simple basket relation implies.

Relative PPP gives S_1/S_0=(1+pi_D)/(1+pi_F), approximately the domestic minus foreign inflation differential. It is a model for price-level consistency, not guaranteed short-run convergence. Services, transport, tax, trade barriers and product differences can sustain a Big Mac price gap; goods are not instantly replicable tradable securities.

Covered interest parity for maturity T with annual effective rates and frictionless financing is:

\[
F_{0,T}=S_0\frac{(1+r_D)^T}{(1+r_F)^T}.
\]

Derive it by comparing domestic investment with conversion, foreign investment and a forward sale of the foreign proceeds. A dollar liability must be hedged by securing dollar purchases; whether that is called a long or short FX quote depends on the currency pair convention. For a future borrowing-rate exposure, an FRA hedge must pay when borrowing rates rise; define payer/receiver direction rather than relying on ambiguous labels. The package requires the economic cash-flow logic, not an advanced FRA settlement model.

The Fisher relation links nominal and real rates with expected inflation: 1+i=(1+r_real)*(1+pi_expected), approximately i=r_real+pi_expected. International Fisher and uncovered-parity arguments add assumptions about expected currency changes, real rates and risk. Unbiased forward theory asserts an expectations relation such as E[S_T]=F under suitable assumptions; covered parity alone cannot prove it because a forward hedge and an uncertain future spot rate are different objects. Source: 2026 Derivatives pp. 8–11, 20–23. Q33–Q34 fix quote direction with numbers.

## 12.7 Complete behavioral glossary and contrasts

These entries cover the full decision-process list, not just the biases frequently selected in short practice sets. More than one mechanism may explain a case; require evidence from the student's explanation. Source: 2026 Behavioral pp. 5–21, 42–52; 2025 Key Terms pp. 3–4.

| Mechanism | Meaning and a finance application |
|---|---|
| Attention bias / inattentional blindness | Focusing on selected information hides another relevant fact. Change blindness is failing to notice a change; they are related but not identical. |
| Confirmation bias | Seek or interpret evidence to fit a favored stock thesis. |
| Selective perception based on experience | Past experience shapes what an analyst notices or how ambiguous information is interpreted. |
| Availability / salience | A memorable recent default dominates the estimated frequency despite broader data. |
| Representativeness | Infer probabilities from resemblance to a stereotype, neglecting base rates; extrapolate a short winning streak. The probability of A AND B cannot exceed P(A). |
| Conservatism | Update too little after informative news. In the standard informed-host Monty Hall game, switching wins with probability 2/3; the reveal protocol matters. |
| Herding | Follow other investors rather than independent information; common reactions can also have rational shared causes. |
| Anchoring | Stay too close to an initial number, such as a purchase price, despite its irrelevance to future value. |
| Framing | Equivalent presentations, such as gain versus loss descriptions, alter choices. |
| Probability matching | Randomize guesses according to outcome frequencies even when always choosing the more likely independent outcome has higher expected success. |
| Overconfidence | Overestimate skill or precision; stated 90% intervals cover materially fewer outcomes. |
| Optimism | Expectations are directionally too favorable, rather than merely too precise. |
| Belief perseverance | Retain an initial view after its evidential basis is discredited. |
| Mental accounting | Treat economically fungible money differently depending on labels or separate mental budgets. Real constraints can justify separate accounts. |
| Disposition effect | Sell winners and retain losers relative to a reference point, often to avoid realizing a loss; distinguish tax incentives. |
| House-money effect | Take greater risk with prior gains treated as less valuable than earned wealth. |
| Home bias | Prefer domestic assets; assess effects on diversification and possible information/cost/liability explanations. |
| Endowment effect | Value an asset more because it is already owned. |
| Sunk-cost fallacy | Continue investing because of irrecoverable past costs rather than future incremental value. |
| Fairness | Care about an allocation's fairness, potentially rejecting an unequal positive offer. A social preference is not automatically a computation error. |
| Hindsight bias | After observing an outcome, believe it was foreseeable or previously predicted. |
| Regret aversion | Avoid decisions expected to cause future regret; can encourage inaction or imitation. |
| Myopic loss aversion | Loss sensitivity combined with frequent short-horizon evaluation distorts long-horizon risk choices. |
| Automation bias | Trust an algorithm despite relevant contradictory evidence. |
| Algorithm aversion | Reject useful algorithms too strongly after seeing errors. |
| Data anchoring / confirmation in model tuning | Historical patterns and a favored thesis influence training data selection or model choice. |
| Social amplification / echo chambers | Repeated selective narratives reinforce attention, herding and overconfidence. |

For a p=0.7 independent red/blue game with equal rewards, probability matching succeeds with 0.7^2+0.3^2=0.58; always red succeeds with 0.7. This conclusion relies on fixed probabilities, independence and the stated payoff objective; it is not a statement that financial diversification is wrong.

Prospect theory evaluates changes from a reference point rather than final wealth alone. Its typical value curve is concave over gains, convex over losses and steeper for losses; decision weights need not equal objective probabilities. A change in framing can change the reference point. Risk seeking in losses is not a universal prediction independent of probabilities and stakes. Structured-product design can map desired floors and caps into option payoffs, but a questionnaire does not prove an allocation is uniquely optimal.

## 12.8 Anomalies, historical cases and critical interpretation

The lecture illustrates seasonality (Sell in May and weekday patterns), descriptive market statistics, a size-effect illustration in the SML discussion, and Tesla/GameStop narratives linking attention and social dynamics to price movements. These are historical teaching cases. The learning objective is to explain competing mechanisms, benchmark an apparent anomaly and distinguish a disciplined process from demonstrated predictive power. A viral story or price chart alone does not identify a causal behavioral effect.

Ask what information was known at the time, whether the benchmark compensates the relevant risk, whether transaction costs erase a result, and whether out-of-sample evidence survives repeated strategy selection. A rule may constrain impulsive behavior without systematically forecasting returns. No present-day stock recommendation follows. Source: 2026 Behavioral pp. 23–32; Neoclassics p. 46.

## 12.9 Credit, crypto and replication cautions

Credit ratings, sovereign-debt charts and distance-to-default measures are indicators, not guaranteed forecasts. A CDS premium compensates multiple risks and is not directly a default probability. A default-protection contract shifts specified credit-event risk and introduces contractual/counterparty terms. Price, yield and credit spread must be separated from the risk-free curve.

A hash is not a digital signature, encryption or a guarantee of truthful external data. Public transaction histories generally provide pseudonymity, not assured anonymity. A nonce is an input varied during PoW search; the target determines valid hashes, and extra binary versus hexadecimal zeros have different difficulty multipliers. Bitcoin halvings reduce new subsidy, not balances. Old Ether issuance statements, coin counts and energy screenshots must be treated as historical illustrations. Explain PoH as sequential verifiable ordering alongside Solana consensus, not an autonomous substitute for all validators. Smart contracts use execution resources (gas); code, keys and external information can still fail. NFT control alone grants neither copyright nor a guaranteed economic claim.

Law of one price equates **identical state cash flows**, subject to compatible risk and trading assumptions. It is stronger than matching expected returns or betas. A claim of negative call value from parity indicates inconsistent quotes/assumptions; do not teach it as a valid option price. Source: 2026 Bonds pp. 3, 13–21; Crypto pp. 3–37; Derivatives pp. 17, 26–27.
