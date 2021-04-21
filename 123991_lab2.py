import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy import optimize
import scipy.integrate as integrate


########################################
# Zadanie 1

def f(x):
    return x ** 3
    # return np.sin(x)


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
    plt.axvline(a, color='red', linestyle='--')
    plt.axvline(b, color='red', linestyle='--')
    x_mid = (x[:-1] + x[1:]) / 2
    y_mid = f(x_mid)
    plt.plot(a, b)
    plt.bar(x_mid, y_mid, width=(b - a) / period, facecolor='None', edgecolor='red', linewidth=1)
    plt.title("Rectangle Method")

    plt.grid(True, linestyle='--')
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
    plt.axvline(a, color='red', linestyle='--')
    plt.axvline(b, color='red', linestyle='--')

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

    plt.grid(True, linestyle='--')
    plt.title("Trapezoidal method")
    plt.show()

    return fig


print("Zadanie 2 =>", trapezoidal_method(f, 0, 2, 0.1))
print(trapezoidal_method_vis(f, 0, 2, 0.5))


########################################
# Zadanie 3

def monte_carlo(f, a, b, shots, step):
    x = np.arange(a, b, step)
    y = f(x)
    f_max = max(y)

    x_rand = a + np.random.random(shots) * (b - a)
    y_rand = 0 + np.random.random(shots) * f_max

    ind_below = np.where(y_rand < f(x_rand))
    ind_above = np.where(y_rand >= f(x_rand))

    return f_max * (b - a) * len(ind_below[0]) / shots


print("Zadanie 3 =>", monte_carlo(f, 0, 2, 10000, 0.1))


########################################
# Zadanie 3 + wizualizacje

def monte_carlo_vis(f, a, b, shots, step):
    x = np.arange(a, b + step, step)
    y = f(x)
    f_max = max(y)

    x_rand = a + np.random.random(shots) * (b - a)
    y_rand = 0 + np.random.random(shots) * f_max

    ind_below = np.where(y_rand < f(x_rand))
    ind_above = np.where(y_rand >= f(x_rand))

    plt.plot(x, y, color='blue')
    plt.scatter(x_rand[ind_below], y_rand[ind_below], color='green')
    plt.scatter(x_rand[ind_above], y_rand[ind_above], color='red')

    plt.gca().add_patch(Rectangle((a, f(a)), b, f(b), linewidth=2, edgecolor='black', linestyle='--', facecolor='none'))

    plt.grid(True, linestyle='--')
    plt.title("Monte-Carlo")
    plt.show()

    return f_max * (b - a) * len(ind_below[0]) / shots


print(monte_carlo_vis(f, 0, 2, 100, 0.01))
