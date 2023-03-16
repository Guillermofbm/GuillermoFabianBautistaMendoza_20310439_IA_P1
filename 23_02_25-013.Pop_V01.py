# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 23:53:25 2023

@author: guill
"""

# Se define una lista llamada "colores" con 10 elementos
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
# Se define una lista llamada "popeados" con dos elementos vacíos
popeados = ['', '']
# Se elimina el segundo elemento de la lista "colores" y se asigna a la primera posición de la lista "popeados"
popeados[0] = colores.pop(1)
# Se elimina el noveno elemento de la lista "colores" y se asigna a la segunda posición de la lista "popeados"
popeados[1] = colores.pop(8)
# Se imprime la lista "popeados"
print(popeados)