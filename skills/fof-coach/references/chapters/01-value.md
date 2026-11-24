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
