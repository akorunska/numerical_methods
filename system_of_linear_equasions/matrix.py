import copy

class Matrix:
	def __init__(self, n=0, values=[], r=[], extended=False):
		self.n = n
		self.values = values

		if len(values) is  0 :
			self.values = [[0 for y in range(n)] for x in range(n)]

		self.extended = extended
		self.r = []
		if (extended):
			if (len(r) is 0):
				r = [0,] * n
			i = 0
			for num in r:
				self.values[i].append(num)
				i += 1

		if (len(r) is not 0):
			self.r = r


	def get_copy(self):
		return copy.deepcopy(self)

	def mult(self, m2):
		ans = Matrix(self.n) # ans is rows1 x cols2
		for i in range(self.n):
			for j in range(self.n):
				for k in range(self.n):
					ans.values[i][j] += self.values[i][k] * m2.values[k][j]
		return ans

	def get_precise_to_str(self):
		res = "\n"
		i = 0
		for line in self.values:
			j = 0
			for num in line:
				if j < self.n:
					res += "%10.4f" % num
				j += 1
			if (len(self.r) > 0 or self.extended):
				if (self.extended):
					res += "   | %10.4f" % self.values[i][self.n]
				else:
					res += "   | %10.4f" % self.r[i]
				i += 1
			res += '\n'
		return res

	def __str__(self):
		res = "\n"
		i = 0
		for line in self.values:
			j = 0
			for num in line:
				if j < self.n:
					res += "%5.f" % num
				j += 1
			if (len(self.r) > 0 or self.extended):
				if (self.extended):
					res += "   | %10.2f" % self.values[i][self.n]
				else:
					res += "   | %10.2f" % self.r[i]
				i += 1
			res += '\n'
		return res


