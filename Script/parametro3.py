#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:23:02 2022

@author: mateobonilla
"""

def direction(ciudad,calle,barrio):
    print("La direccion del barrio es:")
    print("Sector la",barrio)
    print("En la calle", calle)
    print("En la ciudad de", ciudad)
cl=input("Ingrese la calle:")
ba=input("Inrese el sector del domicilio")
ci=input("Ingrese la ciudad")

direction(ci,ba,ci)