# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:44:40 2023

@author: guill
"""

# Se define un diccionario llamado "teclado1" con tres pares clave-valor
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}
# Se define un diccionario llamado "teclado2" con tres pares clave-valor
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
# Se elimina la variable "teclado1"
del teclado1
# Se eliminan las claves "Categoría" y "Precio" del diccionario "teclado2"
del teclado2['Categoría']
del teclado2['Precio']
# Se imprime el valor de la clave "Modelo" del diccionario "teclado2"
print(teclado2['Modelo'])