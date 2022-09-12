#!/bin/python3

# Greene, Jordan CS 5450 Prog 1

from stringlib import *

#Add a Worker class to this file.
#
#The Worker class constructor needs to take as input
#a string.  It will set its own data member to that string.
class Worker:
    def __init__(self, str):
        self.str = str
#
#Add methods to the Worker class that are equivalent to
#functions in the stringlib module.  These methods will
#not take a string as input (except for the containsWord
#method, which will take the contained string parameter).  Instead,
#these methods will operate on the Worker class data member. 
#Your method can call the needed function in the stringlib
#module.
    def reverseStr(self):
        return reverseStr(self.str)
    
    def containsWord(self, externalStr):
        return containsWord(self.str, externalStr)

    def isPalindrome(self):
        return isPalindrome(self.str)

    def upperCaseStr(self):
        return upperCaseStr(self.str)
