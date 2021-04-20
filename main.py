import random

import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return x ** 3


########################################
# Zadanie 3

def monte_carlo(f, a, b, shots, step):
    # fig = plt.figure()
    # x = np.arange(a, b, step)
    # y = f(x)
    # x_ramdom = np.random(shots)
    # y_ramdom = np.random(shots)
    #
    # shot_below = np.where(y_ramdom < f(x_ramdom))
    # shot_above = np.where(y_ramdom >= f(x_ramdom))
    #
    # chart_below = plt.scatter(x_ramdom[shot_below], y_ramdom[shot_below], color='red')
    # chart_above = plt.scatter(x_ramdom[shot_above], y_ramdom[shot_above], color='green')
    #
    # plt.plot(x, y, color='blue')
    # return fig

    count = 0
    for i in range(shots):
        x = random.random()
        y = random.random()
        if f(x) < 1:
            count += 1
        return 4.0 * count / shots


print("Zadanie 3 => ", monte_carlo(f, 0, 2, 10000, 0.1))

# 075408720749967
