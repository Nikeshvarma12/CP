# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
    # Your code goes here
    size1 = len(str(x))
    size2 = len(str(y))
    temp = ''

    # Check if sizes of two strings are same
    if size1 != size2:
        return False

    # Create a temp string with value str1.str1
    temp = str(x) + str(x)

    # Now check if str2 is a substring of temp
    # string.count returns the number of occurrences of
    # the second string in temp
    if (temp.count(str(y)) > 0):
        return True
    elif(str(y)[::-1] == str(x) or str(x)[::-1] == str(y)):
        return True
    else:
        return False