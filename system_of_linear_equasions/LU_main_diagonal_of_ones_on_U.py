from matrix import Matrix


def getLU(matrix):
	L = Matrix(matrix.n)
	U = Matrix(matrix.n, extended=True)
	p = 0
	while p < matrix.n:
		j = p

		i = j
		while i < matrix.n:
			# print(i, j)
			# print("l[%i][%i] = a[%i][%i] = %i" % (i, j, i, j, matrix.values[i][j]))
			L.values[i][j] = matrix.values[i][j]
			k = 0
			while k < j:
				L.values[i][j] -= U.values[k][j] * L.values[i][k]
				# print("l[%i][%i] -= u[%i][%i] * l[%i][%i] =  - %i * %i" % (i, j, k, j, i, k, U.values[k][j], L.values[i][k]))
				k += 1
			i += 1
			# print("L: ", L)

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
		# print("U: ", U)

		p += 1
	return (L, U)

def LU_main_diagonal_of_ones_on_U(matrix):
	(L, U) = getLU(matrix)
	print("L: ", L)
	print("U: ", U) 

	init = L.mult(U)
	print("L * U = ", init)