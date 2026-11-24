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
