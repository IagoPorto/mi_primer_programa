"""
Modifica el programa de tabla de multiplicar para que solo muestre los resultados que sean multiplos de 2
"""

numero=int(input("Escribe un número: "))

for a in range(1,11):
    resultado = numero*a
    if resultado % 2 == 0:
        print("{}*{}={}".format(numero,a,resultado))

