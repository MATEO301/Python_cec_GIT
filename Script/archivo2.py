#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:37:14 2022

@author: mateobonilla
"""

file = open("devices.txt")
for a in file:
    a=a.strip("\n")
    print(a)
file.close()