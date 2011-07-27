import math
sentinel = int(math.floor(math.sqrt(500)))
for x in xrange(sentinel,1,-1):
	if not 500 % x:
		y = (500 / x) - x
		a = x*x - y*y
		b = 2 * x * y
		c = x*x + y*y
		if a+b+c == 1000:
			print ((a*b*c),a,b,c)
			break;
