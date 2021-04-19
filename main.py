import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return x ** 3


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


print("Trapezoidal method =>", trapezoidal_method(f, 0, 2, 0.1))
print("Trapezoidal method VISUALIZATION", trapezoidal_method_vis(f, 0, 2, 0.5))
