# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 23:38:29 2018

@author: shurastogi
"""

list_exam=[0,1,2]
def fun(index):
    try:
        print(list_exam[index])
    except IndexError as ex:
        print("you have search for index outside of list", ex)

fun(2)
fun(3)z