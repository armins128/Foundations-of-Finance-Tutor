# Foundations of Finance — learning edition

Self-contained course summary. Built 23 November 2026 from the supplied course context, with complete-course extensions from the 2025–2027 archive audit. The chapter text is explanatory material, not a future exam announcement. Use scope.md and learning-protocol.md for tutoring behavior; solution examples are not learner evidence.

# 0. Notation and foundations

## 0.1 Core notation

| Symbol | Meaning |
|---|---|
| \(t=0,1,\ldots,T\) | Time index; \(t=0\) is today |
| \(CF_t\) | Cash flow at time \(t\) |
| \(i\), \(r\) | Interest rate, discount rate, yield, or risk-free rate, depending on context |
| \(PV\) | Present value |
| \(FV\) | Future value |
| \(\mu\) | Expected value or expected return |
| \(\sigma^2\) | Variance |
| \(\sigma\) | Standard deviation or volatility |
| \(\operatorname{Cov}(R_i,R_j)\) | Covariance between returns \(R_i\) and \(R_j\) |
| \(\rho_{ij}\) | Correlation between returns \(R_i\) and \(R_j\) |
| \(w_i\) | Portfolio weight of asset \(i\) |
| \(S_0\), \(S_T\) | Underlying asset price today and at maturity |
| \(F_0\) | Forward or futures delivery price agreed today |
| \(X\) | Option exercise price or strike price |
| \(\beta_i\) | Beta of asset \(i\) |

## 0.2 Rates and time must be consistent

A rate must correspond to the length of one model period. If cash flows are annual, an annual rate can be used directly. If periods differ, rate and time units must first be made consistent. The formulas below use discrete compounding unless stated otherwise.

A percentage rate must be converted into decimal form for calculations. For example, \(5\%=0.05\).

## 0.3 Cash-flow timelines

Before valuing a project or security, it is useful to draw a timeline:

```text
t = 0        t = 1        t = 2                    t = T
 CF_0         CF_1         CF_2                     CF_T
```

Cash flows can only be added or compared directly when they refer to the same point in time. Discounting moves future cash flows to the present; compounding moves current cash flows into the future.

---


# 1. Value

## 1.1 Present value, future value, discounting, and compounding

One monetary unit today can earn interest and become more than one monetary unit in the future. Conversely, a future payment is worth less today when the discount rate is positive.

For a present value \(PV_0\), interest rate \(i\), and \(T\) periods:

$$
FV_T = PV_0(1+i)^T.
$$

The **compound factor** is

$$
(1+i)^T.
$$

Solving for present value gives

$$
PV_0 = \frac{FV_T}{(1+i)^T}.
$$

The **discount factor** is

$$
\frac{1}{(1+i)^T}.
$$

Important comparative statics:

- For a positive future cash flow, a higher discount rate produces a lower present value.
- For a positive present amount, a higher interest rate produces a higher future value.
- A cash flow further in the future is discounted more heavily when the rate is positive.
- At a zero rate, present value and future value are equal.

## 1.2 Net present value

The net present value of a stream of cash flows is

$$
NPV_0 = \sum_{t=0}^{T}\frac{CF_t}{(1+i)^t}.
$$

Because \((1+i)^0=1\), the cash flow at \(t=0\) is included without discounting. If an initial investment \(I_0\) is paid today, then \(CF_0=-I_0\), so

$$
NPV_0=-I_0+\sum_{t=1}^{T}\frac{CF_t}{(1+i)^t}.
$$

Decision rule for an independent investment:

- \(NPV>0\): accept; the investment creates value relative to the required return.
- \(NPV=0\): the investor is indifferent at the assumed discount rate.
- \(NPV<0\): reject; the investment destroys value relative to the required return.

The NPV is measured in currency units at \(t=0\). It is not a return percentage.

### Reservation price

The reservation price is the maximum price a buyer can pay while achieving a target NPV of zero. Economically, it equals the present value of the future benefits when there are no other time-zero cash flows. More generally, set the full NPV equation equal to zero and solve for the unknown purchase price.

### Choosing a discount rate

The discount rate represents the opportunity cost of capital appropriate for the risk and timing of the cash flows. Using an inappropriate rate can reverse an investment decision. A risk-adjusted rate derived from CAPM is introduced later.

## 1.3 Annuities

An **ordinary annuity** consists of the same payment \(c\) at the end of each period from \(t=1\) through \(t=T\).

Its present value is

$$
PV=c\cdot AF(i,T),
$$

where the annuity factor is

$$
AF(i,T)=\frac{(1+i)^T-1}{i(1+i)^T}
=\frac{1-(1+i)^{-T}}{i}.
$$

Given a present value, the constant payment with the same present value is

$$
c=CRF(i,T)\cdot PV,
$$

where the capital recovery factor is

$$
CRF(i,T)=\frac{i(1+i)^T}{(1+i)^T-1}.
$$

The two factors are reciprocals:

$$
AF(i,T)=\frac{1}{CRF(i,T)}.
$$

Interpretation:

- \(AF\) converts a constant future payment into a present value.
- \(CRF\) converts a present value into an equivalent constant end-of-period payment.
- This conversion is useful when alternatives have different cash-flow patterns or lives and must be expressed as comparable constant annual amounts.

The future value of a constant end-of-period payment \(c\) is

$$
FV_T=c\cdot FVAF(i,T),
$$

with

$$
FVAF(i,T)=\frac{(1+i)^T-1}{i}.
$$

This factor compounds each payment to time \(T\). The last payment occurs at \(T\) and therefore earns no additional interest.

## 1.4 Perpetuities

A **perpetuity** pays the same amount \(C\) forever, starting one period from today. Its present value is

$$
PV=\frac{C}{r},
$$

for \(r>0\).

A **growing perpetuity** has a first payment \(C_1\) at \(t=1\), followed by payments that grow at constant rate \(g\). Its present value is

$$
PV=\frac{C_1}{r-g},
$$

provided

$$
r>g.
$$

Timing is crucial: the numerator is the payment one period from now, not a payment today. If a current payment \(C_0\) is given, then \(C_1=C_0(1+g)\).

The condition \(r>g\) ensures that the discounted infinite series converges. As \(g\) approaches \(r\) from below, the value becomes very large.

## 1.5 Internal rate of return

The internal rate of return is the discount rate that makes the project's NPV equal to zero:

$$
\sum_{t=0}^{T}\frac{CF_t}{(1+IRR)^t}=0.
$$

For a conventional project with an initial outflow followed by inflows, the common comparison is:

- Accept if \(IRR\) exceeds the required return.
- Be indifferent if \(IRR\) equals the required return.
- Reject if \(IRR\) is below the required return.

NPV and IRR answer related but different questions. NPV measures value creation in currency units at a specified opportunity cost of capital. IRR reports a break-even discount rate implied by the cash flows.

Important limitation: if cash flows change sign more than once, the NPV equation may have multiple IRRs or no economically useful IRR. In such cases, the NPV rule at the appropriate discount rate is the more reliable decision criterion.

## 1.6 Frequent valuation errors

- Confusing \(PV\) with \(NPV\): \(PV\) values future cash flows; \(NPV\) also includes the time-zero investment.
- Discounting the initial investment even though it is already at \(t=0\).
- Using \(C_0\) rather than \(C_1\) in a growing perpetuity.
- Applying a perpetuity formula to a finite payment stream.
- Treating \(AF\) and \(CRF\) as the same factor rather than reciprocals.
- Rounding discount factors or intermediate present values too early.
- Applying a simple IRR decision rule when cash flows have multiple sign changes.

---


# 2. Bonds

## 2.1 Bond cash flows and pricing

A bond is valued by discounting all promised cash flows at the relevant yield. The general formula is

$$
B=\sum_{t=1}^{T}\frac{CF(t)}{(1+i)^t}.
$$

For a coupon bond with face value \(N\), annual coupon \(C\), maturity \(T\), and redemption of face value at maturity:

