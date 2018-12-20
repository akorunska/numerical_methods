from matrix import Matrix
import math

def sign(val):
	if val >= 0:
		return 1
	return -1

def build_householder_matrix(w):
	w_t = w.transpose()
	K = w.mult(w_t)
	K.mult_by_val(2)
	I = Matrix.get_unit_matrix(K.n)
	return I.minus(K)


def LQ_decomposition(m):
	beta = [0 for x in range(m.n - 1)]
	mu = [0 for x in range(m.n - 1)]
	A = [0 for x in range(m.n)]
	A[0] = m
	Q = 0

	for i in range(m.n - 1):
		prev = A[i]

		row_sq_sum = 0
		for k in range(i, m.n):
			row_sq_sum += prev.values[i][k] ** 2
		beta[i] = sign(-prev.values[i][i]) * math.sqrt(row_sq_sum)

		mu[i] = 1 / (math.sqrt((2 * beta[i] ** 2) - 2 * beta[i] * prev.values[i][i]))
		w_values = [[0] for k in range(m.n)]
		w_values[i] = [mu[i] * (prev.values[i][i] - beta[i])]
		for k in range(i + 1, m.n):
			w_values[k] = [mu[i] * prev.values[i][k]]
		w = Matrix(n=1, m=m.n, values=w_values)
		H = build_householder_matrix(w)

		A[i + 1] = prev.mult(H)
		print(A[i + 1])
	print("thats all folks")

