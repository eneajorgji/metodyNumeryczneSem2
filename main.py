import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return x ** 3


def rectangle_method(f, a, b, step):
    period = int((b - a) / step)
    x = np.linspace(a + step / 2, b - step / 2, period)
    return step * np.sum(f(x))


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
    plt.axhline(a, b, color='r')
    x_mid = (x[:-1] + x[1:]) / 2  # Midpoints
    y_mid = f(x_mid)
    plt.plot(a, b)
    # plt.plot(x_mid, y_mid, 'b.')
    plt.bar(x_mid, y_mid, width=(b - a) / period, facecolor='None', edgecolor='r', linewidth=1)
    plt.title(f"Rectangle Method = {period}")

    plt.grid(True, ls='--')
    plt.show()
    return fig


# print(midpoint(f, 0, 2, 0.5))
# print("20 przedzialow =>", midpoint_1(f, 0, 2, 20))
print("this is rectangle method =>", rectangle_method(f, 0, 2, 0.003))
print("this is rectangle method =>", rectangle_method_vis(f, 0, 2, 0.2))
# print("This is the last rectangle rule =>", rectangle_rule(f, 0, 2, 20))
