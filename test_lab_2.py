import numpy as np
from matplotlib import pyplot as plt

f = lambda x: x ** 3
a = 0
b = 2
N = 4
n = 10  # Use n*N+1 points to plot the function smoothly

x = np.linspace(a, b, N + 1)
y = f(x)
print(y)

X = np.linspace(a, b, n * N + 1)
Y = f(X)
print(Y)

plt.figure()

# plt.subplot(1, 3, 2)
plt.plot(X, Y)
x_mid = (x[:-1] + x[1:]) / 2  # Midpoints
y_mid = f(x_mid)
plt.plot(x_mid, y_mid, 'b.', markersize=10)
plt.bar(x_mid, y_mid, width=(b - a) / N, alpha=0.2, edgecolor='b')
plt.title('Midpoint Riemann Sum, N = {}'.format(N))

plt.show()
