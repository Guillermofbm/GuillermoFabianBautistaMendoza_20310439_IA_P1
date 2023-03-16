# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:21:57 2023
Este programa utiliza un bucle while para imprimir los valores de x del 1 al 30, excepto los valores 4, 6 y 10.
El programa se detendrá cuando x llegue a 15.
"""

# Inicializar x con un valor de 0
x = 0

# Iniciar un bucle while que se ejecutará mientras x sea menor o igual a 30
while x <= 30:
    # Incrementar x en 1 en cada iteración
    x = x + 1
    
    # Verificar si x es diferente de 4, 6 o 10
    if x != 4 or x != 6 or x != 10:
        # Si x es diferente de 4, 6 o 10, imprimir el valor de x
        print("El valor del bucle es: " + str(x))
    else:
        # Si x es igual a 4, 6 o 10, imprimir que se saltó el valor de x
        print("Se saltó el valor de x")
    
    # Verificar si x es igual a 15
    if x == 15:
        # Si x es igual a 15, salir del bucle while
        break

# Imprimir el valor de x cuando se saltó el bucle while
print("Se saltó el bucle cuando x valía: " + str(x))
