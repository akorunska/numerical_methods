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
			U.values[i][j] /= L.values[i][i] # вся разница между факторизациями в этой строчке????
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

def LU_main_diagonal_of_ones_on_U(matrix):
	(L, U) = getLU(matrix)
	print("L: ", L)
	print("U: ", U) 

	init = L.mult(U)
	print("L * U = ", init)
	return get_result(L, U)

