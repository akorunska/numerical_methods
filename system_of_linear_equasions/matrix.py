import copy

class Matrix:
	def __init__(self, n=0, values=[], r=[], extended=True):
		self.n = n
		self.values = values
		self.extended = extended
		if (extended):
			i = 0
			for num in r:
				values[i].append(num)
				i += 1
		else:
			self.r = r


	def get_copy(self):
		return copy.deepcopy(self)

	def __str__(self):
		res = "\n"
		i = 0
		for line in self.values:
			j = 0
			for num in line:
				if j < self.n:
					res += "%5d" % num
				j += 1
			if (self.extended):
				res += " | " + str(self.values[i][self.n]) +'\n'
			else:
				res += " | " + str(r[i]) +'\n'
			i += 1
		return res


