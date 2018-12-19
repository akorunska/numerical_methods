from matrix import Matrix


def read_matrix(filename):
	values = []
	r = []

	f = open(filename, 'r')
	lines = [line for line in f]
	n = int(lines[0])
	i = 0
	while i < n:
		values.append([int(num) for num in lines[i + 1].split(' ')])
		i += 1
	i = 0
	while i < n:
		r.append(int(lines[ i + n + 1]))
		i += 1
	f.close()
	return Matrix(n, values, r, extended=True)