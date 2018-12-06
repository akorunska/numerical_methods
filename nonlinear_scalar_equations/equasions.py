import math
from scipy.misc import derivative

# e ^(sqrt(abs(x)) - cos(x)^2 + x^3 - sqrt(1 + cos(x))

def equasion_5_as_fucntion(x):
	value =  math.exp(math.sqrt(math.fabs(x))) - (math.cos(x) ** 2) \
	+ (x ** 3) - math.sqrt(1 + math.cos(x))
	return value

def function_5_derivative(x, n=1):
	return derivative(equasion_5_as_fucntion, x, dx=1e-6, n=n)

def equasion_34_as_function(x):
	value = (x ** 2) * math.sin(x) * math.cos(x) + math.pi - x
	return value

def function_34_derivative(x, n=1):
	return derivative(equasion_34_as_function, x, dx=1e-6, n=n)

