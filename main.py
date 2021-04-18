import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return x ** 3


def midpoint_1(f, a, b, n):
    h = float(b - a) / n
    x = np.linspace(a + h / 2, b - h / 2, n)
    plt.plot(x, f(x))
    plt.show()
    return h * np.sum(f(x))


def rectangle_method(f, a, b, step):
    period = int((b - a) / step)
    x = np.linspace(a + step / 2, b - step / 2, period)
    return step * np.sum(f(x))


def rectangle_method_vis(f, a, b, step):
    # fig = plt.figure()

    period = int((b - a) / step)
    x = np.linspace(a + step / 2, b - step / 2, period)

    plt.axvline(a, ls='--', color='red')
    plt.axvline(b, ls='--', color='red')

    plt.plot(x, f(x))
    plt.grid(True, ls='--')
    plt.show()

    return step * np.sum(f(x))


# print(midpoint(f, 0, 2, 0.5))
# print("20 przedzialow =>", midpoint_1(f, 0, 2, 20))
print("this is rectangle method =>", rectangle_method(f, 0, 2, 0.003))
print("this is rectangle method =>", rectangle_method_vis(f, 0, 2, 0.003))
# print("This is the last rectangle rule =>", rectangle_rule(f, 0, 2, 20))
