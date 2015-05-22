def fibonacci(n):
	a, b = 0, 1
	for _ in xrange(n):
		yield a
		a, b = b, a + b