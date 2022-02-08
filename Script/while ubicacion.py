#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:06:15 2022

@author: mateobonilla
"""
while True:
    x=input("ingrese un numero:")
    if x== "q" or x== "quit":
        break
    
    x=int(x)
    y=int(x)

    while True:
     print(y)
     y+=1
     if y>x:
        break
    