$$
B=\sum_{t=1}^{T}\frac{C}{(1+i)^t}+\frac{N}{(1+i)^T}.
$$

The final period contains both the last coupon and repayment of the face value.

For a zero-coupon bond:

$$
B=\frac{N}{(1+i)^T}.
$$

If the price, face value, and maturity of a zero-coupon bond are known, its yield can be obtained from

$$
i=\left(\frac{N}{B}\right)^{1/T}-1.
$$

This is an algebraic rearrangement of the zero-bond pricing formula.

## 2.2 Coupon rate, yield, and price relative to par

The coupon rate determines the contractual coupon relative to face value. The yield is the market discount rate used to value the promised cash flows. They are not generally equal.

- Coupon rate \(>\) yield: the bond trades above face value, at a **premium**.
- Coupon rate \(<\) yield: the bond trades below face value, at a **discount**.
- Coupon rate \(=\) yield: the bond trades at **par**.

The logic is that existing coupons are attractive when they exceed the market-required yield and unattractive when they fall below it.

Bond prices and yields move in opposite directions. When the yield rises, the present value of the fixed promised cash flows falls.

## 2.3 Macaulay duration

Macaulay duration is the present-value-weighted average time at which the bond's cash flows are received:

$$
D_{Mac}=\frac{\sum_{t=1}^{T}\frac{CF(t)\,t}{(1+i)^t}}{B}.
$$

Each cash flow's weight equals its present value divided by the bond price. These weights sum to one, making duration a weighted average measured in periods.

For a zero-coupon bond, the only cash flow occurs at maturity, so

$$
D_{Mac}=T.
$$

For a coupon bond, some cash is received before maturity, so Macaulay duration is generally below maturity.

An equivalent derivative representation is

$$
\frac{dB}{dR}=\sum_{t=1}^{T}\frac{-t\,CF(t)}{(1+R)^{t+1}},
$$

and

$$
D_{Mac}=-\frac{dB}{dR}\frac{1}{B}(1+R).
$$

This representation connects the timing interpretation of duration with price sensitivity to changes in yield.

## 2.4 Modified duration and price sensitivity

Modified duration is

$$
D_{Mod}=\frac{D_{Mac}}{1+i}.
$$

It approximates the percentage price response to a small change in yield:

$$
\frac{\Delta B}{B}\approx-D_{Mod}\Delta i.
$$

Equivalently,

$$
\Delta B\approx-BD_{Mod}\Delta i.
$$

An approximate new price can therefore be calculated as

$$
B_{new}\approx B_{old}+\Delta B
=B_{old}(1-D_{Mod}\Delta i).
$$

The yield change must be entered as a decimal. For example, 50 basis points equal \(0.0050\).

The minus sign captures the inverse relationship between bond prices and yields:

- if \(\Delta i>0\), the approximate price change is negative;
- if \(\Delta i<0\), the approximate price change is positive.

## 2.5 Convexity and the limitation of duration

The true bond price-yield relationship is curved rather than linear. Duration uses the tangent to this curve and therefore provides a linear approximation.

For a standard bond with positive convexity, the curved price-yield relation lies above its tangent. As a result, a duration-only estimate typically **underestimates the actual bond price** after either an upward or downward yield movement. Equivalently:

- when yields rise, duration tends to overstate the absolute price loss and underestimate the new price;
- when yields fall, duration tends to understate the price gain and underestimate the new price.

The approximation is usually more accurate for small yield changes and less accurate for large changes.

## 2.6 Bond portfolio duration

The duration of a bond portfolio is the value-weighted average duration of its components:

$$
D_P=\sum_{j=1}^{n}w_jD_j,
$$

with

$$
\sum_{j=1}^{n}w_j=1.
$$

The weights are proportions of the portfolio's current market value, not proportions of face value or numbers of bonds.

## 2.7 Immunization

Immunization aims to protect the ability of an asset portfolio to meet a future liability when interest rates change.

For a certain liability \(L_T\) paid at time \(T\):

$$
PV_L=\frac{L_T}{(1+i)^T}.
$$

Because this is a single payment, its duration is

$$
D_{liability}=T.
$$

The basic immunization conditions are

$$
PV_{assets}=PV_{liability}
$$

and

$$
D_P=D_{liability}.
$$

The first condition matches values today; the second matches first-order interest-rate sensitivity. Duration matching is a local protection against relatively small rate changes, not a universal guarantee. As time passes or yields change, portfolio values and durations change, so rebalancing may be necessary.

## 2.8 Frequent bond errors

- Forgetting repayment of face value in the final coupon-bond cash flow.
- Discounting every cash flow for the same number of periods.
- Confusing coupon rate with yield.
- Reversing the price-yield relationship.
- Using Macaulay duration directly in the price-change formula instead of modified duration.
- Treating a basis-point change as a percentage-point or decimal change incorrectly.
- Using face-value weights instead of market-value weights for portfolio duration.
- Assuming a duration approximation is exact.
- Matching duration but not present value when immunizing a liability.

## 2.9 Credit risk, ratings, and CDS spreads

**Credit risk** is the risk that a borrower does not make promised payments in full and on time. An important component is the probability of default. Greater perceived credit risk generally implies:

- a higher yield demanded by investors;
- a lower bond price for given promised cash flows;
- a worse credit assessment, all else equal.

Credit ratings are assessments issued periodically by rating agencies. They summarize creditworthiness in rating categories, but they are not guarantees and may adjust only after new information has accumulated.

A **credit default swap (CDS)** is a contract that transfers specified credit risk from a protection buyer to a protection seller. The buyer pays a periodic CDS premium or **spread** and receives protection if a contractually defined credit event occurs. The seller receives the spread and bears the obligation specified by the contract after such an event.

The CDS spread is therefore a market-based indicator of perceived credit risk:

- a wider CDS spread generally indicates that the market demands more compensation for bearing the reference entity's credit risk;
- a narrower CDS spread generally indicates lower market-perceived credit risk;
- an unchanged credit rating does not imply an unchanged CDS spread because market prices can react continuously and faster than ratings.

A CDS spread is not itself a default probability, and its interpretation can also be affected by expected recovery, liquidity, risk premia, and market conditions. The core course intuition is directional: higher perceived credit risk is associated with wider spreads, higher required bond yields, and lower bond prices.

---


# 3. Portfolio theory

## 3.1 Return, expected return, variance, and volatility

For a return series \(R_1,\ldots,R_n\), the arithmetic mean is

$$
\mu=\frac{1}{n}\sum_{t=1}^{n}R_t.
$$

Under the population convention used in this course context, variance is

$$
\sigma^2=\frac{1}{n}\sum_{t=1}^{n}(R_t-\mu)^2,
$$

and volatility is

$$
\sigma=\sqrt{\sigma^2}.
$$

Variance is measured in squared return units. Volatility is measured in the same units as the original returns and is therefore easier to interpret.

Calculation sequence:

1. Calculate the mean return.
2. Calculate each deviation \(R_t-\mu\).
3. Square each deviation.
4. Sum the squared deviations.
5. Divide by \(n\).
6. Take the square root to obtain volatility.

## 3.2 Covariance and correlation

Covariance measures whether two assets tend to move together:

$$
\operatorname{Cov}(R_i,R_j)
=\frac{1}{n}\sum_{t=1}^{n}(R_{i,t}-\mu_i)(R_{j,t}-\mu_j).
$$

- Positive covariance: returns tend to be above or below their means at the same time.
- Negative covariance: one return tends to be above its mean when the other is below its mean.
- Zero covariance: there is no linear co-movement in the observations.

Correlation standardizes covariance:

$$
\rho_{ij}=\operatorname{Corr}(R_i,R_j)
=\frac{\operatorname{Cov}(R_i,R_j)}{\sigma_i\sigma_j}.
$$

Correlation is dimensionless and lies between \(-1\) and \(+1\). Covariance depends on the measurement scale; correlation does not.

