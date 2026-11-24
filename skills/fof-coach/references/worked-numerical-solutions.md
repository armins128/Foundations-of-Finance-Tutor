# Worked numerical practice

Original fictional data. Read after an attempt or on explicit request. Four decimals are display values; calculations use full precision.

## Q01

A repair kiosk costs EUR 840 today and pays EUR 330 at each year-end for three years, with no residual value. Required annual effective return is 7%. Find PV of receipts and NPV. Use full precision internally; give final numbers to four decimals with units.

PV=330*(1-1.07^-3)/0.07; NPV=PV-840. Interpret against the opportunity cost.

- pv_eur: **866.0243**
- npv_eur: **26.0243**

## Q02

A kiosk pays EUR 180 at t=1 and EUR 210 plus EUR 620 sale proceeds at t=2. Required return 6%. What is the reservation price today? Use full precision internally; give final numbers to four decimals with units.

Price=180/1.06+(210+620)/1.06^2; final proceeds counted once.

- price_eur: **908.5084**

## Q03

Repay a EUR 2400 loan through four equal year-end installments at 4%. Find annual installment and year-1 principal repayment. Use full precision internally; give final numbers to four decimals with units.

Payment=2400/AF(4%,4); interest1=96; amortization1=payment-96.

- payment_eur: **661.1761**
- principal_repaid_eur: **565.1761**

## Q04

Two one-off projects have NPVs EUR 120 and EUR 160, with lives 2 and 4 years. At 5%, convert both NPVs to annual equivalents using a COMMON four-year comparison horizon. No replacement is assumed. Use full precision internally; give final numbers to four decimals with units.

Use the same CRF(5%,4) for both NPVs; B ranks higher. Do not annualize each over its own life.

- annual_a_eur: **33.8414**
- annual_b_eur: **45.1219**

## Q05

An annual EUR 72 payment continues forever, first at t=4. Discount rate 9%. Find PV today. Use full precision internally; give final numbers to four decimals with units.

72/0.09 is value at t=3, then divide by 1.09^3.

- pv_eur: **617.7468**

## Q06

A license has just paid EUR 24 (C0). Future annual payments continue indefinitely, growing 3%; required return is 9%. Find PV immediately after the payment. Use full precision internally; give final numbers to four decimals with units.

C1=24*1.03; PV=C1/(0.09-0.03). The just-paid C0 is excluded.

- pv_eur: **412.0000**

## Q07

A project costs EUR 640 today and pays EUR 768 in one year only. Find IRR and NPV at a 12% required return. Use full precision internally; give final numbers to four decimals with units.

IRR=768/640-1; NPV=-640+768/1.12; conventional independent project.

- irr_decimal: **0.2000**
- npv_eur: **45.7143**

## Q08

Deposit EUR 140 at the end of each of five years at 4%. Find terminal wealth at t=5. Use full precision internally; give final numbers to four decimals with units.

FV=140*FVAF(4%,5); independently accumulate each of the five deposits.

- fv_eur: **758.2852**

## Q09

A noncallable bond pays EUR 50 annually for three years and repays EUR 1000 principal with its last coupon. Annual effective yield is 4%. Find price and Macaulay duration in years. Use full precision internally; give final numbers to four decimals with units.

B=50/1.04+50/1.04^2+1050/1.04^3; DMac=sum(t*PV(CFt))/B.

- price_eur: **1027.7509**
- duration_years: **2.8615**

## Q10

A zero-coupon bond pays EUR 1200 in three years and costs EUR 1050 now. Find its annual effective yield. Use full precision internally; give final numbers to four decimals with units.

y=(1200/1050)^(1/3)-1; annual compounding.

- yield_decimal: **0.0455**

## Q11

A bond pays coupons of EUR 25 at t=0.5,1,1.5,2 and principal EUR 1000 at t=2. Annual EFFECTIVE yield is 6%. Find its price. Use full precision internally; give final numbers to four decimals with units.

