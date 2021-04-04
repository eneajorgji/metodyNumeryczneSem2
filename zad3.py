import numpy as np
import matplotlib.pyplot as plt


def f3(x):
    return (x - 2) ** 2 - 1


def dxf(f3, x0):
    h = 10 ** -7
    return float(f3(x0 + h) - f3(x0)) / h


