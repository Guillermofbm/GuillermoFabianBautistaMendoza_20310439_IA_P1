# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:21:57 2023

@author: guill
"""

x =0
while x <= 30:
    x= x+1
    
    if x != 4 or  x!=6 or x!=10:
        print("El valor del bucle es: " + str(x))
    else:
        print("Se salto el valor de x")
    if x==15:
        break
print("Se salto el bucle cuando x valia: "+str(x))
    