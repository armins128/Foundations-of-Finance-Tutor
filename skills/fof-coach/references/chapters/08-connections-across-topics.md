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
