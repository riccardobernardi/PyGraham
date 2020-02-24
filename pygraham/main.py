from pygraham import *


def test_list():
	v = list([1, 2, 3])
	v = v.map(lambda x: 2 * x)

	print(v)

def test_list_map_reduce():
	v = list([1, 2, 3])
	v = v.map(lambda x: 2 * x).reduce(lambda x,y: x+y)

	print(v)

def test_list_map_filter_reduce():
	v = list([1, 2, 3])
	v = v.map(lambda x: 2 * x).filter(lambda x: (x%2==0)).reduce(lambda x,y: x+y)

	print(v)

def test_list_map_filter_zip():
	v = list([1, 2, 3])
	v = v.map(lambda x: 2 * x).filter(lambda x: (x%2==0)).zip([2,3,4], lambda x, y: (x+y, x*y))

	print(v)

def test_dict():
	v = dict({9:2,11:3,33:4})
	v = v.map(lambda x: 2 * x[0] + 2*x[1])

	print(v)

def test_dict_unzip():
	v = dict({9:2,11:3,33:4})
	u, v = v.unzip(lambda x: x[0], lambda x: x[1])

	print(u)
	print(v)

def test_dict_unzip_zip():
	v = dict({9:2,11:3,33:4})
	u, v = v.unzip(lambda x: x[0], lambda x: x[1])
	u = u.zip(v,lambda x,y: (x,y))

	print(u)

def test_dict_unzip_zip_to_dict():
	v = dict({9:2,11:3,33:4})
	u, v = v.unzip(lambda x: x[0], lambda x: x[1])
	u = u.zip(v,lambda x,y: (x,y))
	u = dict(u)

	print(u)

def test_set():
	v = set([4, 43, 36])
	v = v.map(lambda x: 2 * x)

	print(v)


if __name__ == "__main__":
	print("test_list()")
	test_list()
	print("-------------------------")
	print("test_list_map_reduce()")
	test_list_map_reduce()
	print("-------------------------")
	print("test_list_map_filter_reduce()")
	test_list_map_filter_reduce()
	print("-------------------------")
	print("test_list_map_filter_zip()")
	test_list_map_filter_zip()
	print("-------------------------")
	print("test_dict()")
	test_dict()
	print("-------------------------")
	print("test_dict_unzip()")
	test_dict_unzip()
	print("-------------------------")
	print("test_dict_unzip_zip()")
	test_dict_unzip_zip()
	print("-------------------------")
	print("test_dict_unzip_zip_to_dict()")
	test_dict_unzip_zip_to_dict()
	print("-------------------------")
	print("test_set()")
	test_set()
	print("-------------------------")
