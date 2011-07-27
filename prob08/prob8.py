def fileread(filename):
	f = open(filename,'r')
	return f.read()

def productfromstring(str):
	high = 0
	for a in xrange(996):
		c = str[a:a+5]
		prod = 1
		for i in xrange(5):
			p = int(c[i])
			prod *= p
		if prod > high: high = prod
	return high
		
	

print productfromstring(fileread('prob8data'))




	
