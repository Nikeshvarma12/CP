# isPalindromicPrime() Write a function isPalindromicPrime that takes a value n as a parameter and retur
# urns True if the given n is a palindrome and prime and False otherwise.

def isPalindrome(n):
	reverse= int(str(n)[::-1])
	if(int(n)==reverse):
		return(True)
	else:
		return(False)

def isPrime(n):
	if n> 1:	
		for i in range(2, int(n/2)+1):
			if (n % i) == 0:
				print(False)
				#break
			else:
				return (True)
	else:
		return(False)

def isPalindromicPrime(n):
	if (isPalindrome(n)):
		if (isPrime(n)):
			return True
	else:	
		return False
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
print("All test cases passed... :-)")