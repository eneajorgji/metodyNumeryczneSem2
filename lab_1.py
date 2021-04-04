import numpy as np
import matplotlib.pyplot as plt


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

    print(x_value)
    return c


print("Metoda Polowienia ", bisection_method(f, 1.5, 3, eps=10 ** -6))


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

    print(x_value)
    x = np.linspace(1.5, 3, 100)
    plt.plot(x, f(x))

    for i in x_value:
        plt.axvline(i, c="r", ls="--")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("x = 2.000000238418579")
    plt.show()
    return c


result = bisection_method_vis(f, 1.5, 3, eps=10 ** -6)
