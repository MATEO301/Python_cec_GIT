#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:43:48 2022

@author: mateobonilla
"""

lista=[]
file = open("devices.txt")
for a in file:
    a=a.strip("\n")
    lista.append(a)
    print(a)
file.close()
print(a)