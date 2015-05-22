from unittest import TestCase

from design_pattern.singleton import Singleton


@Singleton
class Foo:
	def __init__(self):
		pass


class TestSingleton(TestCase):
	def test_singleton(self):
		i = Foo.get_instance()
		self.assertIsInstance(i, type(Foo))
		j = Foo.get_instance()
		self.assertIsInstance(i, type(Foo))
		self.assertTrue(i is j)

	def test_singleton_raise(self):
		k = None
		try:
			k = Foo()
			self.assertEqual(0, 1)
		except TypeError:
			self.assertNotIsInstance(k, type(Foo))
		finally:
			self.assertIsNone(k)