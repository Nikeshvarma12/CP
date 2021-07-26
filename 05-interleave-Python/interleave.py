# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	a=len(s1)
	b=len(s2)
	n=''
	if(a<b):
		k=a
	else:
		k=b
	for i in range(0,k):
		n=n+s1[i]+s2[i]
	if(k==a):
		n=n+s2[i+1:]
	else:
		n=n+s1[i+1:]
    
	return n

	