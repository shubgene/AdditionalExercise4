# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 15:49:20 2018

@author: shurastogi
"""

def ispalindrome(str):
    rev=str[::-1]
    if(str.lower()==rev.lower()):
        print("String {} is palindrome".format(str))
    else:
        print("Not a Palindrome")
    