# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	a=[]
	b=len(L)
	for i in range(b):
		n=len(L[i])
		for j in range(n):
			if(L[i][j] in a):
				return True
			else:
				a.append(L[i][j])
	return False
