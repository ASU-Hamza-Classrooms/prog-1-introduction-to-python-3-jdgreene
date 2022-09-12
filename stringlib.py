#!/bin/python3

# Greene, Jordan CS 5450 Prog 1

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
from operator import truediv

def reverseStr(str):
    return str[::-1]
#
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
def containsWord(containingStr, containedStr):
    if containedStr in containingStr:
        return 'Yes'
    return 'No'
#
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
def isPalindrome(str):
    rStr = reverseStr(str)
    if str == rStr:
        return 'Yes'
    return 'No'
#
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
def upperCaseStr(str):
    return str.upper()
#

if __name__ == '__main__':
    test = 'hello there'
    print(reverseStr(test))
    print(containsWord(test, 'ello'))
    print(containsWord(test, 'yello'))
    print(isPalindrome(test))
    print(isPalindrome('uggu'))
    print(upperCaseStr(test))