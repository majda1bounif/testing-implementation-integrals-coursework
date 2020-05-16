import numpy as np


def derivative_Integral(f, a, method='central', h=0.01):  # default Value
    if method == 'central':
        return (f(a + h) - f(a - h)) / (2 * h)
    elif method == 'forward':
        return (f(a + h) - f(a)) / h
    elif method == 'backward':
        return (f(a) - f(a - h)) / h
    else:
        raise ValueError
    #if f == int or f == int:
        #raise TypeError


def Integration_Method_trapezoidal(f, a, b, n):
    h = float(b - a) / n
    S = 0.5 * f(a) + 0.5 * f(b)
    for i in range(1, n):
        S += f(a + i * h)
    S *= h
    return S


def Integration_Method_trapezoidal_vectorized(f, a, b, n):
    h = float(b - a) / n
    x = np.linspace(a, b, n + 1)
    s = sum(f(x)) - 0.5 * f(a)-0.5
    return h*s
