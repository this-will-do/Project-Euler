def seq(num,count):
	ret = 0
	if num == 1: return count
	if num % 2:
		ret = seq(3*num+1,count+1)
	else:
		ret = seq(num/2,count+1)
	return ret

high = tuple( (0,0) )
for x in xrange(999999,1000000//3,-2):
	print ('At:',x)
	ret = seq(x,1)
	if ret > high[0]: 
		high = tuple( (ret,x) )

print high
