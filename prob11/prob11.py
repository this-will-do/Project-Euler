f = open('prob11data')
c = []
for line in f:
	list = []
	sep = line.split(' ')
	for i in sep: list.append(int(i))
	c.append(list)
high = 0

for y in xrange(0,20):
	for x in xrange(0,20):
		try:
			prod = c[y][x] * c[y+1][x+1] * c[y+2][x+2] * c[y+3][x+3]
			if prod > high:
				high = prod
				print (x,y,prod)			
		except IndexError: continue
for y in xrange(0,20):
	for x in xrange(0,20):
		try:
			prod = c[y][x] * c[y][x+1] * c[y][x+2] * c[y][x+3]
			if prod > high: 
				high = prod
				print (x,y,prod)
		except IndexError: continue
for y in xrange(0,20):
	for x in xrange(0,20):
		try:
			prod = c[y][x] * c[y+1][x] * c[y+2][x] * c[y+3][x]
			if prod > high:
				high = prod
				print (x,y,prod)
		except IndexError: continue
for y in xrange(0,20):
	for x in xrange(0,20):
		try:
			prod = c[y][x] * c[y-1][x+1] * c[y-2][x+2] * c[y-3][x+3]
			if prod > high:
				high = prod
				print (x,y,prod)
		except IndexError: continue

print high
