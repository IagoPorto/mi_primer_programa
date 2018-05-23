"""
Modificar el programa de la tabla de multiplicar para que vaya del 5 al 15 y no del 1 al 10
"""

numero=int(input("Escribe un número: "))

for a in range(5,16):
    resultado=numero*a
    print("{}x{}={}".format(numero,a,resultado))

