import numpy as np
import scipy as sci


def X_acc_linalg_solve(A, b):
    return np.linalg.solve(A, b)


def jacobi_method(A, b, iter_limit=10, x=None):
    # wyznacz macierze D
    diagonal = np.diagonal(A)

    # wyznacz marcierze D ** -1
    # inverse = np.linalg.inv(diagonal)
    # print(inverse)
    # wyznacz marcierze L and U
    # L_and_U = sci.linalg.lu(a)

    # return diagonal * (b - L_and_U * x)
    return diagonal


if __name__ == '__main__':
    A = np.array([[50, 2, 8, 4],
                  [6, 41, 7, 4, ],
                  [4, 9, 47, 10],
                  [2, 6, 6, 48]])
    b = np.array([68,
                  139,
                  115,
                  -16])
    x0 = np.array([1,
                   1,
                   1,
                   1])

    result_1 = jacobi_method(A, b, x=x0)
    print("def jacobi_method", result_1)



    result_2 = X_acc_linalg_solve(A, b)
    print("Rozwiazanie z Linalg.solve", result_2)
