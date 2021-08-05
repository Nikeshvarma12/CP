# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).

def consecutivedigits(n):
	n=abs(n)
	k=0
	l=0
	c=1
	while(n>0):
		a=n%10
		n=n//10
		b=n%10
		if(a==b):
			c=c+1
		else:
			if(l<c):
				l=c
				k=a
			elif(l==c):
				if(k>=a):
					k=a
			c=1
	return k
def longestdigitrun(n):
	# Your code goes here
	return consecutivedigits(n)
