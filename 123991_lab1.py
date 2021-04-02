import numpy as np
import matplotlib.pyplot as plt


#########################################
# Zadanie 1

def f(x):
    return (x - 2) ** 3 - x ** 2 + 2 * x


def bisection_method(f, a, b, eps=10 ** -6, max_iter=100):
    c = (a + b) / 2.0
    count_iters = 0

    while (b - a) / 2.0 > eps and count_iters < max_iter:
        count_iters += 1

        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        # c = (a + b) / 2.0

        print(count_iters)

    return c


print(bisection_method(f, 1.5, 3, eps=10 ** -6))


#########################################
# Zadanie 1 + wizualizacja

def bisection_method_vis(f, a, b, eps=10 ** -4, max_iter=100):
    c = (a + b) / 2.0
    count_iters = 0

    while (b - a) / 2.0 > eps and count_iters < max_iter:
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        count_iters += 1
        # print(number_iter)

    return c


result = bisection_method(f, 1.5, 3, eps=10 ** -6)
# print(bisection_method_vis(f, 1.5, 3, eps=10 ** -6))
print(result)

x = np.linspace(1.5, 3, 100)
plt.plot(x, f(x))
plt.axvline(result)
plt.grid()
plt.show()


#########################################
# Zadanie 2
def f2(x):
    return (x - 2) ** 2 - 1


def golden_section(f, a, b, eps=10 ** -4, max_iter=100):
    k = (5 ** 0.5 - 1) / 2

    count_iters = 0
    # x_left = b - (b - a) * k
    # x_right = a + (b - a) * k

    while abs(b - a) > eps and count_iters < max_iter:
        count_iters += 1

        x_left = b - (b - a) * k
        x_right = a + (b - a) * k

        if f(x_left) < f(x_right):
            b = x_right
        else:
            a = x_left

        c = (x_left + x_right) / 2
        print(count_iters, c)

    return c


result = golden_section(f2, 0, 5)
print(golden_section(f2, 0, 5))

# TODO create def golden_section_vis(..)

x = np.linspace(0, 5, 100)
plt.plot(x, f2(x))
plt.axvline(result)
plt.grid()
plt.show()
