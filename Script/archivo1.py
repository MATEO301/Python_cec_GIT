#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 19:03:07 2022

@author: mateobonilla
"""

file = open("devices.txt","a")
while True:
    newItem=input("Ingrese datos:")
    if newItem == "exit":
        print("Esta hecho")
        break
    file.write(newItem + "\n")  
file.close()
