import numpy as np


def x_acc_linalg_solve(A, b):
    return np.linalg.solve(A, b)


def jacobi_method(A, b, iter_limit=100, x=None):
    if x is None:
        x = np.zeros(len(A[0]))

    diagonal = np.diag(A)
    left_and_right = A - np.diagflat(diagonal)
    # print("This is R =>", R)

    for i in range(iter_limit):
        x = (1 / diagonal) * (b - np.dot(left_and_right, x))
    return x


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
    print("Jacobi Method", result_1)
    result_2 = x_acc_linalg_solve(A, b)
    print("Result from Linalg.solve", result_2)
