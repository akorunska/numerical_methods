from matrix import Matrix


def LU_main_diagonal_of_ones_on_U(matrix):
	L = Matrix(matrix.n)
	U = Matrix(matrix.n, extended=True)
	p = 0
	while p < matrix.n:
		j = p

		i = j
		while i < matrix.n:
			print("L: %i %i" % (i, j))
			L.values[i][j] = matrix.values[i][j]
			print("l[%i][%i] = A[%i][%i] = %i" % (i, j, i, j, matrix.values[i][j]))
			k = 0
			while k < j - 1:
				L.values[i][j] -= U.values[k][j] * L.values[i][k]
				k += 1
			i += 1
		print("L: ", L)

		i = p
		j = i
		while j < matrix.n + 1:
			print("U: %i %i" % (i, j))
			U.values[i][j] = matrix.values[i][j]
			k = 0
			while k < i - 1:
				U.values[i][j] -= U.values[k][j] * L.values[i][k]
				k += 1
			if (L.values[i][i] is not 0):
				U.values[i][j] /= L.values[i][i] # вся разница между факторизациями в этой строчке????
			j += 1
		print("U: ", U)

		p += 1
	print("L: ", L)
	print("U: ", U)