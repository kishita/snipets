def decorate(f):
	f.x = 1
	return f

def add_one(f):
	def new_f(*args, **kwds):
		result = f(*args, **kwds)
		return result + 1
	return new_f

def multiple(x):
	def _multiple(f):
		def new_f(*args, **kwds):
			result = f(*args, **kwds)
			return result * x
		return new_f
	return _multiple

def hoge(m,n):
	if m % n == 0:
		return n
	else:
		r = m % n
		return hoge(n,r)

@multiple(2)
@add_one
def func():
	return 3

print func()

def timing(f):
	import time
	def new_f(*args, **kwds):
		t = time.time()
		result = f(*args, **kwds)
		print ('%s: %s' % (f.func_name, time.time()-t))
		return result
	return new_f

def accepts(*types):
	def _accepts(f):
		def new_f(*args, **kwds):
			for arg, type_ in zip(args, types):
				if not isinstance(arg, type_):
					raise TypeError('%s -> %s' % (arg, type_))
			return f(*args, **kwds)
		return new_f
	return _accepts

@accepts(str, int)
def duplicate(text, count):
	return ''.join(map(lambda x: ''.join(x),
		zip(*(text,)*count)))

print duplicate('Python',3)

class Shape(object):
	def __init__(self, width):
		self.width = width
	@classmethod
	def create_from_text(cls, text):
		width = {'large':10, 'medium':3, 'small':1}[text]
		return cls(width)
	@staticmethod
	def get_golden_ratio(width):
		return (width, width / 1.61803388)

shape = Shape.create_from_text('large')

import re
pattern = re.compile('p')
print pattern.sub('s', 'hop step jump')
pattern = re.compile('[a-z]', re.I)

import json
obj = ['foo', {'bar': ('baz', None, 1.0, 2)}]
json_str = json.dumps(obj)
print json_str
print json.loads(json_str)
