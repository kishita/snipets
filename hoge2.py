class hoge:
	def __init__(self, x):
		self.data = x
		self.pup = None

	def __mul__(self, x):
		return x * 5

	def __add__(self, x):
		return x + 3

hoge = hoge(5)
print hoge.data
print hoge * 4
print hoge + 5
print hoge + 8