The sign of covariance and correlation is the same when both volatilities are positive. A correlation cannot be computed in the usual way if either asset has zero volatility because the denominator is then zero.

## 3.3 Portfolio weights and expected return

For a fully invested portfolio,

$$
\sum_{i=1}^{n}w_i=1.
$$

Unless constraints are imposed, a weight can exceed one or be negative. A negative weight represents a short position; weights above one generally imply leverage financed by negative weights elsewhere.

Portfolio return is the weighted sum of individual asset returns, so expected portfolio return is

$$
\mu_P
=\mathbb{E}\left[\sum_{i=1}^{n}w_i\widetilde R_i\right]
=\sum_{i=1}^{n}w_i\mu_i.
$$

For two assets:

$$
\mu_P=w_1\mu_1+w_2\mu_2,
\qquad w_1+w_2=1.
$$

Expected return is linear in the weights. Risk is not generally linear because assets co-move.

## 3.4 Portfolio variance and volatility

For \(n\) assets:

$$
\sigma_P^2
=\sum_{i=1}^{n}\sum_{j=1}^{n}
w_iw_j\sigma_i\sigma_j\rho_{ij}.
$$

For two assets:

$$
\sigma_P^2
=w_1^2\sigma_1^2+w_2^2\sigma_2^2
+2w_1w_2\operatorname{Cov}(R_1,R_2),
$$

or equivalently,

$$
\sigma_P^2
=w_1^2\sigma_1^2+w_2^2\sigma_2^2
+2w_1w_2\sigma_1\sigma_2\rho_{12}.
$$

Portfolio volatility is

$$
\sigma_P=\sqrt{\sigma_P^2}.
$$

The cross term is essential. Simply taking a weighted average of individual volatilities generally gives the wrong portfolio risk.

## 3.5 Diversification

Diversification works because portfolio risk depends not only on individual volatilities but also on co-movement.

- If \(\rho=+1\), the two assets move perfectly together and there is no diversification benefit from combining them.
- If \(\rho<+1\), combining the assets can reduce risk relative to a simple weighted average of their volatilities.
- If \(\rho=-1\), suitable weights may eliminate volatility completely.

Negative covariance is particularly valuable for risk reduction. In the unconstrained two-asset minimum-variance problem, strictly negative covariance implies positive minimum-variance weights for both assets: each numerator in the weight formulas is a positive variance minus a negative covariance. Negative covariance alone, however, does not guarantee zero portfolio volatility; perfect elimination requires the stronger condition of perfect negative correlation together with suitable weights.

## 3.6 Minimum-variance portfolio with two risky assets

The weight of asset 1 in the unconstrained two-asset minimum-variance portfolio is

$$
w_1^{MVP}
=\frac{\sigma_2^2-\operatorname{Cov}(R_1,R_2)}
{\sigma_1^2+\sigma_2^2-2\operatorname{Cov}(R_1,R_2)}.
$$

The second weight is

$$
w_2^{MVP}=1-w_1^{MVP}.
$$

These weights minimize portfolio variance subject to the budget constraint \(w_1+w_2=1\). They do not maximize expected return and do not depend on expected returns.

Because the formula is unconstrained, it can in general produce negative weights or weights above one. If short selling is prohibited, a constrained solution may instead lie at a boundary.

After finding the weights, use the usual portfolio-return and portfolio-variance formulas to calculate the MVP's expected return and volatility.

## 3.7 Efficient frontier

The feasible set contains all risk-return combinations obtainable from the available assets and allowed portfolio weights. The **minimum-variance frontier** identifies portfolios with the lowest variance for different expected returns. The **efficient frontier** is the upper part of that frontier: for a given risk, an efficient portfolio offers the highest expected return; for a given expected return, it offers the lowest risk.

A portfolio is inefficient if another feasible portfolio offers a higher expected return for the same or lower risk, or lower risk for the same or higher expected return.

## 3.8 Risk-free asset and two-fund separation

Consider a portfolio combining the market portfolio \(M\) with a risk-free asset earning \(r\). If \(w_M\) is invested in the market and \(1-w_M\) in the risk-free asset, then

$$
\mu=w_M\mu_M+(1-w_M)r
=r+(\mu_M-r)w_M.
$$

For a non-negative market weight, volatility is

$$
\sigma=w_M\sigma_M,
$$

so

$$
w_M=\frac{\sigma}{\sigma_M}.
$$

More generally, volatility is \(|w_M|\sigma_M\), because volatility cannot be negative.

Interpretation of weights:

- \(0<w_M<1\): some wealth is invested risk-free.
- \(w_M=1\): all wealth is invested in the market portfolio.
- \(w_M>1\): the investor borrows at the risk-free rate to leverage the market investment.
- \(w_M<0\): the market is short-sold and more than 100% is invested in the risk-free asset.

Two-fund separation means that investors can choose risk exposure by combining the same risky fund with the risk-free asset rather than selecting different collections of individual risky securities.

## 3.9 Frequent portfolio-theory errors

- Dividing by \(n-1\) when the course calculation requires division by \(n\).
- Forgetting to take the square root after calculating variance.
- Confusing covariance with correlation.
- Omitting the factor of two in the two-asset covariance term.
- Using a weighted average of volatilities as portfolio volatility.
- Forgetting that portfolio weights must sum to one.
- Assuming that all weights must lie between zero and one in an unconstrained problem.
- Assuming negative covariance automatically produces zero portfolio risk.
- Using expected returns in the formula for the minimum-variance weights.

---


# 4. Capital Asset Pricing Model

## 4.1 Total, systematic, and unsystematic risk

Total return risk can be understood as having two components:

- **Systematic risk** is exposure to broad market movements. It cannot be eliminated by holding a well-diversified portfolio.
- **Unsystematic**, **idiosyncratic**, or firm-specific risk can be reduced through diversification.

CAPM predicts that only systematic risk earns a risk premium because investors can diversify away unsystematic risk. Total volatility alone therefore does not determine an asset's required expected return.

## 4.2 Beta

Beta measures an asset's sensitivity to market returns:

$$
\beta_i=\frac{\operatorname{Cov}(R_i,R_M)}{\operatorname{Var}(R_M)}.
$$

Using correlation and volatility, the same beta is

$$
\beta_i=\rho_{iM}\frac{\sigma_i}{\sigma_M}.
$$

Interpretation:

- \(\beta_i=1\): the asset has the same systematic exposure as the market.
- \(\beta_i>1\): the asset has more market sensitivity than the market portfolio.
- \(0<\beta_i<1\): the asset moves with the market but less strongly.
- \(\beta_i=0\): no linear market exposure.
- \(\beta_i<0\): the asset tends to move against the market.

The risk-free asset has beta zero; the market portfolio has beta one.

Two assets can have the same total volatility but different betas because beta also depends on correlation with the market. With equal total volatility, the asset with the larger absolute market correlation has the larger absolute beta. This illustrates why total risk and systematic risk are distinct.

## 4.3 Capital Market Line

The Capital Market Line describes efficient portfolios formed from the risk-free asset and the market portfolio:

$$
\mu=r+\frac{\mu_M-r}{\sigma_M}\sigma.
$$

Its slope is the market price of risk:

$$
MPR=\frac{\mu_M-r}{\sigma_M}.
$$

The MPR is the market portfolio's expected excess return per unit of total volatility.

The CML applies to efficient combinations of the market portfolio and the risk-free asset. Its horizontal axis is total risk, measured by \(\sigma\).

## 4.4 Security Market Line and CAPM pricing equation

CAPM states

$$
\mu_i=r+(\mu_M-r)\beta_i.
$$

Equivalently,

$$
\mathbb{E}[\widetilde R_i]
=r+(\mu_M-r)\beta_i.
$$

The Security Market Line plots expected return against beta. Its intercept is the risk-free rate and its slope is the market risk premium \(\mu_M-r\).

Unlike the CML, the SML applies to individual assets and portfolios, whether efficient or inefficient. Its risk measure is beta rather than total volatility.

