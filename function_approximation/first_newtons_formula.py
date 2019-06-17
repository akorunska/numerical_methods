from sympy import Symbol, simplify, lambdify, expand
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
import operator


control_points = [
    8.420, 8.677, 10.250, 11.213,
    11.288, 11.942, 12.288, 12.463,
    12.834, 12.913, 14.207, 16.404,
    16.639, 16.942, 18.683, 18.795,
    19.071,
]

def f(x):
    return np.log(x**3) + np.cos(x) + x

x_values=np.linspace(6, 20, len(control_points))
y_values = np.array(list(map(f, x_values)))


def Newton(x, x_values, y_values):
    n=len(x_values)
    f=np.zeros((n,n))
    f[:,0]=y_values
    for i in range(n-1,0,-1):
        for j in range(0,i):
            f[n-i+j,n-i]=(f[n-i+j,n-i-1]-f[n-i+j-1,n-i-1])/(x_values[n-i+j]-x_values[j])
    P=0
    for i in range(0,n):
        a=f[i,i]
        for j in range(0,i):
            a=a*(x-x_values[j])
        P=P+a
    return P


print("f(x) = ln(x^3) + cos(x) + x")
print(y_values)

x=Symbol('X')
P=Newton(x,x_values,y_values)
print('The interpolating polynomial is:', expand(P))

x_approx = np.array(control_points)
y_approx = lambdify(x, P)(x_approx)

fig, ax = plt.subplots()
ax.plot(x_approx, y_approx)
ax.scatter(x_values, y_values, c = 'r')
plt.show()