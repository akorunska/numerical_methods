import math
from matrix import Matrix


def get_UtU(m):
	U = Matrix(n=m.n)
	for i in range(m.n):
		diag_sq = m.values[i][i]
		for k in range(i):
			diag_sq -= U.values[k][i] ** 2
		U.values[i][i] = math.sqrt(diag_sq)
		for j in range(i + 1, m.n):
			U.values[i][j] = m.values[i][j]
			for k in range(i):
				U.values[i][j] -= U.values[k][i] * U.values[k][j]
			U.values[i][j] /= U.values[i][i]
	return U, U.transpose()

def get_answer(m, U):
	y = [0 for x in range(m.n)]
	x = [0 for x in range(m.n)]

	for i in range(m.n):
		y[i] = m.r[i]
		for k in range(i):
			y[i] -= U.values[k][i] * y[k]
		y[i] /= U.values[i][i]

	for i in reversed(range(m.n)):
		x[i] = y[i]
		for k in range(i + 1, m.n):
			x[i] -= U.values[i][k] * x[k]
		x[i] /= U.values[i][i]
	return x


def holetsky_method(m):
	U, U_transp = get_UtU(m)
	print("U = ", U)
	print("U^T = ", U_transp)
	print("U^T * U = ", U_transp.mult(U))
	return get_answer(m, U)