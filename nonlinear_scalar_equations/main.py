import sys
from parse_options import *
from equasions import *
from secant_method import secant_method
from simplified_newtons_method import simplified_newtons_method

method_names = ['secant', 'simplified_newtons', 'sim', 'lobachesky']
equasions_avaliable = [5, 34]


options = parse_and_validate_options(sys.argv[1:])
print(options)

# a = 0
# b = 1
# precision = 10 ** (-7)

# result = simplified_newtons_method(
# 	equasion_5_as_fucntion, 
# 	function_5_derivative, 
# 	a, 
# 	b, 
# 	precision)

# print("result of solving equasion is: ", result)
