import time


def timer(func):
	def count(seconds):
		ts = time.time()
		func(seconds)
		return time.time() - ts

	return count