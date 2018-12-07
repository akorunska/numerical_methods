import sys
from parse_options import *
from equasions import *
from secant_method import secant_method
from simplified_newtons_method import simplified_newtons_method
from fixed_point_iteration_method import fixed_point_iteration_method

# method_names = ['secant', 'simplified_newtons', 'fpi', 'lobachesky']
# equasions_avaliable = [5, 34]

def get_method_function(options):
	if options['method_name'] == 'secant':
		return secant_method
	if options['method_name'] == 'simplified_newtons':
		return simplified_newtons_method
	if options['method_name'] == 'fpi':
		return fixed_point_iteration_method

def get_equasion_functions(options):
	if options['equasion_num'] == 5:
		return (equasion_5_as_fucntion, function_5_derivative, minus_function_5_derivative)
	if options['equasion_num'] == 34:
		return (equasion_34_as_function, function_34_derivative, minus_function_5_derivative)


options = parse_and_validate_options(sys.argv[1:])
print(options)

if options['method_name'] == 'lobachevsky':
	print("using 'lobachevsky' method to solve the equasion")
else:
	method = get_method_function(options)
	f, df, dminus_f = get_equasion_functions(options)
	a = options['a']
	b = options['b']
	precision = 10 ** -7

	print("trying to use", options['method_name'],
		"method to find solution of equasion number", options['equasion_num'],
		"in [ ", a, ", ", b, " ]\n\n")

	result = method(f, df, a, b, precision)
	print("result =", result)
	