### CML versus SML

| Feature | CML | SML |
|---|---|---|
| Risk measure | Total volatility \(\sigma\) | Systematic risk \(\beta\) |
| Applies to | Efficient market/risk-free portfolios | Individual assets and portfolios |
| Slope | \((\mu_M-r)/\sigma_M\) | \(\mu_M-r\) |

## 4.5 Alpha and mispricing

The CAPM-required expected return is

$$
\mu_i^{CAPM}=r+(\mu_M-r)\beta_i.
$$

Alpha is the difference between the asset's expected return and this benchmark:

$$
\alpha_i=\mu_i-\mu_i^{CAPM}.
$$

Interpretation:

- \(\alpha_i>0\): the asset lies above the SML and tends to be described as undervalued relative to CAPM.
- \(\alpha_i<0\): the asset lies below the SML and tends to be described as overvalued relative to CAPM.
- \(\alpha_i=0\): the asset lies on the SML.

This interpretation is conditional on CAPM being the appropriate model and on the expected-return and beta estimates being correct.

If alpha, expected return, the risk-free rate, and market expected return are known, an implied beta can be obtained by rearranging

$$
\alpha_i=\mu_i-r-(\mu_M-r)\beta_i
$$

to give

$$
\beta_i=\frac{\mu_i-r-\alpha_i}{\mu_M-r},
$$

provided \(\mu_M\ne r\).

## 4.6 Replicating systematic risk

Consider a portfolio consisting of the market portfolio and the risk-free asset. Portfolio beta is the weighted average of component betas:

$$
\beta_{repl}=w_M\cdot 1+(1-w_M)\cdot 0=w_M.
$$

To replicate the systematic risk of asset \(i\), choose

$$
w_M=\beta_i,
\qquad
w_r=1-\beta_i.
$$

The expected return of this replicating portfolio is

$$
\mu_{repl}=w_M\mu_M+(1-w_M)r.
$$

Weight interpretation matters:

- If \(\beta_i>1\), invest more than 100% in the market and borrow at the risk-free rate.
- If \(0<\beta_i<1\), split wealth between the market and the risk-free asset.
- If \(\beta_i<0\), short the market and invest more than 100% in the risk-free asset.

A portfolio can also combine other risky positions with market and risk-free positions. To make its beta equal to a target value, use the fact that portfolio beta is the weighted sum of component betas together with the budget constraint that weights sum to one.

## 4.7 Risk-adjusted discount rate and cost of capital

CAPM provides a risk-adjusted required return:

$$
\text{cost of capital}=r+(\mu_M-r)\beta_i.
$$

For a one-period expected future price, the current value is

$$
P_i=\frac{\mathbb{E}[\widetilde P_i]}
{1+r+(\mu_M-r)\beta_i}.
$$

A higher beta raises the required return when the market risk premium is positive and therefore lowers the present value of a given expected future payoff.

## 4.8 Frequent CAPM errors

- Using total volatility where beta is required.
- Forgetting that beta divides by market variance, not market volatility.
- Confusing the market risk premium \(\mu_M-r\) with the market expected return \(\mu_M\).
- Confusing CML and SML.
- Interpreting alpha without first calculating the CAPM benchmark return.
- Assuming that equal total volatility implies equal systematic risk.
- Constructing a beta-matched portfolio without enforcing that weights sum to one.
- Mishandling negative beta: matching it requires a short market position and a risk-free weight above one.
- Using a risky discount rate for a risk-free cash flow or a risk-free rate for a risky cash flow without justification.

---


# 5. Derivatives

## 5.1 Payoff, profit, and position direction

A derivative's **payoff** is the cash flow generated by the contract at maturity. **Profit** also accounts for the price or premium paid or received initially and, where relevant, its financing over time. These terms should not be used interchangeably.

A **long** position benefits when the contract's payoff rises. A **short** position has the negative payoff of the corresponding long position.

## 5.2 Forward and futures payoffs

A forward or futures contract fixes a delivery price \(F_0\) today for a transaction at maturity.

Long forward payoff:

$$
\Pi_{long\ forward}=S_T-F_0.
$$

Short forward payoff:

$$
\Pi_{short\ forward}=F_0-S_T.
$$

The long benefits when the terminal spot price exceeds the agreed delivery price; the short benefits when it is lower.

## 5.3 Fair forward or futures price without payouts

For an underlying asset that makes no payouts and can be stored or held without other costs, the no-arbitrage delivery price with discrete compounding is

$$
F_0=S_0(1+r)^T.
$$

For one period:

$$
F_0=S_0(1+r).
$$

The fair price equals the future value of buying the underlying today. This is a cost-of-carry relation: the holder gives up the interest that could have been earned on the money used to purchase the asset.

## 5.4 Cash-and-carry and reverse cash-and-carry

If the observed futures price is above the no-arbitrage price,

$$
F^{obs}>S_0(1+r)^T,
$$

a typical cash-and-carry strategy is:

1. borrow \(S_0\) today;
2. buy the underlying asset;
3. short the futures contract;
4. deliver the asset at maturity for \(F^{obs}\);
5. repay \(S_0(1+r)^T\).

The maturity profit per unit, absent transaction costs, is

$$
\pi=F^{obs}-S_0(1+r)^T>0.
$$

If the observed futures price is below the fair price,

$$
F^{obs}<S_0(1+r)^T,
$$

a typical reverse cash-and-carry strategy is:

1. short-sell the underlying asset;
2. invest the proceeds at the risk-free rate;
3. take a long futures position;
4. acquire the asset through the futures contract at maturity;
5. return the asset to close the short sale.

No-arbitrage arguments require that all legs be stated at each date. If transaction or financing costs are introduced, place each cost on the timeline and compound or discount it consistently. An apparent price difference is only an arbitrage if net profit remains non-negative in every relevant state and positive in at least one state, with no net initial investment or risk.

## 5.5 Option payoffs

A call gives its holder the right, but not the obligation, to buy the underlying for strike \(X\). A put gives its holder the right, but not the obligation, to sell the underlying for \(X\).

Long call payoff:

$$
\Pi_{long\ call}=\max(S_T-X,0).
$$

Short call payoff:

$$
\Pi_{short\ call}=-\max(S_T-X,0).
$$

Long put payoff:

$$
\Pi_{long\ put}=\max(X-S_T,0).
$$

Short put payoff:

$$
\Pi_{short\ put}=-\max(X-S_T,0).
$$

At maturity:

- a call is exercised when \(S_T>X\);
- a put is exercised when \(S_T<X\);
- at \(S_T=X\), both have zero intrinsic payoff.

The payoff formulas do not subtract the option premium. To calculate profit, include the initial premium and, if all values are compared at maturity, its financing effect.

## 5.6 Put-call parity

For European options on the same non-dividend-paying stock, with the same strike and maturity, put-call parity is

$$
S_0+P_0=\frac{X}{(1+r)^T}+C_0.
$$

For one period:

$$
S+P=\frac{X}{1+r}+C.
$$

The left portfolio consists of one stock and one put. The right portfolio consists of one call and a risk-free investment that will grow to \(X\) at maturity.

Their terminal payoffs are identical:

| Terminal state | Stock + put | Call + risk-free payoff |
|---|---:|---:|
| \(S_T<X\) | \(S_T+(X-S_T)=X\) | \(0+X=X\) |
| \(S_T\ge X\) | \(S_T+0=S_T\) | \((S_T-X)+X=S_T\) |

Because the future payoffs match in every state, the two portfolios must have the same price today.

## 5.7 Law of one price and option replication

The **law of one price** says that portfolios with identical future cash flows must have the same price today. If they had different prices, an investor could buy the cheaper portfolio and sell the more expensive one, locking in a no-arbitrage profit.

Put-call parity is an application of the law of one price. It can be rearranged to solve for the value of any one component given the other three. A parity violation suggests buying the cheaper side and selling the more expensive side, provided the assumed trades are feasible and all relevant costs are included.

