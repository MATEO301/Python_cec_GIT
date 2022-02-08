#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 23:34:12 2022

@author: mateobonilla
"""
space=" "
nombre=input("Hola, Como te llamas?")
apellido=input("Y tu apellido, Cual es?")
print("Un gusto de conocerte",nombre+space+apellido)
lugar=input("En donde vives?")
edad=int(input("Cuantos años tienes?"))
print("Hola"+space+nombre+apellido+space+"vive en:"+space+
      "y tiene:",edad,"años")
         
if edad>=0 and edad<=17: 
    print (nombre,"es un menor de edad")
elif edad>=18 and edad<=65:
    print(nombre,"es un mayor de edad")
elif edad>=80 and edad<=99:
    print(nombre,"es un anciano")
elif edad>=100 and edad<=105:
    print(nombre,"es un mayor de larga vida")
else:
    print(nombre,"deberia estar descansando")