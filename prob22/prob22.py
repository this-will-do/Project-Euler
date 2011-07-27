f = open('prob22data')
namelist = f.read().split(',')


namelist.sort()

sum = 0
for i in xrange(0,len(namelist)):
	word = 0
	for l in namelist[i]:
		if l is not '"':
			word += (ord(l)-64)
	sum += (i+1) * word

print sum
