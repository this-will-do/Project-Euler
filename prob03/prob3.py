import math

def primer(start,target,list):
	end = ceil(sqrt(target))
	while (start < end) and (target % start):
		++start
	if start >= end: return (1,target)
	
	return (list + (start,primer(start,target/start,list))
