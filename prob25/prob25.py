import math
fuck = 1
count = 2
a = 1
b = 1
cob = math.log(10)
while (math.log(fuck)/cob)+1 < 1000:
	fuck = a+b
	a = b
	b = fuck
	count += 1
print count
	
	
