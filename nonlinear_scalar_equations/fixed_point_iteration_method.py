import math
import sys
from scipy.optimize import minimize_scalar

def get_func_mininum_in_bounds(f, a, b):
	res = minimize_scalar(f, bounds=(a, b), method='bounded')
	return res.fun

def get_func_maximum_in_bounds(f, a, b):
	res = minimize_scalar(lambda x: -f(x), bounds=(a, b), method='bounded')
	return -res.fun

def handle_q(q):
	if q >= 1 or q <= 0:
		print("value of q should be in (0; 1)")
		print("how about putting another bounds?")
		sys.exit(2)

def fixed_point_iteration_method(f, deriv_f, a, b, eps):
	alpha = get_func_mininum_in_bounds(deriv_f, a, b)
	gamma = get_func_maximum_in_bounds(deriv_f, a, b)
	print("alpha =", alpha, "  gamma =", gamma)

	if alpha < 0 and gamma < 0:
		print("alpha and gamma are both < 0\n")
		return "" # метод будет запущен для -f(x)

	lambd = 2 / (gamma + alpha)
	q = (gamma - alpha) / (gamma + alpha)

	print ("lambda =", lambd, ";  q =", q)

	handle_q(q)

	presision =  ((1 - q) / q) * eps
	print ("presision is found as (1 - q)/q * eps =", presision)

	prev = a
	cur = prev - lambd * f(prev)
	print("x0 =", prev)

	while math.fabs(cur - prev) >= presision:
		prev = cur
		print("received xk =", cur)
		cur = prev - lambd * f(prev)
	return cur

