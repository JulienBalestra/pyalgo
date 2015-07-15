class DecoSingleton:
	def __init__(self, decorated):
		self._decorated = decorated
		self._instance = None

	def get_instance(self, *args):
		if self._instance is None:
			self._instance = self._decorated(*args)
		return self._instance

	def __call__(self, *args):
		return self.get_instance(*args)


class MetaSingleton(object):
	_instance = None

	def __new__(cls, *args):
		if not cls._instance:
			cls._instance = super(MetaSingleton, cls).__new__(cls)
		return cls._instance

	def __init__(self, arg_one):
		self.arg_one = arg_one

	def affect_arg_two(self):
		self.arg_two = self.arg_one