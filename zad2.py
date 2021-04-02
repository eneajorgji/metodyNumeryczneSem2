import math

gr = (math.sqrt(5) + 1) / 2
print(gr)

def f(x):
    return (x - 2) ** 2 - 1


def gss(f, a, b, tol=10 ** -4):
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


ans = gss(f, 0, 5, )
print(ans)
