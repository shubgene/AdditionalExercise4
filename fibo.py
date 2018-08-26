# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 15:26:19 2018

@author: shurastogi
"""

def fib2(num):
    n1=0
    n2=1
    if(num<=0):
        print("Number should be positive")
    elif(num==1):
        print(1)
    else:
        while(n1<num):
            print(n1,end=",")
            n=n1+n2
            n1=n2
            n2=n