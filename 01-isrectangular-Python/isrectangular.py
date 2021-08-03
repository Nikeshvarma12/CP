# Write the function isrectangular(L) that takes a possibly-2d 
# list L and returns True  if it is rectangular, so each row has
#  the same number of elements. Return False otherwise.


def fun_isrectangular(l):
	n=len(l)
	b=len(l[0])
	for i in range (n):
		if(len(l[i])!=b):
			return False
	return True



