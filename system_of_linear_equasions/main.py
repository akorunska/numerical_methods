from matrix import Matrix
from read_matrix import read_matrix
from gaussian_elimination import gaussian_elimination
from LU_main_diagonal_of_ones_on_U import LU_main_diagonal_of_ones_on_U


def gaussian_elimination_demo():
	m = read_matrix("matrixes/2.txt")
	res = gaussian_elimination(m, choose_by_column_mode=True)
	print("result is: \n", res)


def LU_main_diagonal_of_ones_on_U_demo():
	m = read_matrix("matrixes/1.txt")
	print("Initial matrix: ", m)

	res = LU_main_diagonal_of_ones_on_U(m)



# SLE 1


# SLE 2
# gaussian_elimination_demo()

# SLE 3
LU_main_diagonal_of_ones_on_U_demo()
