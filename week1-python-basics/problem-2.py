# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 22:31:16 2018

@author: Filip
"""

counter = 0
for i in range(len(s)-2):
    if s[i] == "b" and s[i+1] == "o" and s[i+2] == "b":
        counter +=1
print("Number of times bob occurs is: " + str(counter))