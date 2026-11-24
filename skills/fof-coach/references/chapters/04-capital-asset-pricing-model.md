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
