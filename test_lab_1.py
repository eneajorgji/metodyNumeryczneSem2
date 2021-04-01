import numpy as np
import matplotlib.pyplot as plt


# Zadanie 2

def f2(x):
    return (x - 2) ** 2 - 1


def golden_section(f, a, b, eps=10 ** -4, max_iter=100):
    k = (5 ** .5 - 1) / 2

    x_left = b - (b - a) * k
    x_right = a + (b - a) * k

    number_iter = 0

    while (b - a) > eps:
        if f2(x_left < f2(x_right)):
            b = x_right
            x_right = x_left
            x_left = b - (b - a) * k


        else:
            a = x_left
            x_left = x_right
            x_right = a + (b - a) * k

    return (a + b) / 2


answer = golden_section(f2, 0, 5)

print(answer)
