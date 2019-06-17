import math
import numpy
from Integral import Integral


def trapezoid_formula(integral, n):
    h = (integral.b - integral.a) / n
    y = [integral.f(val) for val in numpy.arange(integral.a, integral.b + h, h)]
    return h * ((y[0] + y[-1])/2 + sum(y[1:-1]))


if __name__=="__main__":
    n = 55509
    result = trapezoid_formula(Integral(), n)
    print("I = ", result)