## 5.8 Additional forward and futures concepts

The same no-arbitrage logic extends beyond a non-paying stock:

- **FX forwards:** forward prices reflect the interest-rate differential between the two currencies.
- **Commodity futures:** financing and other costs of carry affect the futures price.
- **Forward rate agreements (FRAs):** these contracts can hedge exposure to future interest-rate changes.

The exact extended pricing formulas are outside this knowledge base. The key common principle is replication and no-arbitrage.

## 5.9 Building structured payoffs

A structured payoff is created by combining basic building blocks such as:

- the underlying asset;
- a risk-free borrowing or lending position;
- long or short calls;
- long or short puts;
- forwards or futures.

The terminal payoff of the complete structure is the sum of the terminal payoffs of all positions. The initial net cost is the sum of amounts paid minus amounts received at inception.

### A general construction method

For any strategy:

1. List every position, quantity, strike, maturity, and initial price.
2. Confirm that all option legs refer to the same underlying and, when a standard strategy is intended, the same maturity.
3. Divide the possible terminal stock prices at all distinct strike prices.
4. Write each leg's payoff separately in every region.
5. Add the leg payoffs to obtain the total terminal payoff.
6. Include initial premiums and other initial costs to obtain profit rather than payoff.
7. Solve for break-even prices by setting profit equal to zero in each relevant region.
8. Check extreme cases such as \(S_T=0\) and a very large \(S_T\).

Unless stated otherwise, the formulas below describe **terminal payoffs before initial premiums and financing costs**. Break-even formulas are stated using unfinanced total net premiums for simplicity. If all values are measured at maturity, initial net costs must be compounded consistently.

### Protective put

Position:

- long one share;
- long one put with strike \(K\).

Terminal payoff:

$$
S_T+\max(K-S_T,0)=\max(S_T,K).
$$

The put establishes a floor at \(K\) while retaining upside participation. The protection is not free: the investor pays the put premium \(P_0\). A protective put resembles portfolio insurance.

With initial stock price \(S_0\) and put premium \(P_0\), the simplified break-even price above the strike is

$$
S_T=S_0+P_0.
$$

Put-call parity shows that a protective put has the same payoff as a call plus a risk-free payment of \(K\) at maturity:

$$
S_0+P_0=C_0+PV(K).
$$

### Covered call

Position:

- long one share;
- short one call with strike \(K\).

Terminal payoff:

$$
S_T-\max(S_T-K,0)=\min(S_T,K).
$$

The call premium generates income and partially cushions losses, but upside is capped at \(K\). The downside from owning the stock remains substantial. A covered call is not a fully protected strategy.

### Collar

Position:

- long one share;
- long one put with lower strike \(K_L\);
- short one call with upper strike \(K_U\), where \(K_L<K_U\).

Terminal payoff:

$$
S_T+\max(K_L-S_T,0)-\max(S_T-K_U,0)
=
\begin{cases}
K_L, & S_T<K_L,\\
S_T, & K_L\le S_T\le K_U,\\
K_U, & S_T>K_U.
\end{cases}
$$

The put creates a floor and the short call creates a cap. The call premium helps finance the put. A **zero-cost collar** is structured so that the call premium received approximately equals the put premium paid; zero initial option cost does not mean zero economic opportunity cost because upside is surrendered.

### Long straddle

Position:

- long one call with strike \(K\);
- long one put with the same strike \(K\) and maturity.

Terminal payoff:

$$
\max(S_T-K,0)+\max(K-S_T,0)=|S_T-K|.
$$

The strategy benefits from a large price movement in either direction and loses when the terminal price stays near the strike. If total premiums are \(C_0+P_0\), the simplified break-even prices are

$$
K-(C_0+P_0)
\qquad\text{and}\qquad
K+(C_0+P_0).
$$

The long straddle is a view on large absolute movement, not specifically on rising or falling prices.

### Short straddle

The short straddle sells both the call and put at the same strike. Its payoff is the negative of the long-straddle payoff. It earns the largest profit when \(S_T=K\), but it can suffer large losses after a substantial move. The upside loss is theoretically unlimited because the short call is uncovered.

### Long strangle

Position:

- long a put with lower strike \(K_L\);
- long a call with upper strike \(K_U\), where \(K_L<K_U\).

Terminal payoff:

$$
\max(K_L-S_T,0)+\max(S_T-K_U,0).
$$

A strangle also benefits from large movements in either direction. Compared with a comparable straddle, it is commonly cheaper but requires a larger movement before either option becomes valuable. If total premiums equal \(P_L+C_U\), simplified break-even prices are

$$
K_L-(P_L+C_U)
\qquad\text{and}\qquad
K_U+(P_L+C_U).
$$

### Bull call spread

Position:

- long one call with lower strike \(K_L\);
- short one call with upper strike \(K_U\), where \(K_L<K_U\).

Terminal payoff:

$$
\max(S_T-K_L,0)-\max(S_T-K_U,0)
=
\begin{cases}
0, & S_T\le K_L,\\
S_T-K_L, & K_L<S_T<K_U,\\
K_U-K_L, & S_T\ge K_U.
\end{cases}
$$

This is a moderately bullish strategy. Both its maximum payoff and initial net premium are limited. The short higher-strike call gives up gains beyond \(K_U\) in exchange for reducing the strategy's cost.

### Bear put spread

Position:

- long one put with upper strike \(K_U\);
- short one put with lower strike \(K_L\), where \(K_L<K_U\).

Terminal payoff:

$$
\max(K_U-S_T,0)-\max(K_L-S_T,0)
=
\begin{cases}
K_U-K_L, & S_T\le K_L,\\
K_U-S_T, & K_L<S_T<K_U,\\
0, & S_T\ge K_U.
\end{cases}
$$

This is a moderately bearish strategy. The maximum payoff and maximum loss are both limited when the initial net premium is included.

Bull and bear spreads can also be constructed with puts or calls in equivalent ways. Put-call parity explains why different collections of instruments can generate the same terminal payoff.

### Long butterfly spread with calls

For strikes \(K_1<K_2<K_3\), typically with equal spacing, the position is:

- long one call at \(K_1\);
- short two calls at \(K_2\);
- long one call at \(K_3\).

Terminal payoff:

$$
\max(S_T-K_1,0)-2\max(S_T-K_2,0)+\max(S_T-K_3,0).
$$

With equally spaced strikes, the payoff is zero below \(K_1\) and above \(K_3\), and reaches its maximum at \(K_2\). A long butterfly expresses the view that the terminal price will be near the middle strike. Both gains and losses are limited.

### Capital-protected participation structure

A simple capital-protected structure combines:

- a risk-free investment that grows to the desired guaranteed amount at maturity;
- a long call that provides participation in upside above a strike.

The risk-free component creates the floor, while the option shapes the upside. Full protection is only as reliable as the risk-free or issuing component and the contractual terms. Increasing protection or participation generally requires giving up something elsewhere, such as paying more, lowering the protected amount, reducing the participation rate, or capping upside.

### Synthetic positions from put-call parity

Rearranging

$$
S_0+P_0=PV(K)+C_0
$$

produces useful synthetic relationships:

$$
C_0-P_0=S_0-PV(K),
$$

so long call plus short put creates the payoff of a long forward financed consistently with the strike. Other legs can similarly be isolated to replicate a stock, call, put, or risk-free claim.

### Strategy comparison

| Strategy | Basic market view or objective | Downside | Upside |
|---|---|---|---|
| Protective put | Own stock with a floor | Floored at strike before premium | Retained |
| Covered call | Income with limited upside | Stock downside partly cushioned by premium | Capped |
| Collar | Keep stock within a payoff band | Floored | Capped |
| Long straddle | Large move in either direction | Limited to premiums | Large gain potential |
| Long strangle | Very large move in either direction | Limited to premiums | Large gain potential |
| Bull call spread | Moderate rise | Limited | Limited |
| Bear put spread | Moderate decline | Limited | Limited |
| Long butterfly | Terminal price near middle strike | Limited | Limited |
| Capital-protected participation | Preserve a floor and retain some upside | Defined floor, subject to contract/issuer | Depends on call participation |

