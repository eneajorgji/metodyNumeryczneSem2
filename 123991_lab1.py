import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


#########################################
# Zadanie 1
#########################################

def f(x):
    return (x - 2) ** 3 - x ** 2 + 2 * x


def bisection_method(f, a, b, eps=10 ** -6, max_iter=100):
    c = (a + b) / 2.0
    count_iters = 0
    x_value = [a, b]

    while (b - a) / 2.0 > eps and count_iters < max_iter:
        count_iters += 1

        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        elif f(a) * f(c) > + 0:
            a = c
        else:
            None

        c = (a + b) / 2.0
        x_value.append(c)

    # print(x_value)
    return c


print(bisection_method(f, 1.5, 3, eps=10 ** -6))


#########################################
# Zadanie 1 + wizualizacja

def bisection_method_vis(f, a, b, eps=10 ** -4, max_iter=100):
    c = (a + b) / 2.0
    count_iters = 0
    x_value = [a, b]

    while (b - a) / 2.0 > eps and count_iters < max_iter:
        count_iters += 1

        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        elif f(a) * f(c) > + 0:
            a = c
        else:
            None
        c = (a + b) / 2.0
        x_value.append(c)

    # print(x_value)

    x = np.linspace(1.5, 3, 100)
    plt.plot(x, f(x))

    for i in x_value:
        plt.axvline(i, c="r", ls="--")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("x = 2.000000238418579")
    plt.grid(True)
    plt.show()
    return c


print(bisection_method_vis(f, 1.5, 3, eps=10 ** -6))


#########################################
# Zadanie 2
#########################################

def f2(x):
    return (x - 2) ** 2 - 1


def golden_section(f, a, b, eps=10 ** -4, max_iter=100):
    k = (5 ** 0.5 - 1) / 2

    count_iters = 0

    while abs(b - a) > eps and count_iters < max_iter:
        count_iters += 1

        x_left = b - (b - a) * k
        x_right = a + (b - a) * k

        if f(x_left) < f(x_right):
            b = x_right
        elif f(x_left) > f(x_right):
            a = x_left
        else:
            None

        c = (x_left + x_right) / 2

    return c


print(golden_section(f2, 0, 5))


#########################################
# Zadanie 2 + wizualizacje

def golden_section_vis(f, a, b, eps=10 ** -4, max_iter=100):
    k = (5 ** 0.5 - 1) / 2
    count_iters = 0
    x_value = [a, b]

    while abs(b - a) > eps and count_iters < max_iter:
        count_iters += 1

        x_left = b - (b - a) * k
        x_right = a + (b - a) * k

        if f(x_left) < f(x_right):
            b = x_right
        elif f(x_left) > f(x_right):
            a = x_left
        else:
            None

        c = (x_left + x_right) / 2
        x_value.append(c)

    x = np.linspace(0, 5, 100)
    plt.plot(x, f(x))

    for i in x_value:
        plt.axvline(i, c="r", ls="--")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("x = 2.0000019054494933")
    plt.grid(True)
    plt.show()

    return c


print(golden_section_vis(f2, 0, 5))


#########################################
# Zadanie 3
#########################################


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
