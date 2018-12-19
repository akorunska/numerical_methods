from matrix import Matrix
from read_matrix import read_matrix
from gaussian_elimination import gaussian_elimination


def gaussian_elimination_demo():
	m = read_matrix("matrixes/2.txt")
	res = gaussian_elimination(m, choose_by_column_mode=True)
	print("result is: \n", res)


gaussian_elimination_demo()



# print(Matrix(2, [[2, 3], [8, 1]], [2, 3], extended=False))