There is no universally best structure. A structure reallocates risk and return; protection, premium income, and upside participation involve trade-offs.

## 5.10 Common errors with option strategies

- Adding initial premiums to a payoff while still labeling the result a payoff rather than profit.
- Comparing an initial premium directly with a terminal payoff without financing it when the calculation requires all values at maturity.
- Ignoring that different strikes divide the payoff into separate regions.
- Forgetting the negative sign on a short option.
- Assuming a zero-cost collar is riskless or economically free.
- Saying a covered call protects the stock's full downside.
- Describing a long straddle or strangle as purely bullish; both are designed for large absolute movements.
- Forgetting that a short uncovered call can create unlimited losses as \(S_T\) rises.
- Combining options with different maturities as though they formed a standard one-maturity payoff.

## 5.11 One-period binomial model

In a one-period binomial model, the stock price can take one of two values at maturity:

$$
S_u=S_0u,
\qquad
S_d=S_0d.
$$

A derivative has corresponding terminal values \(V_u\) and \(V_d\).

### Replication

Construct a portfolio with \(\Delta\) shares and a bond position \(B\), where \(B\) is the bond's value today:

$$
\Delta S_u+B(1+r)=V_u,
$$

$$
\Delta S_d+B(1+r)=V_d.
$$

Subtracting the second equation from the first gives the hedge ratio

$$
\Delta=\frac{V_u-V_d}{S_u-S_d}.
$$

The bond position is

$$
B=\frac{V_d-\Delta S_d}{1+r}.
$$

The derivative's no-arbitrage value today is the cost of the replicating portfolio:

$$
V_0=\Delta S_0+B.
$$

A negative \(B\) represents borrowing. A negative \(\Delta\) represents a short stock position.

### Risk-neutral valuation

Define the risk-neutral up-state probability

$$
q=\frac{(1+r)-d}{u-d}.
$$

Then

$$
V_0=\frac{qV_u+(1-q)V_d}{1+r}.
$$

For an arbitrage-free one-period model, the risk-free gross return lies between the down and up gross stock returns:

$$
d<1+r<u.
$$

This condition ensures \(0<q<1\).

The risk-neutral probability is a pricing device derived from no-arbitrage. It need not equal the real-world probability that the stock price rises. Replication and risk-neutral valuation produce the same derivative price.

## 5.12 Frequent derivatives errors

- Confusing the futures price \(F_0\) with the contract's payoff at maturity.
- Reversing long and short payoffs.
- Calling an option payoff a profit without including the premium.
- Forgetting to finance the spot purchase in a cash-and-carry strategy.
- Comparing cash flows from different dates without compounding or discounting.
- Applying put-call parity to options with different strikes or maturities.
- Buying the expensive parity portfolio and selling the cheap one rather than the reverse.
- Treating risk-neutral probabilities as forecasts of real-world probabilities.
- Discounting the risk-neutral expected payoff incorrectly.
- Forgetting that \(B\) in the replication equations is today's bond position, so it becomes \(B(1+r)\) at maturity.

---


# 6. Blockchain and cryptocurrency foundations

## 6.1 Cryptocurrency and blockchain

A **cryptocurrency** is a digitally represented asset that can be transferred through an electronic network using cryptographic methods. Bitcoin is a cryptocurrency. A cryptocurrency can be bought and sold online, but the ability to trade it does not guarantee its value, liquidity, legality, safety, or future price.

A **blockchain** is a digital ledger in which information is grouped into blocks and linked in sequence. Cryptographic hashes help make later alteration detectable. Copies of the ledger can be maintained across a network rather than by one central clearing house.

The classical intermediary-based model relies on a trusted central party to maintain records and validate transfers. A decentralized blockchain-based model instead uses a protocol and a consensus mechanism so that network participants can agree on the valid history of transactions.

Important distinctions:

- A blockchain is a record-keeping technology; it is not identical to Bitcoin.
- Bitcoin uses a blockchain, but blockchains can support many other assets and applications.
- A cryptocurrency token is not automatically an ownership share in a company. Ownership rights depend on the legal and contractual design of the asset.
- A public ledger can make transaction records visible while users are represented by addresses rather than ordinary names. This is better described as pseudonymity than guaranteed anonymity.

## 6.2 Transactions, blocks, hashes, and the ledger

A simplified transaction process is:

1. A user authorizes a transaction using cryptographic credentials.
2. The transaction is broadcast to the network.
3. Network participants validate it under the protocol's rules.
4. Valid transactions are collected into a block.
5. A consensus mechanism determines how a new block is accepted.
6. The accepted block becomes part of the ledger replicated across the network.

A **hash function** maps input data to a fixed-length output. A small input change produces a different hash. Blocks refer cryptographically to prior data, so changing an old record would disrupt later links and be detectable. This supports tamper evidence, though the security of a real system also depends on network incentives, implementation, governance, and control of consensus resources.

A blockchain helps address the **double-spending problem**: without a trusted intermediary, the network still needs a consistent method for deciding whether the same digital unit has already been transferred elsewhere.

## 6.3 Consensus mechanisms

A consensus mechanism aims to:

- establish agreement about the state and transaction history of the network;
- prevent conflicting transaction histories and double spending;
- give participants incentives to follow the protocol.

### Proof of work

In **proof of work (PoW)**, miners compete using computing power to solve a computational puzzle. The successful miner can propose a block and receive protocol-defined rewards and fees. Rewriting history would require substantial computational resources. The mechanism can be energy intensive.

Bitcoin uses proof of work. New bitcoins are issued through block rewards according to protocol rules. The reward decreases over time, and the protocol limits the maximum bitcoin supply to approximately 21 million coins. Limited supply does not guarantee a stable or rising market price; demand and market conditions still matter.

### Proof of stake

In **proof of stake (PoS)**, validators commit or lock tokens as stake. The protocol selects validators according to its rules, and dishonest behavior can be penalized. PoS avoids the same type of computational competition used by PoW and can require substantially less energy, but it has its own concentration, governance, and implementation risks.

### Proof of history

**Proof of history (PoH)** is a cryptographic ordering mechanism associated with Solana. It provides a verifiable sequence of events and works together with the network's broader consensus design. It should not be confused with proof of work or treated as a complete substitute for all consensus functions by itself.

## 6.4 Cryptoassets, NFTs, and economic rights

Different digital tokens can represent different claims or functions:

- a native cryptocurrency may be used for network transfers, fees, or incentives;
- a utility token may provide access to a service;
- a governance token may provide specified voting rights;
- a stablecoin seeks to track a reference asset but is exposed to design, reserve, counterparty, and market risks;
- a non-fungible token (NFT) is a unique token identifier that can be linked to a digital or physical item.

Owning a token does not automatically confer copyright, company ownership, profit participation, redemption rights, or control over an underlying asset. Those rights depend on the applicable contract and legal framework.

## 6.5 Risks and misconceptions

Cryptoassets can involve:

- extreme price volatility;
- liquidity risk;
- operational and cybersecurity risk;
- loss of private credentials;
- smart-contract or protocol failures;
- counterparty and custody risk;
- regulatory and legal uncertainty;
- manipulation, fraud, and misleading marketing;
- environmental costs, particularly for energy-intensive consensus mechanisms.

Common misconceptions include:

- **“Digital means risk-free.”** Digital assets can lose most or all of their value.
- **“A fixed supply guarantees price appreciation.”** Price depends on both supply and demand.
- **“A branded token is a share in the associated person or business.”** A token conveys only the rights actually specified.
- **“Blockchain records are secret.”** Public blockchains can expose transaction histories even when addresses are pseudonymous.
- **“Blockchain removes the need for trust.”** Trust is redistributed toward software, protocol rules, validators, custodians, governance, and users' security practices.

---


# 7. Behavioral finance

