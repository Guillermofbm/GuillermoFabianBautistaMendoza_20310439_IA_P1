# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:13:46 2023

@author: guill
"""
# Definir una variable x y asignarle el valor de 0
x = 0

# Crear un bucle while que se ejecutará mientras x sea menor que 15
while x < 15:
    # Incrementar el valor de x en 5 unidades
    x = x + 5
    # Imprimir el valor de x en cada iteración
    print(x)

# Imprimir una línea vacía
print("")

# Asignar a x el valor de 0 nuevamente
x = 0

# Crear un bucle while que se ejecutará mientras x sea mayor que -100
while x > -100:
    # Disminuir el valor de x en 20 unidades
    x = x - 20
    # Imprimir el valor de x en cada iteración
    print(x)

# Imprimir una línea vacía
print("")

# Asignar a x el valor de 10
x = 10

# Crear un bucle while que se ejecutará mientras x sea mayor que 0
while x > 0:
    # Disminuir el valor de x en 1 unidad
    x = x - 1
    # Imprimir un mensaje que indica el valor actual de x en cada iteración
    print("El valor del bucle es " + str(x))
