# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 19:24:24 2017

@author: Shahriar Kabir
"""

def deep_reverse(L):
    aList = []
    for i in L[-1::-1]:
        temp = []
        for k in i[-1::-1]:
            temp.append(k)
        aList.append(temp)
    return aList
print(deep_reverse([[1, 2], [3, 4], [5, 6, 7]]))