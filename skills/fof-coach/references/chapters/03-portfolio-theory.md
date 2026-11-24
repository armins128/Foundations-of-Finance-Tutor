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
