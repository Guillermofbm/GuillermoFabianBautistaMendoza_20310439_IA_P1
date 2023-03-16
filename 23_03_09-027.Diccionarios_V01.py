# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:37:32 2023

@author: guill
"""

# Se definen dos diccionarios para representar dos teclados diferentes
teclado1 = {
    'Categoría': 'Teclados',
    'Modelo': 'HyperX Alloy FPS Pro',
    'Precio': '89,99'
}
teclado2 = {
    'Categoría': 'Teclados',
    'Modelo': 'Corsair K55 RGB',
    'Precio': '59,99'
}
# Se almacena el valor asociado a la clave 'Modelo' del diccionario 'teclado1' en la variable 'consulta'
consulta = teclado1['Modelo']
# Se imprimen los valores asociados a las claves 'Modelo' y 'Precio' del diccionario 'teclado2'
print(teclado2['Modelo'])
print(teclado2['Precio'])