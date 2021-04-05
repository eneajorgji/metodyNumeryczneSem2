import inline as inline
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f2(x):
    return (x - 2) ** 2 - 1


def dfdx(x):
    h = 10 ** -7
    return float(f2(x + h) - f2(x)) / h


def newton(f, x0, eps=10 ** -4, max_iter=100):
    count_iters = 0

    while abs(f(x0)) > eps and count_iters < max_iter:
        count_iters += 1

        if count_iters >= max_iter:
            None
        else:
            x1 = x0 - float(f(x0)) / dfdx(x0)
            x0 = x1

    return x1


print(newton(f2, 4))


#########################################
# Zadanie 3 + wizualizacje

def newton_vis(f, x0, eps=10 ** -4, max_iter=100):
    count_iters = 0
    x1_values = [x0]

    while abs(f(x0)) > eps and count_iters < max_iter:
        count_iters += 1

        if count_iters >= max_iter:
            None
        else:
            x1 = x0 - float(f(x0)) / dfdx(x0)
            x0 = x1

        x1_values.append(x1)

    interval_left = 2
    interval_right = 6

    x = np.linspace(interval_left, interval_right, 100)
    plt.figure()
    plt.plot(x, f(x))

    for i in x1_values:
        plt.plot(i, f(i), c="r", marker="o", markersize=5)

        tanget_y = dfdx(i) * x + f(i) - dfdx(i) * i
        plt.plot(x, tanget_y, c="r", ls="--")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("x = 3.000000046476302")
    plt.grid(True)
    plt.show()

    return x1


print(newton_vis(f2, 4))