## 7.1 Neoclassical benchmark and behavioral perspective

Neoclassical finance commonly models investors as rational decision makers who use available information consistently and choose portfolios according to stable preferences. Behavioral finance studies how psychology, limited attention, social influence, and non-standard preferences affect financial decisions and market outcomes.

Behavioral observations do not imply that every investor is always irrational. Some biases create mistakes relative to objective information; other patterns reflect preferences that differ from the classical benchmark.

## 7.2 Belief biases

Belief biases affect how people form or update expectations.

### Overconfidence

Overconfidence is excessive faith in one's knowledge, precision, forecasting ability, or control. An investor may believe that they can predict prices more accurately than they actually can. Possible consequences include excessive trading, concentrated positions, underestimation of risk, and insufficient diversification.

### Confirmation bias

Confirmation bias is the tendency to seek, interpret, or remember information that supports an existing belief while discounting conflicting evidence. An investor may focus on favorable news about a holding and dismiss credible negative information.

### Conservatism

Conservatism is insufficient updating when new information arrives. Beliefs adjust too slowly relative to the evidence.

### Representativeness

Representativeness is the tendency to judge probabilities from resemblance to a familiar pattern while neglecting base rates, sample size, or randomness. Investors may extrapolate a short record of strong performance too far into the future.

### Availability and salience

Availability bias occurs when easily recalled or vivid information receives too much weight. Salient recent stories, dramatic market events, or viral content can dominate a more balanced assessment of probability and value.

### Optimism

Optimism bias is a tendency to assign too much probability to favorable outcomes or too little probability to adverse outcomes, especially for one's own decisions or holdings.

## 7.3 Social influence and herding

**Herding** occurs when investors imitate or follow the observed or perceived decisions of others rather than relying solely on independent analysis. It can arise from social proof, reputational concerns, information cascades, or the belief that others possess superior information.

Herding does not mean that investors always act independently; it is specifically a departure from independent decision-making. Online attention, social-media sentiment, and echo chambers can amplify herding, availability, and overconfidence.

## 7.4 Preference biases and mental accounting

Preference-related patterns concern how outcomes are valued rather than only how probabilities are estimated.

### Loss aversion

Loss aversion means that a loss commonly creates more dissatisfaction than an equally sized gain creates satisfaction. It is not the same as ordinary risk aversion: loss aversion is defined relative to gains and losses around a reference point.

### Mental accounting

Mental accounting is the tendency to separate wealth into different psychological accounts and evaluate decisions account by account rather than as part of one integrated portfolio. This can produce inconsistent risk-taking, weak diversification, or different treatment of economically equivalent money.

### Framing

Framing means that choices can change when economically equivalent outcomes are presented differently, for example as gains rather than avoided losses. A fully description-invariant decision maker would choose the same option under equivalent frames.

### Regret aversion

Regret aversion is the desire to avoid choices that could later generate strong regret. It may encourage inaction, conventional decisions, or reluctance to realize mistakes.

### Disposition effect

The disposition effect is the tendency to sell winning investments too early while holding losing investments too long. It can be related to reference-dependent preferences, loss aversion, and reluctance to realize a loss.

### House-money effect and home bias

The house-money effect describes greater willingness to take risk after prior gains are mentally treated as less painful to lose. Home bias is an excessive preference for familiar domestic assets despite the diversification benefits available internationally.

## 7.5 Prospect theory

Prospect theory describes choices in terms of gains and losses relative to a **reference point**, rather than only final wealth. Its value function is commonly represented as:

- defined around a reference point;
- concave for gains, reflecting diminishing sensitivity;
- convex for losses;
- steeper for losses than for equally sized gains, reflecting loss aversion.

The resulting S-shaped value function can help explain why risk attitudes change across gain and loss domains. The reference point matters: the same final wealth can feel like a gain or a loss depending on the benchmark used.

Prospect theory can help explain low diversification, the disposition effect, framing effects, mental accounting, and demand for payoff structures with floors, targets, or capped regions.

## 7.6 Behavioral finance and structured products

Structured products can reshape the distribution of outcomes to reflect an investor's reference points and preferences. For example:

- a long put can create a loss floor;
- a short call can finance protection by surrendering gains above a target;
- a collar can combine both features;
- a risk-free component plus an option can create capital protection with upside participation.

Such products do not eliminate economic trade-offs. A payoff that feels attractive because it fits psychological preferences can still be expensive, expose the investor to issuer risk, reduce liquidity, cap gains, or obscure tail risks. Behavioral suitability and financial value are separate questions.

## 7.7 Capital-market implications

If many investors display similar biases, their behavior can influence trading volume, demand, and prices. Behavioral finance links individual decision patterns to phenomena such as underreaction, overreaction, momentum, reversals, bubbles, or unusually persistent demand. Observing a market pattern, however, does not by itself prove a specific psychological cause; risk, institutions, costs, and data-mining can offer competing explanations.

## 7.8 Frequent behavioral-finance errors

- Defining loss aversion merely as disliking all risk.
- Treating herding as independent decision-making.
- Confusing overconfidence with objectively superior skill.
- Assuming every deviation from a simple rational benchmark is necessarily irrational.
- Ignoring the reference point in prospect theory.
- Treating biases as mutually exclusive; several may reinforce one another.
- Using a behavioral label as a substitute for evidence.
- Assuming a structured product removes risk rather than reallocating it.

---


# 8. Connections across topics

## 8.1 Discounting is the common valuation language

Project cash flows, bond cash flows, strike payments in put-call parity, and risk-neutral expected derivative payoffs are all compared by moving them to a common date. The appropriate rate and risk treatment differ, but the time-value-of-money logic is the same.

## 8.2 Replication and no-arbitrage

Several parts of the course use the same reasoning pattern:

1. Construct two portfolios with identical future cash flows or identical systematic exposure.
2. Compare their current values or expected returns.
3. If identical future cash flows have different current prices, a no-arbitrage trade is possible.

This logic appears in forward pricing, put-call parity, binomial option valuation, and CAPM market/risk-free replication. CAPM replication matches systematic risk; derivative replication matches state-by-state payoffs, so the economic claims are related but not identical.

## 8.3 Diversification and CAPM

Portfolio theory shows mathematically how imperfect correlation reduces portfolio risk. CAPM builds on this insight: because investors can diversify firm-specific risk, only systematic market exposure is priced in equilibrium.

## 8.4 Sensitivity measures

Both duration and beta are sensitivity measures, but they refer to different risks:

- Modified duration approximates a bond price's percentage sensitivity to its yield.
- Beta measures an asset return's sensitivity to market returns.

They are not interchangeable and have different units and interpretations.

## 8.5 Linear approximations versus exact replication

Duration provides an approximation for a bond price change because the price-yield relationship is curved. In contrast, a correctly constructed one-period binomial replicating portfolio matches the derivative payoff exactly in both modeled states.

---


# 9. Compact formula reference

## Value

$$
FV_T=PV_0(1+i)^T,
\qquad
PV_0=\frac{FV_T}{(1+i)^T}
$$

$$
NPV_0=\sum_{t=0}^{T}\frac{CF_t}{(1+i)^t}
$$

$$
AF(i,T)=\frac{(1+i)^T-1}{i(1+i)^T},
\qquad
CRF(i,T)=\frac{1}{AF(i,T)}
$$

$$
PV_{perpetuity}=\frac{C}{r},
\qquad
PV_{growing\ perpetuity}=\frac{C_1}{r-g}
$$

$$
\sum_{t=0}^{T}\frac{CF_t}{(1+IRR)^t}=0
$$

## Bonds

$$
B=\sum_{t=1}^{T}\frac{CF(t)}{(1+i)^t}
$$

$$
D_{Mac}=\frac{\sum_{t=1}^{T}\frac{CF(t)t}{(1+i)^t}}{B},
\qquad
D_{Mod}=\frac{D_{Mac}}{1+i}
$$

$$
\frac{\Delta B}{B}\approx-D_{Mod}\Delta i
$$

