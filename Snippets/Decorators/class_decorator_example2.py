class Power(object):
	def __init__(self, arg):
		self._arg = arg
		self._memory = []

	def __call__(self, a, b):
		retval = self._arg(a, b)
		self._memory.append(retval ** 2)
		return retval ** 2

	def memory(self):
		return self._memory


@Power
def multiply_together(a, b):
	return a * b


print(multiply_together)
print(multiply_together(2, 2))
print(multiply_together(3, 2))
print(multiply_together(2, 6))
print(multiply_together.memory())