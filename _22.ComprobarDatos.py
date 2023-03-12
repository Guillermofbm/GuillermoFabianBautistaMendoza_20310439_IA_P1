# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:48:39 2023

@author: guill
"""

colores = ('azul','rojo','negro','amarillo')
entrada = input('Escribe un color a buscar...\n')
if(entrada in colores):
    print('El color '+entrada+ ' está admitido')
else:
    print('El color '+entrada+ ' no está admitido')