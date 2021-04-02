import numpy as np
import matplotlib.pyplot as plt


# Zadanie 2
def f2(x):
    return (x - 2) ** 2 - 1


def golden_section(f, a, b, eps=10 ** -4, max_iter=100):
    k = (5 ** 0.5 - 1) / 2

    count_iters = 0
    # x_left = b - (b - a) * k
    # x_right = a + (b - a) * k

    while abs(b - a) > eps and count_iters < max_iter:
        count_iters += 1

        x_left = b - (b - a) * k
        x_right = a + (b - a) * k

        if f(x_left) < f(x_right):
            b = x_right
        else:
            a = x_left

        c = (x_left + x_right) / 2
        print(count_iters, c)

    return c


print(golden_section(f2, 0, 5))
