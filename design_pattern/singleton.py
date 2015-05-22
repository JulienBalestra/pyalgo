class Singleton:
	def __init__(self, decorated):
		self._decorated = decorated
		self._instance = None

	def get_instance(self):
		if self._instance is None:
			self._instance = self._decorated()
		return self._instance

	def __call__(self):
		raise TypeError('Use get_instance() method')