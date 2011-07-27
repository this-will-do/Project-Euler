from string import whitespace
f = open('prob13data')
c = []
for line in f:
	l = []
	for i in line:
		 if i not in whitespace:
			l.append(i)
	c.append(l)
sums = []
for x in xrange(0,12):
	s = 0
	for y in xrange(0,100):
		s += int(c[y][x])
	sums.append(s)

for x in xrange(11,0,-1):
	remainder = sums[x] - (sums[x] % 10)
	sums[x-1] += remainder/10
	sums[x] = sums[x] % 10

print sums,
