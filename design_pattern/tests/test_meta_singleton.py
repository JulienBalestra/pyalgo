from unittest import TestCase

from design_pattern.singleton import MetaSingleton as Singleton


class TestSingleton(TestCase):
	def test_singleton_00(self):
		i, j = None, None
		self.assertIsNone(i)
		i = Singleton("test0")
		self.assertEqual(i.arg_one, "test0")
		i.affect_arg_two()
		self.assertEqual(i.arg_two, "test0")
		self.assertIsInstance(i, Singleton)
		j = Singleton("test1")
		self.assertEqual(j.arg_one, "test1")
		self.assertEqual(j.arg_two, "test0")
		self.assertIsInstance(i, Singleton)
		self.assertTrue(id(i) == id(j))