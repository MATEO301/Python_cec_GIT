#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 20:04:56 2022

@author: mateobonilla
"""

def saludo3(lista1):
    for nombre in lista1:
        print("Hola", nombre)
    print(" ")

saludo3(["Ana"])
saludo3(["Ana","Jose","Maria"])
saludo3(["Ana","Martin","Mateo","Daniel"])