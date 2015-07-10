import unittest
import time

from decorator.timer import timer, timer_with_ret


@timer
def my_function(seconds):
	time.sleep(seconds)


@timer_with_ret
def my_function_ret(seconds):
	time.sleep(seconds)
	return seconds + seconds


class TestTimer(unittest.TestCase):
	def test_00_timer(self):
		seconds = 1
		self.assertEqual(seconds, round(my_function(seconds)))
		
	def test_00_timer_with_ret(self):
		seconds = 1
		ret = my_function_ret(seconds)
		self.assertEqual(seconds, round(ret[0]))
		self.assertEqual(seconds + seconds, ret[1])