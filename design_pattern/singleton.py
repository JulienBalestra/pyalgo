class Singleton:
	def __init__(self, decorated):
		self._decorated = decorated
		self._instance = None

	def get_instance(self, *args):
		if self._instance is None:
			self._instance = self._decorated(*args)
		return self._instance

	def __call__(self, *args):
		return self.get_instance(*args)