from sympy import Symbol, simplify, lambdify, expand
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
import operator

x_values = [
    -20.061, -18.460, -18.119, -17.455,
    -15.386, -13.808, -13.282, -11.270,
    -10.951, -10.280, -6.300, -4.606,
    -3.902, -3.656, -1.280, -0.228,
    -0.068, 1.428, 11.248, 12.692,
    13.094, 15.104, 18.180, 18.424,
    19.127, 19.942, 21.238,
]
y_values = [
    127.098, 96.514, 95.938, 98.498,
    93.513, 59.084, 48.788, 39.285,
    40.464, 41.970, 6.931, 7.561,
    7.902, 7.638, 0.178, -0.205,
    -0.066, 0.883, 44.985, 66.286,
    68.463, 63.612, 124.429, 129.921,
    140.341, 141.739, 134.857,
]
control_points = [
    -18.935, -18.803, -18.643, -13.345,
    -12.055, -9.187, -8.333, -5.474,
    -4.726, -2.364, 3.217, 17.228,
     19.033,
]


def interpolate_lagrange(x, x_values, y_values):
    def _basis(j):
        p = [(x - x_values[m])/(x_values[j] - x_values[m]) for m in range(k) if m != j]
        return reduce(operator.mul, p)
    assert len(x_values) != 0 and (len(x_values) == len(y_values)), 'x and y cannot be empty and must have the same length'
    k = len(x_values)
    return sum(_basis(j)*y_values[j] for j in range(k))


x = Symbol('x')
poly = simplify(interpolate_lagrange(x, x_values, y_values))
print(poly)
expand(poly)

x1 = np.array(control_points)
y1 = lambdify(x, poly)(x1)


fig, ax = plt.subplots()
ax.plot(x1, y1)
ax.scatter(x_values, y_values, c='r')
plt.show()
