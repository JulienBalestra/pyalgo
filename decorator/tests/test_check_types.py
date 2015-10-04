import unittest

from decorator.check_types import accepts


class TestCheckTypes(unittest.TestCase):
	def test_00(self):
		@accepts(int)
		def test_00(integer):
			return integer * integer

		self.assertEqual(25, test_00(5))

	def test_01(self):
		@accepts(int)
		def test_01(integer):
			return integer * integer

		with self.assertRaises(TypeError):
			test_01('2')

	def test_02(self):
		with self.assertRaises(AttributeError):
			@accepts(int)
			def test_02(integer, floating):
				return integer * floating

			test_02(5, 2.5)  # in fact not really needed

	def test_03(self):
		@accepts(int, float)
		def test_03(integer, floating):
			return integer * floating

		self.assertEqual(12.5, test_03(5, 2.5))
