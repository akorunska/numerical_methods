from matrix import Matrix
from read_matrix import read_matrix
from gaussian_elimination import gaussian_elimination
from LU_main_diagonal_of_ones_on_U import LU_main_diagonal_of_ones_on_U
from LU_main_diagonal_of_ones_on_L import LU_main_diagonal_of_ones_on_L
from tomas_algorithm import tomas_algorithm


def LU_main_diagonal_of_ones_on_L_demo():
	m = read_matrix("matrixes/1.txt")
	print("Initial matrix: ", m)
	res, inv_matrix, det = LU_main_diagonal_of_ones_on_L(m)
	print("result is: \n", res)
	print("\ninverce matrix based on LU factorisation: ", inv_matrix.get_precise_to_str())
	print("A * A^(-1) = ", m.mult(inv_matrix))
	print("det(A) = ", det)

def gaussian_elimination_demo():
	m = read_matrix("matrixes/2.txt")
	print("Initial matrix: ", m)
	res= gaussian_elimination(m, choose_by_column_mode=True)
	print("result is: \n", res)


def LU_main_diagonal_of_ones_on_U_demo():
	m = read_matrix("matrixes/3.txt")
	print("Initial matrix: ", m)
	res, inv_matrix, det = LU_main_diagonal_of_ones_on_U(m)
	print("result is: \n", res)
	print("\ninverce matrix based on LU factorisation: ", inv_matrix.get_precise_to_str())
	print("A * A^(-1) = ", m.mult(inv_matrix))
	print("det(A) = ", det)


def tomas_algorithm_demo(): # метод прогонки
	m = read_matrix("matrixes/3.txt")
	print("Initial matrix: ", m)
	res = tomas_algorithm(m)
	print("\nresult is: \n", res)



# SLE 1
# LU_main_diagonal_of_ones_on_L_demo()


# SLE 2
# gaussian_elimination_demo()


# SLE 3
# LU_main_diagonal_of_ones_on_U_demo()
tomas_algorithm_demo()