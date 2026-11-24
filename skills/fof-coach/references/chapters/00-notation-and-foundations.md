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
