# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:53:47 2023

@author: guill
"""

# Se define la función "colores" que toma un número variable de argumentos (*args)
def colores(*args):
	# Se imprime un mensaje que incluye los dos primeros argumentos recibidos en la función
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')
# Se llama a la función "colores" con los argumentos 'Rojo' y 'Azul'
colores('Rojo','Azul')
# Se define la función "suma" que toma un número variable de argumentos (*args)
def suma(*args):
    # Se define la variable "x" como la suma de los dos primeros argumentos recibidos en la función
    x = args[0] + args[1]
    # Se imprime el valor de la variable "x"
    print(x)
# Se llama a la función "suma" con los argumentos 5 y 7
suma(5, 7)
