# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).
def prime(n):
		if(n==2):
				return True
		elif(n>2):
    			for i in range(2,int(n/2)+1):
    					if(n%i==0):
    							return False
		elif(n==1):
			return False
		return True


def ishappynumber(n):
    	# your code goes here

	

	if(n==1):
		return True
	
	elif(n<1):
		return False
	sum=check(n)
	if(sum==1):
		return True
	else:
		return False

def check(n):
	sum=0
	while(1):
		r=n%10
		sum+=r*r
		n=n//10
		
		if(n==0):
			if(sum>=10):
				n=sum
				sum=0
			else:
				return sum


def fun_nth_happy_prime(n):
	found=0
	guess=0
	while(found<=n):
		guess+=1
		if(ishappynumber(guess) and prime(guess)):
			found+=1
	return guess




		


