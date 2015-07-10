import time


def timer(func):
	def count(seconds):
		ts = time.time()
		func(seconds)
		return time.time() - ts

	return count


def timer_with_ret(func):
	def count(seconds):
		ts = time.time()
		ret = func(seconds)
		return time.time() - ts, ret

	return count