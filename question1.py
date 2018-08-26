# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 23:36:46 2018

@author: shurastogi
"""

randomList=['a',0,2]
def acceptrandom(items):
    for item in items:
        print("The entry is {}".format(item))
        try:
            r=1/item
        except Exception as ex:
            print("OOps {} occured".format(ex.__class__))
        else:
            print("The reciprocal of {} is {}".format(item,r))
        finally:
            print("Next Entry")

acceptrandom(randomList)