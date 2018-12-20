from matrix import Matrix
from read_matrix import read_matrix
from gaussian_elimination import gaussian_elimination
from LU_main_diagonal_of_ones_on_U import LU_main_diagonal_of_ones_on_U
from LU_main_diagonal_of_ones_on_L import LU_main_diagonal_of_ones_on_L
from tomas_algorithm import tomas_algorithm
from LQ_decomposition import LQ_decomposition
from holetsky_method import holetsky_method


def get_demo(num):
	if num is 1:
		return LU_main_diagonal_of_ones_on_L_demo
	if num is 2:
		return LQ_decomposition_demo
	if num is 3:
		return holetsky_method_demo
	if num is 4:
		return gaussian_elimination_demo
	if num is 5:
		return tomas_algorithm_demo
	if num is 6:
		return LU_main_diagonal_of_ones_on_U_demo

## DEMOS FOR SLE 1	

def LU_main_diagonal_of_ones_on_L_demo():
	m = read_matrix("matrixes/1.txt")
	print("1: LU factorisation with main diagonal of ones on L: SLE #1\n\n")
	print("Initial matrix: ", m)

	res, inv_matrix, det = LU_main_diagonal_of_ones_on_L(m)
	print("result is: \n", res)
	print("\ninverce matrix based on LU factorisation: ", inv_matrix.get_precise_to_str())
	print("A * A^(-1) = ", m.mult(inv_matrix))
	print("det(A) = ", det)

def LQ_decomposition_demo(): # метод відбиття на основі LQ факторизації
	m = read_matrix("matrixes/1.txt")
	print("Initial matrix: ", m)
	print("2: LQ decomposition: SLE #1\n\n")

	res, det = LQ_decomposition(m)
	print("result is: \n", res)
	# print("\ninverce matrix based on LU factorisation: ", inv_matrix.get_precise_to_str())
	# print("A * A^(-1) = ", m.mult(inv_matrix))
	print("det(A) = +-", det)

##


## DEMOS FOR SLE 2

def holetsky_method_demo():
	m = read_matrix("matrixes/2.txt")
	print("Initial matrix: ", m)
	print("3: Holetsky method: SLE #2\n\n")

	res, det = holetsky_method(m)
	print("result is: \n", res)
	print("det(A) = ", det)

def gaussian_elimination_demo():
	m = read_matrix("matrixes/2.txt")
	print("Initial matrix: ", m)
	print("4: Gaussian elimination: SLE #2\n\n")

	res = gaussian_elimination(m, choose_by_column_mode=True)
	print("result is: \n", res)


##

## DEMOS FOR SLE 3

def tomas_algorithm_demo(): # метод прогонки
	m = read_matrix("matrixes/3.txt")
	print("Initial matrix: ", m)
	print("5: Tomas algorithm: SLE #3\n\n")

	res, inv_matrix, det = tomas_algorithm(m)
	print("\nresult is: \n", res)
	print("\ninverce matrix based on LU factorisation: ", inv_matrix.get_precise_to_str())
	print("A * A^(-1) = ", m.mult(inv_matrix))
	print("det(A) = ", det)

def LU_main_diagonal_of_ones_on_U_demo():
	m = read_matrix("matrixes/3.txt")
	print("Initial matrix: ", m)
	print("6: LU factorisation with main diagonal of ones on U: SLE #3\n\n")

	res, inv_matrix, det = LU_main_diagonal_of_ones_on_U(m)
	print("result is: \n", res)
	print("\ninverce matrix based on LU factorisation: ", inv_matrix.get_precise_to_str())
	print("A * A^(-1) = ", m.mult(inv_matrix))
	print("det(A) = ", det)

##