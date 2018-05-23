"""
Crea un tabla de multiplicar pero invertida, dando los resultados desde el 10 hasta el 1
"""

numero=int(input("Escribe un número: "))

aux=9

for a in range(1,11):
    a+=aux
    aux-=2
    resultado=numero*a
    print("{}*{}={}".format(numero,a,resultado))