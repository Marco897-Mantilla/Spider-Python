# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:26:58 2021

@author: mmant
"""

lista=[]
file=open('devices.txt')
for a in file:
    a=a.strip()
    lista.append(a)
    print(a)
file.close()

print(lista)