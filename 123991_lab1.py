import numpy as np
import matplotlib.pyplot as plt


# Zadanie 1

def f(x):
    return (x - 2) ** 3 - x ** 2 + 2 * x


def bisection_method(f, a, b, eps=10 ** -6, max_iter=100):
    c = (a + b) / 2.0
    number_iter = 0  # ile raz iteruje

    while (b - a) / 2.0 > eps and number_iter < max_iter:
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2.0

        number_iter += 1
        # print(number_iter)

    return c


print(bisection_method(f, 1.5, 3, eps=10 ** -6))


# Zadanie 1 + wizualizacja

def bisection_method_vis(f, a, b, eps=10 ** -4, max_iter=100):
    c = (a + b) / 2.0
    number_iter = 0  # ile raz iteruje

    while (b - a) / 2.0 > eps and number_iter < max_iter:
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        # c = (a + b) / 2.0

        number_iter += 1
        # print(number_iter)

    return c


answer = bisection_method_vis(f, 1.5, 3, eps=10 ** -6)
# print(bisection_method_vis(f, 1.5, 3, eps=10 ** -6))
print(answer)

x = np.linspace(1.5, 3, 100)
plt.plot(x, f(x))
plt.axvline(answer)
plt.grid()
plt.show()
