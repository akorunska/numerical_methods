from equasions import *
from secant_method import secant_method

a = 0
b = 1
precision = 10 ** (-7)

result = secant_method(
	equasion_5_as_fucntion, 
	function_5_derivative, 
	a, 
	b, 
	precision)

print("result of solving equasion is: ", result)
