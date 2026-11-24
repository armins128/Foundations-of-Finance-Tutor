"""Small, dependency-free calculator for verifying freshly generated FoF tasks.

Usage (JSON in, JSON out):
    python fof_calc.py npv '{"rate":0.06,"cfs":[-500,80,150,200,250]}'
    python fof_calc.py self-test

Every function uses the course conventions: annual compounding unless stated,
population (divide by n) statistics for return observations, Macaulay duration
in years and modified duration = Macaulay / (1 + y / m).
"""
from __future__ import annotations

import json
import math
import sys


# ---------- Value ----------
def npv(rate, cfs):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cfs))


def annuity_pv(c, rate, n):
    return c * (1 - (1 + rate) ** -n) / rate


def annuity_payment(pv, rate, n):
    """Equivalent annual cash flow (capital recovery factor)."""
    return pv * rate / (1 - (1 + rate) ** -n)


def growing_perpetuity_pv(c1, rate, g):
    if rate <= g:
        raise ValueError('rate must exceed growth')
    return c1 / (rate - g)


def irr(cfs, lo=-0.99, hi=10.0, tol=1e-12):
    """Bisection IRR; raises if NPV has no sign change in [lo, hi]."""
    f_lo, f_hi = npv(lo, cfs), npv(hi, cfs)
    if f_lo * f_hi > 0:
        raise ValueError('no sign change in bracket; IRR may not exist or be unique')
    for _ in range(300):
        mid = (lo + hi) / 2
        f_mid = npv(mid, cfs)
        if abs(f_mid) < tol:
            return mid
        if f_lo * f_mid < 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
    return (lo + hi) / 2


def sign_changes(cfs):
    signs = [c > 0 for c in cfs if c != 0]
    return sum(a != b for a, b in zip(signs, signs[1:]))


# ---------- Bonds ----------
def bond(face, coupon_rate, years, y, m=1):
    """Price, Macaulay and modified duration. y is the nominal annual yield with m payments."""
    n = round(years * m)
    c = face * coupon_rate / m
    flows = [(k / m, c + (face if k == n else 0)) for k in range(1, n + 1)]
    pvs = [(t, cf / (1 + y / m) ** (t * m)) for t, cf in flows]
    price = sum(p for _, p in pvs)
    mac = sum(t * p for t, p in pvs) / price
    return {'price': price, 'macaulay': mac, 'modified': mac / (1 + y / m)}


def immunize(d_a, d_b, d_liability):
    """Weights of two bonds whose weighted duration matches the liability."""
    w_a = (d_b - d_liability) / (d_b - d_a)
    return {'w_a': w_a, 'w_b': 1 - w_a}


# ---------- Portfolios / CAPM ----------
def stats(x):
    n = len(x)
    mu = sum(x) / n
    var = sum((v - mu) ** 2 for v in x) / n
    return {'mean': mu, 'var': var, 'sd': math.sqrt(var)}


def cov(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / len(x)


def two_asset(x, y):
    sx, sy, c = stats(x), stats(y), cov(x, y)
    w = (sy['var'] - c) / (sx['var'] + sy['var'] - 2 * c)
    mu = w * sx['mean'] + (1 - w) * sy['mean']
    var = w ** 2 * sx['var'] + (1 - w) ** 2 * sy['var'] + 2 * w * (1 - w) * c
    return {'cov': c, 'corr': c / (sx['sd'] * sy['sd']), 'w_mvp_x': w, 'w_mvp_y': 1 - w,
            'mu_mvp': mu, 'sd_mvp': math.sqrt(var)}


def capm(asset, market, rf):
    beta = cov(asset, market) / stats(market)['var']
    mu_m = stats(market)['mean']
    expected = rf + beta * (mu_m - rf)
    return {'beta': beta, 'capm_return': expected, 'alpha': stats(asset)['mean'] - expected,
            'w_market': beta, 'w_riskfree': 1 - beta}


# ---------- Derivatives ----------
def forward(spot, rf, t, income_pv=0.0):
    return (spot - income_pv) * (1 + rf) ** t


def parity_call(put, spot, strike, rf, t):
    return put + spot - strike / (1 + rf) ** t


def parity_put(call, spot, strike, rf, t):
    return call - spot + strike / (1 + rf) ** t


def binomial_one_period(spot, up, down, strike, rf, kind='call'):
    """up/down are gross factors (e.g. 1.2, 0.9). Returns replication and price."""
    su, sd = spot * up, spot * down
    pay = (lambda s: max(s - strike, 0)) if kind == 'call' else (lambda s: max(strike - s, 0))
    delta = (pay(su) - pay(sd)) / (su - sd)
    bond_pos = (pay(su) - delta * su) / (1 + rf)
    q = ((1 + rf) - down) / (up - down)
    return {'delta': delta, 'bond': bond_pos, 'price': delta * spot + bond_pos, 'q': q}


FUNCS = {f.__name__: f for f in (npv, annuity_pv, annuity_payment, growing_perpetuity_pv, irr,
                                   sign_changes, bond, immunize, stats, cov, two_asset, capm,
                                   forward, parity_call, parity_put, binomial_one_period)}


def r4(v):
    if isinstance(v, dict):
        return {k: r4(x) for k, x in v.items()}
    return round(v, 4) if isinstance(v, float) else v


def self_test():
    close = lambda a, b: abs(a - b) < 5e-5
    assert close(npv(0.10, [-100, 110]), 0)
    assert close(annuity_pv(100, 0.06, 3), 267.3012)
    assert close(annuity_payment(annuity_pv(100, 0.06, 3), 0.06, 3), 100)
    assert close(irr([-100, 60, 60]), 0.130662)
    assert sign_changes([-1, 2, -1, 2]) == 3
    b = bond(1000, 0.10, 3, 0.06)
    assert close(b['price'], 1106.9205) and close(b['macaulay'], 2.7491)
    z = bond(1000, 0.0, 2, 0.06)
    assert close(z['macaulay'], 2.0)
    w = immunize(1.0, 3.0, 2.0)
    assert close(w['w_a'], 0.5)
    t = two_asset([0.1, -0.1], [-0.1, 0.1])
    assert close(t['corr'], -1) and close(t['sd_mvp'], 0)
    c = capm([0.2, 0.0], [0.1, 0.0], 0.01)
    assert close(c['beta'], 2.0) and close(c['w_riskfree'], -1.0)
    assert close(forward(50, 0.05, 1), 52.5)
    call = parity_call(3, 50, 48, 0.05, 1)
    assert close(parity_put(call, 50, 48, 0.05, 1), 3)
    bi = binomial_one_period(100, 1.2, 0.9, 100, 0.05)
    assert close(bi['price'], bi['q'] * 20 / 1.05)
    print('PASS: fof_calc verification helpers')


def main(argv):
    if len(argv) < 2 or argv[1] in ('-h', '--help'):
        print(__doc__ + '\nFunctions: ' + ', '.join(sorted(FUNCS)))
        return
    if argv[1] == 'self-test':
        self_test()
        return
    args = json.loads(argv[2]) if len(argv) > 2 else {}
    result = FUNCS[argv[1]](**args)
    print(json.dumps({'exact': result, 'rounded_4dp': r4(result)}, indent=2))


if __name__ == '__main__':
    main(sys.argv)
