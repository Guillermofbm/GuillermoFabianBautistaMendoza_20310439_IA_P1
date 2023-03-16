# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:48:39 2023

@author: guill
"""

# Definición de una tupla llamada "colores" con 4 elementos
colores = ('azul', 'rojo', 'negro', 'amarillo')
# Se le pide al usuario que ingrese un color a buscar y se guarda en una variable llamada "entrada"
entrada = input('Escribe un color a buscar...\n')
# Se verifica si el color ingresado por el usuario está en la tupla "colores"
if entrada in colores:
    # Si el color está en la tupla, se imprime un mensaje diciendo que el color está admitido
    print('El color ' + entrada + ' está admitido')
else:
    # Si el color no está en la tupla, se imprime un mensaje diciendo que el color no está admitido
    print('El color ' + entrada + ' no está admitido')