Discount using fractional-year powers of 1.06; do not simply divide an effective annual yield by two.

- price_eur: **983.0211**

## Q12

For a bond with cash flows EUR 50,50,1050 at t=1,2,3, yield rises from 4% to 5%. Use STANDARD modified duration at the initial yield. Calculate approximate price, exact repriced price and approximation minus exact. Use full precision internally; give final numbers to four decimals with units.

Use Q09 data recalculated at full precision: Dmod=DMac/1.04; Bapprox=B*(1-Dmod*0.01). Reprice at 5%; tangent lies below convex curve.

- approx_eur: **999.4733**
- exact_eur: **1000.0000**
- error_eur: **-0.5267**

## Q13

A single liability of EUR 15000 is due at t=5; yield curve flat at 4%. Two assets have Macaulay durations 2 and 7 years. Find PV liability and asset-1 market-value weight for duration matching. Use full precision internally; give final numbers to four decimals with units.

PV=L/1.04^5; w*2+(1-w)*7=5. Allocate this PV across assets using w and 1-w.

- pv_eur: **12328.9066**
- weight1_decimal: **0.4000**

## Q14

A lottery pays EUR 20 with probability 0.4 or EUR 80 with probability 0.6. U(W)=ln(W+1). Find expected wealth, expected utility, certainty equivalent and monetary risk premium. Use full precision internally; give final numbers to four decimals with units.

E[W]=0.4*20+0.6*80; EU=0.4*ln(21)+0.6*ln(81); CE=exp(EU)-1; RP=56-CE.

- expected_eur: **56.0000**
- expected_utility: **3.8545**
- ce_eur: **46.2040**
- risk_premium_eur: **9.7960**

## Q15

Using U=mu-b*sigma^2 with RETURNS IN DECIMALS and b=2, compare A: mu=0.08,sigma=0.15 with B: mu=0.07,sigma=0.10. Give both utilities. Use full precision internally; give final numbers to four decimals with units.

UA=0.08-2*0.15^2; UB=0.07-2*0.10^2; choose larger utility under this specified model.

- utility_a: **0.0350**
- utility_b: **0.0500**

## Q16

Four equally weighted yearly decimal returns: A=(0.12,-0.04,0.08,0.04), B=(0.02,0.06,0.04,0). Find A mean and population volatility, covariance(A,B) and correlation(A,B). Use full precision internally; give final numbers to four decimals with units.

Means are arithmetic; variance and covariance divide by n=4. Correlation=cov/sqrt(varA*varB).

- mean_a_decimal: **0.0500**
- vol_a_decimal: **0.0592**
- cov_decimal_squared: **-0.0007**
- correlation: **-0.5292**

## Q17

State probabilities are (0.2,0.5,0.3), with returns (-0.10,0.04,0.16). Find expected return and volatility as decimals. Use full precision internally; give final numbers to four decimals with units.

mu=sum(p*R); variance=sum(p*(R-mu)^2); no divisor n after weighting by unequal probabilities.

- mean_decimal: **0.0480**
- vol_decimal: **0.0904**

## Q18

A has mean 0.05 and variance 0.0035; B has mean 0.03 and variance 0.0005; covariance is -0.0007. Invest 40% in A, 60% in B. Find portfolio mean and volatility. Use full precision internally; give final numbers to four decimals with units.

muP=0.4*0.05+0.6*0.03; variance=0.4^2*0.0035+0.6^2*0.0005+2*0.4*0.6*(-0.0007); take sqrt.

- mean_decimal: **0.0380**
- vol_decimal: **0.0201**

## Q19

Two assets have variances 0.0035 and 0.0005 and covariance -0.0007. Find unconstrained minimum-variance weight in the first asset and minimum portfolio volatility. Use full precision internally; give final numbers to four decimals with units.

wA=(0.0005+0.0007)/(0.0035+0.0005+0.0014); insert weights in full portfolio variance.

- weight_a_decimal: **0.2222**
- vol_decimal: **0.0153**

