import math

def determine_initial_approximation(f, deriv_f, a, b):
	# проверяем, для какого конца отрезка выполняется условие Фурье
	if f(a) * deriv_f(a, n=2) > 0:
		return a
	return b

def determine_x1(x0, f, deriv_f):
	# на основе классического метода Ньютона определеляем значение x1
	x1 = x0 - f(x0) / deriv_f(x0)
	return x1

def secant_method(f, deriv_f, a, b, presision):
	x0 = determine_initial_approximation(f, deriv_f, a, b)
	x1 = determine_x1(x0, f, deriv_f)

	prev = x0
	cur = x1

	print ("values at start are: ", x0, " and " x1)

	while math.fabs(cur - prev) > presision:
		new = cur - f(cur) * (prev - cur) / (f(prev) - f(cur))
		print("calculated new value:", new)
		prev = cur
		cur = new

	return cur
	