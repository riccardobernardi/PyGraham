class list(list):
	def map(self, l):
		tmp = self.__iter__()
		new = []
		for i in tmp:
			new.append(l(i))
		return new