## Q20

Assets have volatilities 0.12 and 0.18 and correlation -1. Find the first asset weight in a fully invested long-only zero-volatility portfolio. Use full precision internally; give final numbers to four decimals with units.

wA*0.12=(1-wA)*0.18; verify variance cancels.

- weight_a_decimal: **0.6000**

## Q21

A stock has covariance 0.018 with a market of variance 0.015. Risk-free return is 0.02; expected market return is 0.08; stock forecast return is 0.11. Find beta, CAPM required return and forecast alpha. Use full precision internally; give final numbers to four decimals with units.

beta=0.018/0.015; required=0.02+beta*(0.08-0.02); alpha=0.11-required. Forecast lies above SML.

- beta: **1.2000**
- required_return_decimal: **0.0920**
- alpha_decimal: **0.0180**

## Q22

Stock volatility is 0.30, market volatility 0.20, correlation 0.6. Find beta, systematic volatility and residual volatility. Use full precision internally; give final numbers to four decimals with units.

beta=rho*sigmaS/sigmaM; sys volatility=abs(rho)*sigmaS; residual volatility=sigmaS*sqrt(1-rho^2). Variances add.

- beta: **0.9000**
- systematic_vol_decimal: **0.1800**
- residual_vol_decimal: **0.2400**

## Q23

Risk-free return 0.02, expected market return 0.08, market volatility 0.16. On the positive market CML branch, target expected return 0.11. Find market weight, cash weight and portfolio volatility. Use full precision internally; give final numbers to four decimals with units.

wM=(0.11-0.02)/(0.08-0.02); wCash=1-wM; sigmaP=abs(wM)*0.16. Negative cash means borrowing.

- market_weight: **1.5000**
- cash_weight: **-0.5000**
- vol_decimal: **0.2400**

## Q24

A fully invested portfolio fixes stock weight at 0.40. Stock beta is 1.5; market beta is 1 and cash beta is 0. Choose market and cash weights so portfolio beta is zero. Borrowing and shorting permitted. Use full precision internally; give final numbers to four decimals with units.

0.4*1.5+wM=0 -> wM=-0.6; cash=1-0.4-(-0.6)=1.2. Residual stock risk remains.

- market_weight: **-0.6000**
- cash_weight: **1.2000**

## Q25

A one-year equity claim has expected payoff EUR 112. Beta=1.1, rf=0.03 and expected market return=0.08. Find required return and fair price using CAPM. Use full precision internally; give final numbers to four decimals with units.

Required return=0.03+1.1*(0.08-0.03)=0.085; price=112/1.085.

- return_decimal: **0.0850**
- price_eur: **103.2258**

## Q26

A no-payout asset costs EUR 240. Annual effective financing rate=0.04, maturity=0.5 years. A forward quote is EUR 247. Find fair delivery price and cash-and-carry profit at maturity per unit, ignoring friction. Use full precision internally; give final numbers to four decimals with units.

Borrow 240, buy asset, short forward; terminal receipt 247 minus loan repayment 240*1.04^0.5.

- fair_eur: **244.7529**
- profit_eur: **2.2471**

## Q27

A long European put has strike EUR 55, premium EUR 4 paid today, and terminal stock price EUR 47. Ignore financing of the premium. Find put payoff and simple profit. Use full precision internally; give final numbers to four decimals with units.

Payoff=max(55-47,0)=8; simple profit=8-4. A short put has opposite values.

- payoff_eur: **8.0000**
- profit_eur: **4.0000**

## Q28

A no-dividend stock costs EUR 58; same-strike European call costs EUR 6, strike EUR 60, maturity one year, rf=0.05. Find European put price. Use full precision internally; give final numbers to four decimals with units.

P=C+X/(1+r)-S; replicate max(ST,X) with stock+put versus call+bond.

- put_eur: **5.1429**

## Q29

One-period model: S0=EUR 48, Su=60, Sd=36, European call strike=50, rf=0.05. Find replicating delta, cash investment today, call price and risk-neutral up probability. Use full precision internally; give final numbers to four decimals with units.