$$
D_P=\sum_jw_jD_j,
\qquad
PV_{assets}=PV_{liability},
\qquad
D_P=D_{liability}
$$

## Portfolio theory

$$
\mu=\frac{1}{n}\sum_tR_t,
\qquad
\sigma^2=\frac{1}{n}\sum_t(R_t-\mu)^2
$$

$$
\operatorname{Cov}(R_i,R_j)
=\frac{1}{n}\sum_t(R_{i,t}-\mu_i)(R_{j,t}-\mu_j)
$$

$$
\rho_{ij}=\frac{\operatorname{Cov}(R_i,R_j)}{\sigma_i\sigma_j}
$$

$$
\mu_P=\sum_iw_i\mu_i
$$

$$
\sigma_P^2=\sum_i\sum_jw_iw_j\sigma_i\sigma_j\rho_{ij}
$$

$$
w_1^{MVP}
=\frac{\sigma_2^2-\operatorname{Cov}(R_1,R_2)}
{\sigma_1^2+\sigma_2^2-2\operatorname{Cov}(R_1,R_2)},
\qquad
w_2^{MVP}=1-w_1^{MVP}
$$

## CAPM

$$
\mu=r+\frac{\mu_M-r}{\sigma_M}\sigma
$$

$$
\beta_i=\frac{\operatorname{Cov}(R_i,R_M)}{\operatorname{Var}(R_M)}
=\rho_{iM}\frac{\sigma_i}{\sigma_M}
$$

$$
\mu_i=r+(\mu_M-r)\beta_i
$$

$$
\alpha_i=\mu_i-\left[r+(\mu_M-r)\beta_i\right]
$$

$$
w_M=\beta_i,
\qquad
w_r=1-\beta_i
$$

## Derivatives

$$
F_0=S_0(1+r)^T
$$

$$
\Pi_{long\ forward}=S_T-F_0,
\qquad
\Pi_{short\ forward}=F_0-S_T
$$

$$
\Pi_{long\ call}=\max(S_T-X,0),
\qquad
\Pi_{long\ put}=\max(X-S_T,0)
$$

$$
\Pi_{protective\ put}=S_T+\max(K-S_T,0)=\max(S_T,K)
$$

$$
\Pi_{covered\ call}=S_T-\max(S_T-K,0)=\min(S_T,K)
$$

$$
\Pi_{collar}=S_T+\max(K_L-S_T,0)-\max(S_T-K_U,0)
$$

$$
\Pi_{long\ straddle}=|S_T-K|
$$

$$
S_0+P_0=\frac{X}{(1+r)^T}+C_0
$$

$$
\Delta=\frac{V_u-V_d}{S_u-S_d},
\qquad
B=\frac{V_d-\Delta S_d}{1+r}
$$

$$
q=\frac{(1+r)-d}{u-d},
\qquad
V_0=\frac{qV_u+(1-q)V_d}{1+r}
$$

---


# 10. Suggested prompts for students

The following prompts can be used after providing this file to an AI system.

## Explanation prompts

> Explain the difference between NPV and IRR using one intuitive example and one numerical example. Stay within the course context.

> Explain why diversification depends on correlation and not only on individual volatilities. Then give me a two-asset numerical illustration.

> Compare Macaulay duration, modified duration, maturity, and convexity in a compact table.

> Explain CML versus SML and test my understanding with three short questions, one at a time.

> Derive put-call parity by comparing terminal payoffs in all relevant states.

## Practice-question prompts

> Create five original calculation questions on present value, annuities, growing perpetuities, and IRR. Use new fictional data, give no answers initially, and increase the difficulty gradually.

> Create a mixed bond exercise covering price, yield of a zero-coupon bond, Macaulay duration, modified duration, and a duration-based price approximation. After I answer, grade every step.

> Give me a return dataset for two assets and ask me to calculate means, population variances, covariance, correlation, minimum-variance weights, portfolio return, and portfolio volatility. Keep full precision in the solution.

> Create conceptual CAPM multiple-choice questions about beta, alpha, CML versus SML, systematic versus unsystematic risk, and market/risk-free replication. Explain all answer choices after I respond.

> Create one original no-arbitrage exercise each on forward pricing, put-call parity, and one-period binomial option valuation. Require me to list every cash flow by date.

> Give me terminal stock-price scenarios and ask me to derive the total payoff and profit of a protective put, covered call, collar, straddle, strangle, vertical spread, and butterfly. Do not name the strategy until after I identify it.

> Ask me to design an option structure for each of the following objectives: downside floor, capped upside with premium income, moderate bullish view, moderate bearish view, large movement in either direction, and a stable terminal price near a target.

> Create ten conceptual questions on blockchain, cryptocurrencies, consensus mechanisms, token ownership rights, and cryptoasset risks. Keep the questions independent of current market prices or news.

> Quiz me on behavioral finance using short investor scenarios. Ask me to identify and distinguish loss aversion, herding, overconfidence, confirmation bias, availability, framing, mental accounting, and the disposition effect.

## Feedback prompts

> Here is my solution. Check it line by line, identify the first error, explain why it is wrong, and let me correct it before continuing.

> Diagnose whether my mistake is conceptual, algebraic, a timing error, a sign error, or premature rounding.

> Do not solve the problem yet. Ask me the smallest useful hint that helps me choose the correct formula.

## Oral-review prompt

> Conduct a 15-question oral review based only on this course context. Mix definitions, economic intuition, formula selection, and short calculations. Ask one question at a time, adapt the difficulty to my answers, and finish with a summary of my three weakest areas.

---


# 11. Final concept checklist

A student should be able to:

- move cash flows between dates using compounding and discounting;
- calculate and interpret NPV;
- convert between present values and equivalent annuities;
- value constant and growing perpetuities with correct timing;
- define IRR and recognize its limitations;
- price zero-coupon and coupon bonds;
- explain premium, discount, and par pricing;
- calculate and interpret Macaulay and modified duration;
- use duration for a linear price approximation and explain convexity error;
- state the two basic immunization conditions;
- calculate population mean, variance, volatility, covariance, and correlation;
- calculate expected portfolio return, variance, and volatility;
- explain diversification for different correlations;
- calculate and interpret two-asset minimum-variance weights;
- explain the efficient frontier and two-fund separation;
- distinguish systematic from unsystematic risk;
- calculate and interpret beta;
- distinguish CML from SML;
- apply the CAPM pricing equation and interpret alpha;
- create a market/risk-free portfolio with a target beta;
- use a CAPM return as a risk-adjusted cost of capital;
- calculate long and short forward payoffs;
- derive a fair forward price and describe cash-and-carry logic;
- calculate basic call and put payoffs while distinguishing payoff from profit;
- explain and apply put-call parity and the law of one price;
- replicate a one-period derivative with stock and bond positions;
- value a one-period derivative using risk-neutral valuation;
- recognize the assumptions and common errors associated with each method;
- interpret credit ratings and CDS-spread movements as distinct indicators of credit risk;
- construct and analyze protective puts, covered calls, collars, straddles, strangles, vertical spreads, butterflies, and capital-protected participation structures;
- distinguish a strategy's payoff from its profit and calculate relevant break-even regions;
- explain how put-call parity creates synthetic positions;
- define blockchain, cryptocurrency, distributed ledger, hash, and double spending;
- compare proof of work, proof of stake, and proof of history at a conceptual level;
- explain why a token does not automatically convey company ownership or other legal rights;
- recognize major cryptoasset risks and common misconceptions;
- explain the behavioral-finance perspective relative to the neoclassical benchmark;
- identify loss aversion, herding, overconfidence, confirmation bias, availability, representativeness, framing, and mental accounting;
- explain reference dependence, the prospect-theory value function, and the disposition effect;
- connect investor preferences with structured payoff design without treating structure as free risk removal.

This checklist describes the conceptual scope of the course-context knowledge base. It does not indicate which concepts will appear in any particular assessment.


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
