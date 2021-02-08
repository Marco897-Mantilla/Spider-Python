# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:26:09 2021

@author: mmant
"""

while True:
    x=input("Enter a number to count to: ")
    if x=='q' or x=='quit':
        break
    
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break