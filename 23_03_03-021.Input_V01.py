# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:33:43 2023

@author: guill
"""


# Se le pide al usuario que ingrese su edad y se convierte a un entero
edad = int(input('¿Cuál es tu edad?\n'))
# Se evalúa la edad ingresada por el usuario y se imprime un mensaje correspondiente
if edad <= 0:
    # Si la edad es menor o igual a cero, se imprime un mensaje diciendo que nadie puede tener esa edad
    print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:
    # Si la edad está entre 1 y 17, se imprime un mensaje diciendo que el usuario es menor de edad
    print('Eres menor de edad.')
elif edad >= 18 and edad < 45:
    # Si la edad está entre 18 y 44, se imprime un mensaje diciendo que el usuario es mayor de edad
    print('Eres mayor de edad.')
elif edad >= 45 and edad < 100:
    # Si la edad está entre 45 y 99, se imprime un mensaje diciendo que el usuario ya es muy mayor
    print('Ya eres muy mayor')
elif edad > 100 and edad <= 120:
    # Si la edad está entre 101 y 120, se imprime un mensaje diciendo que el usuario se despida
    print('Despidete')
else:
    # Si la edad no se encuentra en ninguna de las categorías anteriores, se imprime un mensaje diciendo que la edad no es válida
    print('Edad no válida.')
