# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:18:07 2021

@author: mmant
"""

file=open('devices.txt')

while True:
    n=input('Ingrese un nuevo item: ')
    if n =='exit':
        print('Listo')
        break
    else:
        file.write(n + '\n')
   
        
file.close()
