# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:33:43 2023

@author: guill
"""

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad < 45:
	print('Eres mayor de edad.')
elif edad >= 45 and edad <100:
    print('Ya eres muy mayor')
elif edad > 100 and edad <=120:
    print('Despidete')
else:
	print('Edad no válida.')