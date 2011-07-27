def diffsumsq(max):
	sumsq = 0
	sqsum = 0
	for c in xrange(max+1):
		sumsq += (c*c)
		sqsum += c
	print (sumsq,sqsum)
	return (sqsum*sqsum)-sumsq

print diffsumsq(100)

