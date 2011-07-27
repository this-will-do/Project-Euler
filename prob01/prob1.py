def sum35(end):
	res = 0
	for c in xrange(3,end,3):
		if c % 5 > 0: res += c
	for c in xrange(5,end,5):
		res += c
	return res

print sum35(1000)
