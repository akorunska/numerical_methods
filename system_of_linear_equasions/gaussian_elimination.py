import math


def choose_by_column(matrix, col_num):
	maximum = {'row': col_num, 'value': matrix.values[col_num][col_num]}

	i = col_num + 1
	while i < matrix.n:
		if math.fabs(matrix.values[i][col_num]) > math.fabs(maximum['value']):
			maximum['value'] = matrix.values[i][col_num]
			maximum['row'] = i
		i += 1
	matrix.values[col_num], matrix.values[maximum['row']] = matrix.values[maximum['row']], matrix.values[col_num]


def forward_pass(matrix, choose_by_column_mode):
	k = 0
	while k < matrix.n:
		next_matrix = matrix.get_copy()
		if (choose_by_column_mode):
			choose_by_column(matrix, k)
			print("rows were swapped to put biggest element on the diagonal:", matrix, "\n")
		j = k
		while j < matrix.n + 1:
			next_matrix.values[k][j] = matrix.values[k][j] / matrix.values[k][k]
			j += 1
		i = k + 1
		while i < matrix.n:
			j = k
			while j < matrix.n + 1:
				next_matrix.values[i][j] = matrix.values[i][j] - next_matrix.values[k][j] * matrix.values[i][k]
				j += 1
			i += 1
		k += 1
		matrix = next_matrix
		print("after iteration k =%i matrix looks like: \n" % i,  matrix, "\n")
	return matrix

def backward_pass(matrix):
	x = [0] * matrix.n
	i = matrix.n - 1
	while i >= 0:
		x[i] = matrix.values[i][matrix.n]
		j = i + 1
		while j < matrix.n:
			x[i] -= matrix.values[i][j] * x[j]
			j += 1
		i -= 1
	return x


def gaussian_elimination(matrix, choose_by_column_mode=False):
	print(matrix)
	triangle_matrix = forward_pass(matrix, choose_by_column_mode)
	return backward_pass(triangle_matrix)

