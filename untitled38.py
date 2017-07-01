# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 20:55:09 2017

@author: Shahriar Kabir
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    ls = []
    def interior(aList):
        for i in aList:
            if type(i) == list:
                interior(i)
            else:
                ls.append(i)
        return ls
    return interior(aList)

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
