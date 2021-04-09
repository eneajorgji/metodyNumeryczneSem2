from math import *

x = 10
for iteration in range(1, 101):
    x_new = x - (x ** 2 + cos(x) ** 2 - 4 * x) / (2 * (x - cos(x) * sin(x) - 2))
    if abs(x_new - x) < 0.000001:
        break
    x = x_new

print(x_new)
