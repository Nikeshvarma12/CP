# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
	n=len(l)
	for i in range(n):
		b=len(l[i])
		for j in range(b):
			if(isprime(l[i][j])):
				return False
	return True
def isprime(n):
    if(n<=1):
        return False
    if(n==2):
        return True
    if(n%2==0):
        return False
    maxfactor=round(n**0.5)
    for i in range(3,maxfactor+1):
        if(n%i==0):
            return False
    return True

