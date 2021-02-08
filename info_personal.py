# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:07:58 2021

@author: mmant
"""

first_name=input("Ingrese su primer Nombre: ")
second_name=input("Ingrese su segundo Nombre: ")
last_name=input("Ingrese su Apellidos: ")
born=input("Ingrese su ciudad de nacimiento: ")
city=input("Ingrese su ciudad actual: ")
location=input("Ingrese su Ubicación: ")
age=input("Ingrese su Edad: ")
space=" "
print("\n")

print("Su primer nombre es ",first_name,space,", su segundo nombre es ",second_name,", sus apellidos son ",last_name+space,", nacio en la ciudad de ",born," pero actualmente vive en la ciudad de ",city," y su dirección actual es ",location," ademas tiene",space+age," años")

age=int(age)

if age>=0 and  age<= 12:
    print(", Usted es un niño, menor de edad.")
elif age>=13 and  age<= 17:
     print(", Usted es un joven, menor de edad.")
elif age>=18 and  age<= 25:
     print(", Usted es un joven, mayor de edad.")
elif age>=25 and  age<= 65:
     print(", Usted es un adulto.")
else:
    print(", Usted es de la tercera edad.")