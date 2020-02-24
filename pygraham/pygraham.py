def map(o, l):
	tmp = o.__iter__()
	new = list([])
	for i in tmp:
		new += [l(i)]
	return new


def reduce(o, l):
	tmp = o.__iter__()
	r = 0
	for i in tmp:
		r = l(r, i)
	return r


def filter(o, l):
	tmp = o.__iter__()
	new = list([])
	for i in tmp:
		if l(i):
			new += [i]
	return new


def zip(o, v, l):
	v = list(v)
	new = list([])
	for i in range(len(o)):
		new += [l(o[i], v[i])]
	return new


def unzip(o, sx, dx):
	tmp = o.__iter__()
	new_sx = list([])
	new_dx = list([])
	for i in tmp:
		new_sx += [sx(i)]
		new_dx += [dx(i)]
	return new_sx, new_dx


def sort(o, l): # with respect to a rule
	pass


class list(list):
	def map(self, l):
		return map(self, l)

	def reduce(self, l):
		return reduce(self, l)

	def filter(self, l):
		return filter(self, l)

	def unzip(self, sx, dx):
		return unzip(list(self), sx, dx)

	def zip(self, v, l):
		return zip(list(self), v, l)

class dict(dict):
	def map(self, l):
		return map(list(self.items()), l)

	def reduce(self, l):
		return reduce(list(self.items()), l)

	def filter(self, l):
		return filter(list(self.items()), l)

	def unzip(self, sx, dx):
		return unzip(list(self.items()), sx, dx)

	def zip(self, v, l):
		return zip(list(self), v, l)

class set(set):
	def map(self, l):
		return map(list(self), l)

	def reduce(self, l):
		return reduce(list(self), l)

	def filter(self, l):
		return filter(list(self), l)

	def unzip(self, sx, dx):
		return unzip(list(self), sx, dx)

	def zip(self, v, l):
		return zip(list(self), v, l)
