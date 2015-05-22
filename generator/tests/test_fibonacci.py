from unittest import TestCase

from generator.fibonacci import fibonacci


class TestFibonacci(TestCase):
	def test_fibonacci_basic_loop(self):
		fibo = fibonacci(9)
		for i, ret in enumerate(fibo):
			if i == 0:
				self.assertEqual(0, ret)
			elif i == 1:
				self.assertEqual(1, ret)
			elif i == 2:
				self.assertEqual(1, ret)
			elif i == 3:
				self.assertEqual(2, ret)
			elif i == 4:
				self.assertEqual(3, ret)
			elif i == 5:
				self.assertEqual(5, ret)
			elif i == 6:
				self.assertEqual(8, ret)
			elif i == 7:
				self.assertEqual(13, ret)
			else:
				self.assertEqual(21, ret)

	def test_fibonacci_iter(self):
		ret = iter(fibonacci(9))
		self.assertEqual(0, ret.next())
		self.assertEqual(1, ret.next())
		self.assertEqual(1, ret.next())
		self.assertEqual(2, ret.next())
		self.assertEqual(3, ret.next())
		self.assertEqual(5, ret.next())
		self.assertEqual(8, ret.next())
		self.assertEqual(13, ret.next())
		self.assertEqual(21, ret.next())
		try:
			ret.next()
			self.assertEqual(0, 1)
		except StopIteration:
			pass