import unittest
import time

from decorator.timer import timer


@timer
def my_function(seconds):
	time.sleep(seconds)


class TestTimer(unittest.TestCase):
	def test_00(self):
		seconds = 1
		self.assertEqual(seconds, round(my_function(seconds)))