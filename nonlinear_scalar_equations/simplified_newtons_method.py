import math

def determine_initial_approximation(f, deriv_f, a, b):
	# проверяем, для какого конца отрезка выполняется условие Фурье
	if f(a) * deriv_f(a, n=2) > 0:
		return a
	return b

def simplified_newtons_method (f, deriv_f, a, b, presision):
	x0 = determine_initial_approximation(f, deriv_f, a, b)
	# считаем это значение один раз и используем в каждой итерации
	x0_deriv = deriv_f(x0)

	print ("value at start is: x0 =", x0)
	print ("f`(x0) =", x0_deriv)

	cur = x0
	new = cur - f(cur) / x0_deriv
	while math.fabs(new - cur) > presision:
		cur = new
		new = cur - f(cur) / x0_deriv
		print("[x=", new)

	return new