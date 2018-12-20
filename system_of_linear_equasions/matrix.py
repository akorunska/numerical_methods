import copy

class Matrix:
	def __init__(self, n=0, values=[], r=[], extended=False, m=0):
		self.n = n
		if m is 0:
			self.m = n
		else:
			self.m = m
		self.values = values

		if len(values) is  0 :
			self.values = [[0 for y in range(self.n)] for x in range(self.m)]

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

	def transpose(self):
		ans = Matrix(n=self.m, m=self.n)

		for i in range(self.m):
			for j in range(self.n):
				ans.values[j][i] = self.values[i][j]
		return ans

	def mult(self, m2):
		ans = Matrix(n=m2.n, m=self.m) # ans is rows1 x cols2
		for i in range(ans.m):
			for j in range(ans.n):
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


