import numpy as np


def X_acc_linalg_solve(A, b):
    return np.linalg.solve(A, b)


def jacobi_method(A, b, iter_limit=100, x=None):
    if x is None:
        x = np.zeros(len(A[0]))

    diagonal = np.diag(A)
    R = A - np.diagflat(diagonal)

    for i in range(iter_limit):
        x = (b - np.dot(R, x)) / diagonal
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
    print("def jacobi_method", result_1)
    result_2 = X_acc_linalg_solve(A, b)
    print("Rozwiazanie z Linalg.solve", result_2)
