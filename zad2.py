import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


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

# TODO: USUN t
print("golden", golden_section(f2, 0, 5))
print("golden vis", golden_section_vis(f2, 0, 5))
