from matrix import Matrix

def c(m, i):
	return m.values[i][i]

def b(m, i):
	if i is 0:
		return 0
	return m.values[i][i - 1]

def d(m, i):
	if i is m.n:
		return 0
	return m.values[i][i + 1]

def tomas_algorithm(m):
	delta = [0 for i in range(m.n)]
	lambd = [0 for i in range(m.n)]

	for i in range(m.n):
		if i is 0:
			delta[i] = -d(m, i) / c(m, i)
			lambd[i] = m.r[i] / c(m, i)
		else:
			t = c(m, i) + b(m, i) * delta[i - 1]
			delta[i] = -d(m, i) / t
			lambd[i] = (m.r[i] - b(m, i) * lambd[i - 1]) / t
	print("lambda coeficients: \n", lambd)
	print("delta coeficients: \n", delta)
	x = [0 for i in range(m.n)]
	x[m.n - 1] = lambd[m.n - 1]
	for i in reversed(range(m.n - 1)):
		x[i] = delta[i] * x[i + 1] + lambd[i]
	return x

