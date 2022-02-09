#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:04:57 2022

@author: mateobonilla
"""

def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=" ")
        """ c=a+b
        a=b
        b=c"""
        a,b=b,a+b
fib(8)