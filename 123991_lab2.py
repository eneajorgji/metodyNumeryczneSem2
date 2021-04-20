import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import scipy.integrate as integrate


########################################
# Zadanie 1

def f(x):
    return x ** 3


def rectangle_method(f, a, b, step):
    period = int((b - a) / step)
    x = np.linspace(a + step / 2, b - step / 2, period)
    integral = step * np.sum(f(x))
    return integral


print("Zadanie 1 =>", rectangle_method(f, 0, 2, 0.5))


########################################
# Zadanie 1 + wizualizacja

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
    x_mid = (x[:-1] + x[1:]) / 2
    y_mid = f(x_mid)
    plt.plot(a, b)
    plt.bar(x_mid, y_mid, width=(b - a) / period, facecolor='None', edgecolor='r', linewidth=1)
    plt.title(f"Rectangle Method step = {step}")

    plt.grid(True, ls='--')
    plt.show()
    return fig


print(rectangle_method_vis(f, 0, 2, 0.5))


########################################
# Zadanie 2

def trapezoidal_method(f, a, b, step):
    period = int((b - a) / step)
    x = np.linspace(a, b, period + 1)
    y = f(x)
    y_right = y[1:]
    y_left = y[:-1]
    dx = (b - a) / period
    integral = (dx / 2) * sum(y_right + y_left)
    return integral


########################################
# Zadanie 2 + wizualizacja

def trapezoidal_method_vis(f, a, b, step):
    fig = plt.figure()
    plt.axvline(a, color='r', ls='--')
    plt.axvline(b, color='r', ls='--')

    period = int((b - a) / step)
    x = np.linspace(a, b, period + 1)
    y = f(x)

    n = 10
    X = np.linspace(a, b, n * period)
    Y = f(X)

    plt.plot(X, Y)

    for i in range(period):
        xs = [x[i], x[i], x[i + 1], x[i + 1]]
        ys = [0, f(x[i]), f(x[i + 1]), 0]
        plt.fill(xs, ys, edgecolor='r', fill=None, linewidth=1)

    plt.grid(True, ls='--')
    plt.show()

    return fig


print("Zadanie 2 =>", trapezoidal_method(f, 0, 2, 0.1))
print("Trapezoidal method VISUALIZATION", trapezoidal_method_vis(f, 0, 2, 0.5))

# ------------------------#
