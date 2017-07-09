# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 16:18:55 2017

@author: Shahriar Kabir
"""

def word_distribution(text):
    text = text.lower()
    text = text.split()
    aDict = {}
    for i in text:
        temp = ''
        for j in i:
            if len(temp) == 0:
                if j in 'abcdefghijklmnopqrstuvwxyz':
                    temp += j
            else:               
                if j in "abcdefghijklm’nopqrstuvw'xyz":
                    temp += j
        if temp in aDict:
            aDict[temp] += 1
        else:
            aDict[temp] = 1
    return aDict 

text_string = "Hello and welcome to Analytics in Python! We're very excited you're joining us to learn about Analytics in Python and how its application will shape the next generation of Business Analytics."
print(word_distribution(text_string))