# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

import math
def isCircular(n):
    n1=n
    t=n
    c=0
    while(n1):
        c=c+1
        n1=n1//10

    while(isPrime(n)):
        rem=n%10
        d=n//10
        n=(10**(c-1))*rem + d
        if(n==t):
            return True

    return False
def isPrime(n):
    if(n<=1):
        return False
    if(n==2):
        return True
    if(n%2==0):
        return False
    l=round(n**0.5)
    for i in range(3,l+1):
        if(n%i==0):
            return False
    return True
def nthcircularprime(x):
    c=1
    i=1
    while(c<=x):
        if(isCircular(i)):
            c+=1
        i+=1
    return i-1
