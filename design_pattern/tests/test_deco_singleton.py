from unittest import TestCase

from design_pattern.singleton import DecoSingleton as Singleton


@Singleton
class FooNone:
	def __init__(self):
		pass


@Singleton
class FooOne:
	def __init__(self, argue):
		self.argue = argue


class TestSingleton(TestCase):
	def test_singleton_00(self):
		i, j = None, None
		self.assertIsNone(i)
		i = FooOne("test0")
		self.assertEqual(i.argue, "test0")
		self.assertIsInstance(i, type(FooOne))
		j = FooOne("test1")
		self.assertEqual(j.argue, "test0")
		self.assertIsInstance(i, type(FooOne))
		self.assertTrue(i is j)

	def test_singleton_01(self):
		i, j = None, None
		self.assertIsNone(i)
		i = FooOne("test2")
		self.assertEqual(i.argue, "test0")
		self.assertIsInstance(i, type(FooOne))
		j = FooOne("test3")		
		self.assertEqual(j.argue, "test0")
		self.assertIsInstance(i, type(FooOne))
		
		self.assertTrue(i is j)	
		
	def test_singleton_02(self):
		i, j = None, None
		self.assertIsNone(i)
		i = FooNone()
		self.assertIsInstance(i, type(FooOne))
		j = FooNone()
		self.assertIsInstance(i, type(FooOne))
		self.assertTrue(i is j)

	def test_singleton_03(self):
		i, j = None, None
		self.assertIsNone(i)
		i = FooNone()		
		self.assertIsInstance(i, type(FooOne))
		j = FooNone()
		self.assertIsInstance(i, type(FooOne))
		self.assertTrue(i is j)