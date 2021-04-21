import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 3


def monte_carlo(f, a, b, shots, step):
    x = np.arange(a, b + step, step)
    y = f(x)
    f_max = max(y)

    x_rand = a + np.random.random(shots) * (b - a)
    y_rand = 0 + np.random.random(shots) * f_max

    ind_below = np.where(y_rand < f(x_rand))
    ind_above = np.where(y_rand >= f(x_rand))

    return f_max * (b - a) * len(ind_below[0]) / shots


print(monte_carlo(f, 0, 2, 10000, 0.1))


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


print("Zadanie 3 Wizualizacja =>", monte_carlo_vis(f, 0, 2, 100, 0.01))
