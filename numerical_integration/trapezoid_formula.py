import math
import numpy


def ctg(x):
    return math.cos(x) / math.sin(x)


def f(x):
    return (1 + math.sqrt(ctg(x)))/math.pow(math.sin(x), 2)


def trapezoid_formula(f, a, b, n):
    h = (b - a) / n
    y = [f(val) for val in numpy.arange(a, b + h, h)]
    print("h = %f" % h)
    print("y = ", y)
    I = h * ((y[0] + y[-1])/2 + sum(y[1:-1]))
    print("I = ", I)


def run_trapezoid_formula():
    n = 55509
    trapezoid_formula(f, 0.5, 1, n)


run_trapezoid_formula()
