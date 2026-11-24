"""Original fixed practice instances; calculation paths are bundled with answers."""
from math import sqrt, log, exp, isclose


def bank():
    out = []

    def add(key, skills, prompt, answers, method, units='decimal unless labelled'):
        out.append(dict(id=key, competencies=skills.split(','), family=key,
                        kind='numerical', difficulty=3, points=len(answers)*2,
                        minutes=max(2,len(answers)*2), prompt=prompt+
                        ' Use full precision internally; give final numbers to four decimals with units.',
                        answers=answers, units=units, solution=method,
                        hints=['Identify dates, signs and the requested units.',
                               'Choose the matching formula in the course companion; name each input.',
                               'Write the substituted expression before evaluating it.']))

    af = lambda r,t: t if r == 0 else (1-(1+r)**-t)/r
    npv = lambda c,r: sum(x/(1+r)**t for t,x in enumerate(c))
    add('Q01','V01,V02','A repair kiosk costs EUR 840 today and pays EUR 330 at each year-end for three years, with no residual value. Required annual effective return is 7%. Find PV of receipts and NPV.',
        {'pv_eur':330*af(.07,3),'npv_eur':npv([-840,330,330,330],.07)},
        'PV=330*(1-1.07^-3)/0.07; NPV=PV-840. Interpret against the opportunity cost.')
    add('Q02','V03','A kiosk pays EUR 180 at t=1 and EUR 210 plus EUR 620 sale proceeds at t=2. Required return 6%. What is the reservation price today?',
        {'price_eur':180/1.06+830/1.06**2}, 'Price=180/1.06+(210+620)/1.06^2; final proceeds counted once.')
    a=2400/af(.04,4)
    add('Q03','V04','Repay a EUR 2400 loan through four equal year-end installments at 4%. Find annual installment and year-1 principal repayment.',
        {'payment_eur':a,'principal_repaid_eur':a-2400*.04}, 'Payment=2400/AF(4%,4); interest1=96; amortization1=payment-96.')
    add('Q04','V05','Two one-off projects have NPVs EUR 120 and EUR 160, with lives 2 and 4 years. At 5%, convert both NPVs to annual equivalents using a COMMON four-year comparison horizon. No replacement is assumed.',
        {'annual_a_eur':120/af(.05,4),'annual_b_eur':160/af(.05,4)}, 'Use the same CRF(5%,4) for both NPVs; B ranks higher. Do not annualize each over its own life.')
    add('Q05','V06','An annual EUR 72 payment continues forever, first at t=4. Discount rate 9%. Find PV today.',
        {'pv_eur':72/.09/1.09**3}, '72/0.09 is value at t=3, then divide by 1.09^3.')
    add('Q06','V06','A license has just paid EUR 24 (C0). Future annual payments continue indefinitely, growing 3%; required return is 9%. Find PV immediately after the payment.',
        {'pv_eur':24*1.03/(.09-.03)}, 'C1=24*1.03; PV=C1/(0.09-0.03). The just-paid C0 is excluded.')
    add('Q07','V07','A project costs EUR 640 today and pays EUR 768 in one year only. Find IRR and NPV at a 12% required return.',
        {'irr_decimal':768/640-1,'npv_eur':-640+768/1.12}, 'IRR=768/640-1; NPV=-640+768/1.12; conventional independent project.')
    add('Q08','V08','Deposit EUR 140 at the end of each of five years at 4%. Find terminal wealth at t=5.',
        {'fv_eur':140*((1.04**5-1)/.04)}, 'FV=140*FVAF(4%,5); independently accumulate each of the five deposits.')
    c=[50,50,1050]; price=sum(x/1.04**t for t,x in enumerate(c,1)); dur=sum(t*x/1.04**t for t,x in enumerate(c,1))/price
    add('Q09','B01,B04','A noncallable bond pays EUR 50 annually for three years and repays EUR 1000 principal with its last coupon. Annual effective yield is 4%. Find price and Macaulay duration in years.',
        {'price_eur':price,'duration_years':dur}, 'B=50/1.04+50/1.04^2+1050/1.04^3; DMac=sum(t*PV(CFt))/B.')
    add('Q10','B02','A zero-coupon bond pays EUR 1200 in three years and costs EUR 1050 now. Find its annual effective yield.',
        {'yield_decimal':(1200/1050)**(1/3)-1}, 'y=(1200/1050)^(1/3)-1; annual compounding.')
    add('Q11','B03','A bond pays coupons of EUR 25 at t=0.5,1,1.5,2 and principal EUR 1000 at t=2. Annual EFFECTIVE yield is 6%. Find its price.',
        {'price_eur':sum(25/1.06**(j/2) for j in range(1,5))+1000/1.06**2}, 'Discount using fractional-year powers of 1.06; do not simply divide an effective annual yield by two.')
    exact=sum(x/1.05**t for t,x in enumerate(c,1)); approx=price*(1-dur/1.04*.01)
    add('Q12','B05','For a bond with cash flows EUR 50,50,1050 at t=1,2,3, yield rises from 4% to 5%. Use STANDARD modified duration at the initial yield. Calculate approximate price, exact repriced price and approximation minus exact.',
        {'approx_eur':approx,'exact_eur':exact,'error_eur':approx-exact}, 'Use Q09 data recalculated at full precision: Dmod=DMac/1.04; Bapprox=B*(1-Dmod*0.01). Reprice at 5%; tangent lies below convex curve.')
    add('Q13','B06','A single liability of EUR 15000 is due at t=5; yield curve flat at 4%. Two assets have Macaulay durations 2 and 7 years. Find PV liability and asset-1 market-value weight for duration matching.',
        {'pv_eur':15000/1.04**5,'weight1_decimal':(5-7)/(2-7)}, 'PV=L/1.04^5; w*2+(1-w)*7=5. Allocate this PV across assets using w and 1-w.')
    eu=.4*log(21)+.6*log(81); ce=exp(eu)-1
    add('Q14','N03,N04','A lottery pays EUR 20 with probability 0.4 or EUR 80 with probability 0.6. U(W)=ln(W+1). Find expected wealth, expected utility, certainty equivalent and monetary risk premium.',
        {'expected_eur':56,'expected_utility':eu,'ce_eur':ce,'risk_premium_eur':56-ce}, 'E[W]=0.4*20+0.6*80; EU=0.4*ln(21)+0.6*ln(81); CE=exp(EU)-1; RP=56-CE.')
    add('Q15','N05','Using U=mu-b*sigma^2 with RETURNS IN DECIMALS and b=2, compare A: mu=0.08,sigma=0.15 with B: mu=0.07,sigma=0.10. Give both utilities.',
        {'utility_a':.08-2*.15**2,'utility_b':.07-2*.10**2}, 'UA=0.08-2*0.15^2; UB=0.07-2*0.10^2; choose larger utility under this specified model.')
    ra=[.12,-.04,.08,.04]; rb=[.02,.06,.04,0]; ma=sum(ra)/4; mb=sum(rb)/4
    va=sum((v-ma)**2 for v in ra)/4; vb=sum((v-mb)**2 for v in rb)/4; cov=sum((a-ma)*(b-mb) for a,b in zip(ra,rb))/4
    add('Q16','P01,P03','Four equally weighted yearly decimal returns: A=(0.12,-0.04,0.08,0.04), B=(0.02,0.06,0.04,0). Find A mean and population volatility, covariance(A,B) and correlation(A,B).',
        {'mean_a_decimal':ma,'vol_a_decimal':sqrt(va),'cov_decimal_squared':cov,'correlation':cov/sqrt(va*vb)}, 'Means are arithmetic; variance and covariance divide by n=4. Correlation=cov/sqrt(varA*varB).')
    probs=[.2,.5,.3]; rs=[-.1,.04,.16]; mean=sum(p*v for p,v in zip(probs,rs)); var=sum(p*(v-mean)**2 for p,v in zip(probs,rs))
    add('Q17','P02','State probabilities are (0.2,0.5,0.3), with returns (-0.10,0.04,0.16). Find expected return and volatility as decimals.',
        {'mean_decimal':mean,'vol_decimal':sqrt(var)}, 'mu=sum(p*R); variance=sum(p*(R-mu)^2); no divisor n after weighting by unequal probabilities.')
    w=.4; vp=w*w*va+(1-w)**2*vb+2*w*(1-w)*cov
    add('Q18','P04,P05','A has mean 0.05 and variance 0.0035; B has mean 0.03 and variance 0.0005; covariance is -0.0007. Invest 40% in A, 60% in B. Find portfolio mean and volatility.',
        {'mean_decimal':w*ma+(1-w)*mb,'vol_decimal':sqrt(vp)}, 'muP=0.4*0.05+0.6*0.03; variance=0.4^2*0.0035+0.6^2*0.0005+2*0.4*0.6*(-0.0007); take sqrt.')
    mvp=(vb-cov)/(va+vb-2*cov); mvpvar=mvp*mvp*va+(1-mvp)**2*vb+2*mvp*(1-mvp)*cov
    add('Q19','P07','Two assets have variances 0.0035 and 0.0005 and covariance -0.0007. Find unconstrained minimum-variance weight in the first asset and minimum portfolio volatility.',
        {'weight_a_decimal':mvp,'vol_decimal':sqrt(mvpvar)}, 'wA=(0.0005+0.0007)/(0.0035+0.0005+0.0014); insert weights in full portfolio variance.')
    add('Q20','P06','Assets have volatilities 0.12 and 0.18 and correlation -1. Find the first asset weight in a fully invested long-only zero-volatility portfolio.',
        {'weight_a_decimal':.18/(.12+.18)}, 'wA*0.12=(1-wA)*0.18; verify variance cancels.')
    add('Q21','C01,C03,C04','A stock has covariance 0.018 with a market of variance 0.015. Risk-free return is 0.02; expected market return is 0.08; stock forecast return is 0.11. Find beta, CAPM required return and forecast alpha.',
        {'beta':1.2,'required_return_decimal':.02+1.2*.06,'alpha_decimal':.11-(.02+1.2*.06)}, 'beta=0.018/0.015; required=0.02+beta*(0.08-0.02); alpha=0.11-required. Forecast lies above SML.')
    add('Q22','C02','Stock volatility is 0.30, market volatility 0.20, correlation 0.6. Find beta, systematic volatility and residual volatility.',
        {'beta':.6*.3/.2,'systematic_vol_decimal':.6*.3,'residual_vol_decimal':.3*sqrt(1-.6**2)}, 'beta=rho*sigmaS/sigmaM; sys volatility=abs(rho)*sigmaS; residual volatility=sigmaS*sqrt(1-rho^2). Variances add.')
    wm=(.11-.02)/(.08-.02)
    add('Q23','C05','Risk-free return 0.02, expected market return 0.08, market volatility 0.16. On the positive market CML branch, target expected return 0.11. Find market weight, cash weight and portfolio volatility.',
        {'market_weight':wm,'cash_weight':1-wm,'vol_decimal':abs(wm)*.16}, 'wM=(0.11-0.02)/(0.08-0.02); wCash=1-wM; sigmaP=abs(wM)*0.16. Negative cash means borrowing.')
    add('Q24','C06','A fully invested portfolio fixes stock weight at 0.40. Stock beta is 1.5; market beta is 1 and cash beta is 0. Choose market and cash weights so portfolio beta is zero. Borrowing and shorting permitted.',
        {'market_weight':-.4*1.5,'cash_weight':1-.4+.4*1.5}, '0.4*1.5+wM=0 -> wM=-0.6; cash=1-0.4-(-0.6)=1.2. Residual stock risk remains.')
    add('Q25','C07','A one-year equity claim has expected payoff EUR 112. Beta=1.1, rf=0.03 and expected market return=0.08. Find required return and fair price using CAPM.',
        {'return_decimal':.03+1.1*.05,'price_eur':112/(1+.03+1.1*.05)}, 'Required return=0.03+1.1*(0.08-0.03)=0.085; price=112/1.085.')
    add('Q26','D01,D02','A no-payout asset costs EUR 240. Annual effective financing rate=0.04, maturity=0.5 years. A forward quote is EUR 247. Find fair delivery price and cash-and-carry profit at maturity per unit, ignoring friction.',
        {'fair_eur':240*1.04**.5,'profit_eur':247-240*1.04**.5}, 'Borrow 240, buy asset, short forward; terminal receipt 247 minus loan repayment 240*1.04^0.5.')
    add('Q27','D05','A long European put has strike EUR 55, premium EUR 4 paid today, and terminal stock price EUR 47. Ignore financing of the premium. Find put payoff and simple profit.',
        {'payoff_eur':8,'profit_eur':4}, 'Payoff=max(55-47,0)=8; simple profit=8-4. A short put has opposite values.')
    add('Q28','D06','A no-dividend stock costs EUR 58; same-strike European call costs EUR 6, strike EUR 60, maturity one year, rf=0.05. Find European put price.',
        {'put_eur':6+60/1.05-58}, 'P=C+X/(1+r)-S; replicate max(ST,X) with stock+put versus call+bond.')
    s=48; su=60; sd=36; strike=50; r=.05; cu=10; cd=0; delta=(cu-cd)/(su-sd); cash=(cd-delta*sd)/(1+r); call=delta*s+cash; q=(1+r-.75)/(1.25-.75)
    add('Q29','D07','One-period model: S0=EUR 48, Su=60, Sd=36, European call strike=50, rf=0.05. Find replicating delta, cash investment today, call price and risk-neutral up probability.',
        {'delta':delta,'cash_eur':cash,'call_eur':call,'q':q}, 'Cu=10,Cd=0; delta=10/24; B0=(0-delta*36)/1.05; C0=delta*48+B0; q=(1.05-0.75)/(1.25-0.75).')
    add('Q30','D08','Buy stock for EUR 60, buy put strike 54 for EUR 3 and sell call strike 68 for EUR 2. Ignore financing of initial cost. Find collar payoff at ST=45,60,80 and simple profit at ST=80.',
        {'payoff_low_eur':54,'payoff_mid_eur':60,'payoff_high_eur':68,'profit_high_eur':7}, 'Payoff=ST+max(54-ST,0)-max(ST-68,0); net initial cost=60+3-2=61; high-state profit=68-61.')
    add('Q31','D08','A long straddle buys a call and put of strike EUR 70 for premiums EUR 5 and EUR 4. Ignore premium financing. Find the two break-even stock prices and profit at ST=82.',
        {'lower_be_eur':61,'upper_be_eur':79,'profit_eur':3}, 'Straddle payoff=abs(ST-70); total premium=9; break-evens 70+-9; profit at 82=12-9.')
    add('Q32','D09','A EUR 100 budget must guarantee EUR 100 at t=2 using a default-free zero bond. Annual effective rf=5%. One call costs EUR 8. Ignore fees. Find zero-bond cost and calls affordable per product.',
        {'bond_cost_eur':100/1.05**2,'call_units':(100-100/1.05**2)/8}, 'Bond cost=100/1.05^2; remaining budget divided by 8 buys calls; promised floor depends on bond performance.')
    add('Q33','X01','A comparable basket costs 21 domestic units and 7 foreign units. Market quote=2.5 domestic units per foreign unit. Find absolute PPP quote and domestic basket price in foreign units. Compute the domestic basket premium relative to the foreign basket.',
        {'ppp_domestic_per_foreign':3,'domestic_basket_foreign_units':21/2.5,'premium_decimal':(21/2.5)/7-1}, 'PPP=21/7=3; convert domestic basket by dividing by 2.5; premium=(8.4-7)/7. State denominator.')
    add('Q34','X02,X03','Spot quote is 1.20 domestic per foreign. Domestic interest=4%, foreign interest=2%; one year. Separately domestic inflation=3%, foreign inflation=1%. Find covered forward quote and relative-PPP predicted spot quote.',
        {'forward_domestic_per_foreign':1.2*1.04/1.02,'ppp_spot_domestic_per_foreign':1.2*1.03/1.01}, 'CIP uses interest factors; relative PPP uses inflation factors. These relations have different assumptions and need not give identical numbers.')
    add('Q35','H06,H08','In the standard informed-host three-door game, give switching win probability. Separately an independent fixed-frequency game has P(red)=0.8 and equal rewards for correct guesses: find success probability under probability matching and under always-red.',
        {'switch_probability':2/3,'matching_probability':.8**2+.2**2,'always_red_probability':.8}, 'Standard informed host: switch succeeds iff first choice wrong (2/3). Probability matching success=p^2+(1-p)^2; always choose more likely color gives p.')
    add('Q36','K03,K05','Assume uniform independent binary hash prefixes. A puzzle requires 8 leading binary zeros. Find expected trials. Then a fictional protocol block subsidy of 12 units undergoes three halvings; find the new subsidy (this is NOT a current Bitcoin reward).',
        {'expected_trials':2**8,'subsidy_units':12/2**3}, 'Success probability=2^-8, expected trials=256. Subsidy=12*(1/2)^3; existing balances do not halve.')

    # Independent checkpoints and financially meaningful invariants.
    ids={q['id']:q for q in out}
    assert isclose(ids['Q16']['answers']['cov_decimal_squared'],-.0007,abs_tol=1e-15)
    assert isclose(ids['Q18']['answers']['vol_decimal'],sqrt(.000404),abs_tol=1e-15)
    assert isclose(call,(q*cu+(1-q)*cd)/(1+r),abs_tol=1e-12)
    assert isclose(delta*su+cash*(1+r),cu,abs_tol=1e-12)
    assert isclose(delta*sd+cash*(1+r),cd,abs_tol=1e-12)
    assert isclose(af(.04,5),sum(1.04**-t for t in range(1,6)),rel_tol=1e-12)
    assert approx < exact
    assert isclose((.6*.3)**2+(.3*sqrt(1-.6**2))**2,.3**2,abs_tol=1e-15)
    return out


if __name__ == '__main__':
    print(len(bank()), 'numerical items checked')
