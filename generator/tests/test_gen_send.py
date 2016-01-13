from unittest import TestCase

from generator.gen_send import generator


class TestSendGenerator(TestCase):
	def test_no_send(self):
		gen = generator(10)
		check = 0
		for i in gen:
			self.assertEqual(check, i)
			check += 1
		self.assertEqual(check, 10)

	def test_send(self):
		gen = generator(10)
		check = 0
		for i in gen:
			self.assertEqual(check, i)
			check += 1
			if i == 2:
				gen.send(7)
				check = 8
		self.assertEqual(check, 10)
