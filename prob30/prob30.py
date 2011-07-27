list = [a**4 for a in xrange(0,10)]
ans = []

for a in xrange(0,10):
	for b in xrange(0,10):
		for c in xrange(0,10):
			for d in xrange(0,10):
				sum = (1000*a)+(100*b)+(10*c)+(d)
				if list[a]+list[b]+list[c]+list[d] is sum: ans.append(sum)

print ans
