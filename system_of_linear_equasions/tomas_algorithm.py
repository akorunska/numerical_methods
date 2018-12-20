import math
from matrix import Matrix
from LU_main_diagonal_of_ones_on_U import get_inverse_matrix

def c(m, i):
	return m.values[i][i]

def b(m, i):
	if i is 0:
		return 0
	return m.values[i][i - 1]

def d(m, i):
	if i is m.n - 1:
		return 0
	return m.values[i][i + 1]

def build_LU(m, t, delta):
	L = Matrix(m.n)
	U = Matrix(m.n)

	for i in range(m.n):
		L.values[i][i] = t[i]
		U.values[i][i] = 1
		if i is not 0:
			L.values[i][i - 1] = b(m, i)
		if i is not m.n - 1:
			U.values[i][i + 1] = -delta[i]
	print("L:", L)
	print("U:", U)
	return L, U

def build_inv_matrix(m, t, delta):
	L, U = build_LU(m, t, delta)
	return get_inverse_matrix(L, U)

def get_determinant(t):
	det = 1
	for i in range(len(t)):
		det *= t[i]
	return det

def diagonal_domination(m):
	for i in range(m.n):
		if math.fabs(c(m, i)) < math.fabs(b(m, i)) + math.fabs(d(m, i)):
			return False
	return True

def tomas_algorithm(m):
	if not diagonal_domination(m):
		print("computations below are likely to be incorrect thus matrix does not meet conditions of diagonal domination\n\n")
	else:
		print(" matrix meets conditions of diagonal domination, proceeding\n\n")

	delta = [0 for i in range(m.n)]
	lambd = [0 for i in range(m.n)]
	t = [0 for i in range(m.n)]

	for i in range(m.n):
		if i is 0:
			t[i] = c(m, i)
			delta[i] = -d(m, i) / t[i]
			lambd[i] = m.r[i] / t[i]
		else:
			t[i] = c(m, i) + b(m, i) * delta[i - 1]
			delta[i] = -d(m, i) / t[i]
			lambd[i] = (m.r[i] - b(m, i) * lambd[i - 1]) / t[i]
	print("lambda coeficients: \n", lambd)
	print("delta coeficients: \n", delta)

	x = [0 for i in range(m.n)]
	x[m.n - 1] = lambd[m.n - 1]
	for i in reversed(range(m.n - 1)):
		x[i] = delta[i] * x[i + 1] + lambd[i]

	inv_matr = build_inv_matrix(m, t, delta)
	det = get_determinant(t)

	return x, inv_matr, det

