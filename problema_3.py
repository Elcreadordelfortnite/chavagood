"""
Tarea 3 
cristopher salvador mendoza contreras 
371156
"""
import numpy as np
import random
N = 4
x = [random.randint(1, 9) for _ in range(N)]  # Corregido randit a randint

matriz = []
for i in range(N):
    fila = []
    for j in range(1, N+1):  # Este rango está correcto
        fila.append(x[i] * j)
    matriz.append(fila)  # Este código ahora está dentro del bucle principal, al final de cada fila

for fila in matriz:
    print(fila)