Cu=10,Cd=0; delta=10/24; B0=(0-delta*36)/1.05; C0=delta*48+B0; q=(1.05-0.75)/(1.25-0.75).

- delta: **0.4167**
- cash_eur: **-14.2857**
- call_eur: **5.7143**
- q: **0.6000**

## Q30

Buy stock for EUR 60, buy put strike 54 for EUR 3 and sell call strike 68 for EUR 2. Ignore financing of initial cost. Find collar payoff at ST=45,60,80 and simple profit at ST=80. Use full precision internally; give final numbers to four decimals with units.

Payoff=ST+max(54-ST,0)-max(ST-68,0); net initial cost=60+3-2=61; high-state profit=68-61.

- payoff_low_eur: **54.0000**
- payoff_mid_eur: **60.0000**
- payoff_high_eur: **68.0000**
- profit_high_eur: **7.0000**

## Q31

A long straddle buys a call and put of strike EUR 70 for premiums EUR 5 and EUR 4. Ignore premium financing. Find the two break-even stock prices and profit at ST=82. Use full precision internally; give final numbers to four decimals with units.

Straddle payoff=abs(ST-70); total premium=9; break-evens 70+-9; profit at 82=12-9.

- lower_be_eur: **61.0000**
- upper_be_eur: **79.0000**
- profit_eur: **3.0000**

## Q32

A EUR 100 budget must guarantee EUR 100 at t=2 using a default-free zero bond. Annual effective rf=5%. One call costs EUR 8. Ignore fees. Find zero-bond cost and calls affordable per product. Use full precision internally; give final numbers to four decimals with units.

Bond cost=100/1.05^2; remaining budget divided by 8 buys calls; promised floor depends on bond performance.

- bond_cost_eur: **90.7029**
- call_units: **1.1621**

## Q33

A comparable basket costs 21 domestic units and 7 foreign units. Market quote=2.5 domestic units per foreign unit. Find absolute PPP quote and domestic basket price in foreign units. Compute the domestic basket premium relative to the foreign basket. Use full precision internally; give final numbers to four decimals with units.

PPP=21/7=3; convert domestic basket by dividing by 2.5; premium=(8.4-7)/7. State denominator.

- ppp_domestic_per_foreign: **3.0000**
- domestic_basket_foreign_units: **8.4000**
- premium_decimal: **0.2000**

## Q34

Spot quote is 1.20 domestic per foreign. Domestic interest=4%, foreign interest=2%; one year. Separately domestic inflation=3%, foreign inflation=1%. Find covered forward quote and relative-PPP predicted spot quote. Use full precision internally; give final numbers to four decimals with units.

CIP uses interest factors; relative PPP uses inflation factors. These relations have different assumptions and need not give identical numbers.

- forward_domestic_per_foreign: **1.2235**
- ppp_spot_domestic_per_foreign: **1.2238**

## Q35

In the standard informed-host three-door game, give switching win probability. Separately an independent fixed-frequency game has P(red)=0.8 and equal rewards for correct guesses: find success probability under probability matching and under always-red. Use full precision internally; give final numbers to four decimals with units.

Standard informed host: switch succeeds iff first choice wrong (2/3). Probability matching success=p^2+(1-p)^2; always choose more likely color gives p.

- switch_probability: **0.6667**
- matching_probability: **0.6800**
- always_red_probability: **0.8000**

## Q36

Assume uniform independent binary hash prefixes. A puzzle requires 8 leading binary zeros. Find expected trials. Then a fictional protocol block subsidy of 12 units undergoes three halvings; find the new subsidy (this is NOT a current Bitcoin reward). Use full precision internally; give final numbers to four decimals with units.

Success probability=2^-8, expected trials=256. Subsidy=12*(1/2)^3; existing balances do not halve.

- expected_trials: **256.0000**
- subsidy_units: **1.5000**
