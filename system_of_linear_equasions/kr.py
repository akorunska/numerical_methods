from read_matrix import read_matrix
from RQ_decomposition import RQ_decomposition
from gaussian_elimination import gaussian_elimination


m = read_matrix("matrixes/kr_1.txt")
print("Initial matrix: ", m)

# QL_decomposition(m)

res = RQ_decomposition(m)
print("result is: \n", res)