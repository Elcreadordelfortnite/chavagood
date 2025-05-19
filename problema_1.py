"""
tarea 1 
cristopher salvador mendoza contreras
371156
"""

def pedir_numero():
    try:
        N = 5.6
        if N <= 0:
            print("Error: El número debe ser positivo.")
        else:
            print(f"El número ingresado es: {N}")
    except ValueError:
        print("Error: No has ingresado un número entero válido.")


pedir_numero()