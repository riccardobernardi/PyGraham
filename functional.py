class dict(dict):
	def map(self, l):
		tmp = list(self.items())
		new = {}
		for i in tmp:
			new[i[0]] = l(i[1])
		return new


import array


class list(list):
	def map(self, l):
		tmp = self.__iter__()
		new = []
		for i in tmp:
			new.append(l(i))
		return new
