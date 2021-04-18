import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import scipy.integrate as integrate
from math import *


########################################
# Zadanie 1

def f(x):
    return x ** 3


def rectangle_method(f, a, b, step):
    # iterations = (b - a) / step
    integral = 0
    # for i in range(iterations):
    value_b_minus_a = 0
    while value_b_minus_a < b - a:
        value_b_minus_a += step
        integral += step * f(a + (value_b_minus_a))
    print("Integral is equal to: ", integral)
    return integral


print("Zadanie 1 =>", rectangle_method(f, 0, 2, 0.1))


def rectangle_method_vis(f, a, b, step):
    period = int((b - a) / step)
    x = np.linspace(a, b, period + 1)
    y = f(x)
    n = 10
    X = np.linspace(a, b, n * period + 1)
    Y = f(X)

    fig = plt.figure()

    plt.plot(X, Y)
    plt.axvline(a, color='r', ls='--')
    plt.axvline(b, color='r', ls='--')
    x_mid = (x[:-1] + x[1:]) / 2  # Midpoints
    y_mid = f(x_mid)
    plt.plot(a, b)
    # plt.plot(x_mid, y_mid, 'b.')
    plt.bar(x_mid, y_mid, width=(b - a) / period, facecolor='None', edgecolor='r', linewidth=1)
    plt.title(f"Rectangle Method step = {step}")

    plt.grid(True, ls='--')
    plt.show()
    return fig


print(rectangle_method_vis(f, 0, 10, 0.5))

########################################
# Zadanie 2

# def trapezoidal_method(f, a, b, step):
#     # def trapezoidal(f, a, b, n):
#     # print("this is h", h)
#     n = int((b - a) / step)
#     print(n)
#     h = float(b - a) / n
#
#     result = 0.5 * f(a) + 0.5 * f(b)
#     for i in range(1, n):
#         result += f(a + i * h)
#     result *= h
#     return result
#
#
# print("zadanie 2", trapezoidal_method(f, 0, 2, 0.001))
