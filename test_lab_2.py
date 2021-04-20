import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 3


def definite_integral(f, a, b, shots, step):
    """Approximate the definite integral of f(x)dx between x0 and x1 using
    N random points

    Arguments:
    f -- a function of one real variable, must be nonnegative on [x0, x1]
    N -- the number of random points to use


    """
    # First, let's compute fmax. We do that by evaluating f(x) on a grid
    # of points between x0 and x1
    # This assumes that f is generally smooth. If it's not, we're in trouble!
    x = np.arange(a, b, step)
    y = f(x)
    f_max = max(y)

    # Now, let's generate the random points. The x's should be between
    # x0 and x1, so we first create points beterrm 0 and (x1-x0), and
    # then add x0
    # The y's should be between 0 and fmax
    #
    #                  0...(x1-x0)
    x_rand = a + np.random.random(shots) * (b - a)
    y_rand = 0 + np.random.random(shots) * f_max

    # Now, let's find the indices of the poitns above and below
    # the curve. That is, for points below the curve, let's find
    #   i s.t. y_rand[i] < f(x_rand)[i]
    # And for points above the curve, find
    #   i s.t. y_rand[i] >= f(x_rand)[i]
    ind_below = np.where(y_rand < f(x_rand))
    ind_above = np.where(y_rand >= f(x_rand))

    # Finally, let's display the results
    # plt.plot(x, y, color="red")
    # plt.scatter(x_rand[ind_below], y_rand[ind_below], color="green")
    # plt.scatter(x_rand[ind_above], y_rand[ind_above], color="blue")
    # plt.legend((pts_below, pts_above),
    #            ('Pts below the curve', 'Pts above the curve'),
    #            loc='lower left',
    #            ncol=3,
    #            fontsize=8)

    # plt.show()

    print("Number of pts above the curve: ttttttttttttttttteeest", len(ind_above[0]))
    print("Number of pts below the curve:", len(ind_below[0]))
    print("N. below/N.total:", len(ind_below[0]) / shots)
    print("Rectangle area:", f_max * (b - a))
    print("Area under the curve:", f_max * (b - a) * len(ind_below[0]) / shots)


print(definite_integral(f, 0, 2, 10000, 0.1))


def definite_integral_show(f, a, b, shots, step):
    """Approximate the definite integral of f(x)dx between x0 and x1 using
    N random points

    Arguments:
    f -- a function of one real variable, must be nonnegative on [x0, x1]
    N -- the number of random points to use


    """
    # First, let's compute fmax. We do that by evaluating f(x) on a grid
    # of points between x0 and x1
    # This assumes that f is generally smooth. If it's not, we're in trouble!
    x = np.arange(a - 2, b + step, step)
    y = f(x)
    f_max = max(y)

    # Now, let's generate the random points. The x's should be between
    # x0 and x1, so we first create points beterrm 0 and (x1-x0), and
    # then add x0
    # The y's should be between 0 and fmax
    #
    #                  0...(x1-x0)
    x_rand = a + np.random.random(shots) * (b - a)
    y_rand = 0 + np.random.random(shots) * f_max

    # Now, let's find the indices of the poitns above and below
    # the curve. That is, for points below the curve, let's find
    #   i s.t. y_rand[i] < f(x_rand)[i]
    # And for points above the curve, find
    #   i s.t. y_rand[i] >= f(x_rand)[i]
    ind_below = np.where(y_rand < f(x_rand))
    ind_above = np.where(y_rand >= f(x_rand))

    # Finally, let's display the results
    plt.plot(x, y, color="red")
    plt.scatter(x_rand[ind_below], y_rand[ind_below], color="green")
    plt.scatter(x_rand[ind_above], y_rand[ind_above], color="red")
    # plt.legend((pts_below, pts_above),
    #            ('Pts below the curve', 'Pts above the curve'),
    #            loc='lower left',
    #            ncol=3,
    #            fontsize=8)

    plt.gca().add_patch(Rectangle((a, f(a)), b, f(b), linewidth=1, edgecolor='black', linestyle='--', facecolor='none'))
    plt.grid(True, linestyle='--')
    plt.show()

    print("Number of pts above the curve:", len(ind_above[0]))
    print("Number of pts below the curve:", len(ind_below[0]))
    print("N. below/N.total:", len(ind_below[0]) / shots)
    print("Rectangle area:", f_max * (b - a))
    print("Area under the curve:", f_max * (b - a) * len(ind_below[0]) / shots)


print(definite_integral_show(f, 0, 2, 100, 0.1))
