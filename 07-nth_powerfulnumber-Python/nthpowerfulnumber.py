# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math
def nthpowerfulnumber(n):
	# Your code goes here
	a=0
	b=0
	while(a<=abs(n)):
		b+=1
		if(isPowerful(b)):
			a+=1
	return b
def isPowerful(n):
	while(n%2==0):
		x=0
		while(n%2==0):
			n=n//2
			x+=1
		if(x==1):
			return False
	for i in range(3, int(math.sqrt(n))+1,2):
		x=0
		while(n%i==0):
			n=n//i
			x=x+1
		if(x==1):
			return False
	return (n==1)

