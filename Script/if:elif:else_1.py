#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:02:51 2022

@author: mateobonilla
"""

acl=int(input("Ingrese el # de ACL"))
if acl>=1 and acl<=99:
    print("La ACL es Estandar ")
elif acl>=100 and acl<=199: 
    print("La ACL es Extentida")
else:
    print("EL DATO INGRESADO NO ES UN ACL ")