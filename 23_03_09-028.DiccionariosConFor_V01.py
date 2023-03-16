# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:41:12 2023

@author: guill
"""
#Creamos un diccionario llamado teclado1 con sus argumentos
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}
#Creamos un diccionario llamado teclado2 con sus argumentos
teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}
#Creamos un ciclo for que navegue entre los argumentos del diccionario teclado1
for x in teclado1:
    #imprimimos la categoria y su valor
	print(x+" = " +teclado1[x])