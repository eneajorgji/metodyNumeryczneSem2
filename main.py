import numpy as np

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

diagonal = np.diagonal(A)
print(diagonal)
