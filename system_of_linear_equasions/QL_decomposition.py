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

def build_QL(m):
	beta = [0 for x in range(m.n - 1)]
	mu = [0 for x in range(m.n - 1)]
	A = [0 for x in range(m.n)]
	A[0] = m
	Q = 0

	for i in range(m.n - 1):
		n = m.n - 1
		prev = A[i]

		row_sq_sum = 0
		for k in range(n - i + 1):
			row_sq_sum += prev.values[k][n - i] ** 2
		beta[i] = sign(-prev.values[n - i][n - i]) * math.sqrt(row_sq_sum)

		mu[i] = 1 / (math.sqrt((2 * beta[i] ** 2) - 2 * beta[i] * prev.values[n - i][n - i]))

		w_values = [[0] for k in range(m.n)]

		for k in range(n - i + 1):
			w_values[k] = [mu[i] * prev.values[k][n - i]]
			if k is n - i:
				w_values[k] = [mu[i] * (prev.values[k][n - i] - beta[i])]

		w = Matrix(n=1, m=m.n, values=w_values)
		print(w_values)
		H = build_householder_matrix(w)
		print (H.get_precise_to_str())

		A[i + 1] = H.mult(A[i])
		if Q is 0:
			Q = H
		else:
			Q = H.mult(Q)
		print("A(%i):" % (i + 1), A[i + 1])
		# print("Q: ", Q)
	return A[i + 1], Q

def get_answer(m, L, Q_transp):
	y = [0 for i in range(L.m)]
	for i in range(L.m):
		y[i] = L.values[i][L.n - 1]
	x = [0 for i in range(L.m)]

	x[0] = y[0] / L.values[0][0]
	for i in range(1, m.n):
		x[i] = y[i]
		for k in range(i):
			x[i] -= L.values[i][k] * x[k]
		x[i] /= L.values[i][i]
	return x
	

# def get_determinant(L):
# 	det = 1;
# 	for i in range(L.n):
# 		det *= L.values[i][i]
# 	return det

def QL_decomposition(m):
	L, Q = build_QL(m)
	print("L: ", L, "Q: ", Q)
	print("Q^T * L = ", Q.transpose().mult(L))
	return get_answer(m, L, Q)
