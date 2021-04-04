import math
from scipy import optimize

gr = (math.sqrt(5) + 1) / 2


def f2(x):
    return (x - 2) ** 2 - 1


def gss(f, a, b, tol=10 ** -4):
    """Golden-section search
    to find the minimum of f on [a,b]
    f: a strictly unimodal function on [a,b]

    Example:
    >>> f = lambda x: (x-2)**2
    >>> x = gss(f, 1, 5)
    >>> print("%.15f" % x)
    2.000009644875678

    """
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    while abs(b - a) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c

        # We recompute both c and d here to avoid loss of precision which may lead to incorrect results or infinite loop
        c = b - (b - a) / gr
        d = a + (b - a) / gr

    return (b + a) / 2


print(gss(f2, 0, 5, ))
minimum = optimize.golden(f2, brack=(0, 5))
print(minimum)