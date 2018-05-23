"""
Crea un programa que calcule la media de todos los elementos de una lista
"""

lista=[3, 4, 5 ,6, 12, 98, 4]
contador=0
suma=0

for item in lista:
    contador+=1
    suma+=item

resultado=suma/contador

print("La media es: {}".format(resultado))
