# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 19:24:24 2017

@author: Shahriar Kabir
"""

def deep_reverse(L):
    """ 
    assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    aList = []
    for i in L[-1::-1]:
        temp = []
        for k in i[-1::-1]:
            temp.append(k)
        aList.append(temp)
    return aList
print(deep_reverse([[1, 2], [3, 4], [5, 6, 7]]))
