def generator(x):
	n = 0
	while n < x:
		v = (yield n)
		if v:
			n = v
		else:
			n += 1
