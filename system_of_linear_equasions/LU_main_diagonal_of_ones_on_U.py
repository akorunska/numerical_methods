from matrix import Matrix


def getLU(matrix):
	L = Matrix(matrix.n)
	U = Matrix(matrix.n, extended=True)
	p = 0
	while p < matrix.n:
		j = p
		i = j
		while i < matrix.n:
			L.values[i][j] = matrix.values[i][j]
			k = 0
			while k < j:
				L.values[i][j] -= U.values[k][j] * L.values[i][k]
				k += 1
			i += 1

		i = p
		j = i
		while j < matrix.n + 1:
			U.values[i][j] = matrix.values[i][j]
			k = 0
			while k < i:
				U.values[i][j] -= U.values[k][j] * L.values[i][k]
				k += 1
			U.values[i][j] /= L.values[i][i]
			j += 1

		p += 1
	return (L, U)


def get_result(L, U):
	n = L.n
	x = [0 for x in range(n)]
	i = n - 1
	while i >= 0:
		x[i] = U.values[i][n]
		k = i + 1
		while k < n:
			x[i] -= U.values[i][k] * x[k]
			k += 1
		i -= 1
	return x


def cron(i, j):
	if i == j:
		return 1
	return 0


def get_inverse_matrix(L, U):
	X = Matrix(L.n)
	p = L.n - 1
	while p >= 0:
		i = p
		j = i
		while j >= 0:
			X.values[i][j] = cron(i, j)
			k = j + 1
			while k < L.n:
				X.values[i][j] -= L.values[k][j] * X.values[i][k]
				k += 1
			X.values[i][j] /= L.values[j][j]
			j -= 1
		j = p
		i = j - 1
		while i >= 0:
			k = i + 1
			while k < L.n:
				X.values[i][j] -= U.values[i][k] * X.values[k][j]
				k += 1
			i -= 1
		p -= 1
	return X


def get_determinant(L):
	det = 1;
	for i in range(L.n):
		det *= L.values[i][i]
	return det


def LU_main_diagonal_of_ones_on_U(matrix):
	(L, U) = getLU(matrix)
	print("L: ", L)
	print("U: ", U) 

	init = L.mult(U)
	print("L * U = ", init)

	ans = get_result(L, U)
	inv_matrix = get_inverse_matrix(L, U)
	det = get_determinant(L)
	return ans, inv_matrix, det

