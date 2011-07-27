def findperim(m,n):

a = 2
b = 1
last = 0
list = [0] * 1000

while a <= 1000:
	while b < a:
		last = findperim(a,b)
		if last <= 1000:
			list[last-1] += 1
			b+=1
		else: break
	a+=1

print list
high = 0
for i in xrange(0,1000):
	if list[i] > list[high]:
		high = i

		

