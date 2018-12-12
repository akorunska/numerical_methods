import math

def quadr(n, a):
	b = []
	i = 0

	while i <= n:
		b.append(a[i] ** 2)
		j = 1
		added_val = 0
		while j <= n - i:
			if (i - j >= 0):
				added_val += ((-1)**j) * a[i - j] * a[i + j]
			j += 1
		b[i] += 2  * added_val
		i += 1
	return b

def norm_dist(n, a, b):
	dist = 0
	i = 0

	while i < n:
		dist += (1 - b[i] / (a[i] ** 2)) ** 2
		i += 1
	return math.sqrt(dist)


def get_results(n, b, p, f):
	x = []
	i = 1

	while (i <= n):
		val = (b[n - i] / b[n - i + 1]) ** (1 / 2**p)
		f_x = f(val)
		f_mx = f(-val)
		x.append(val if (math.fabs(f_x) < math.fabs(f_mx)) else -val)
		i += 1
	return x

# n учитывает индексацию с 0
def lobachevsky_method(n, a, f):
	b = quadr(n, a)
	p = 1

	while (norm_dist(n, a, b) > 0.6):
		print (a, "  =>  ", b, "\n\n")
		a = b
		b = quadr(n, a)
		p += 1

	return get_results(n, b, p, f)