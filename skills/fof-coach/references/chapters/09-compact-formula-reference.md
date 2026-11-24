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
