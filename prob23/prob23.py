def divisors(input):
	import math
	list = set()
	sentinel = int(math.ceil(math.sqrt(input)))
	for x in xrange(1,sentinel+1):
		if not input % x:
			list.add(x)
			list.add(input / x)
	return list

def abundant(input):
	l = divisors(input)
	summ = sum(i for i in l)
	summ -= input
	if summ > input: return True
	return False

ablist = []
nonlist = set()


for x in xrange(1,28124):
	if abundant(x): ablist.append(x)
print ("Abundant list size:",len(ablist))

for x in xrange(0,len(ablist)):
	for y in xrange(x,len(ablist)):
		if ablist[x]+ablist[y] > 28123: break
		nonlist.add(ablist[x]+ablist[y])
print ("Blacklist size:",len(nonlist))

s = 0
for i in xrange(1,28124):
	if i in nonlist:continue
	s += i
	

print s
