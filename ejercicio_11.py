"""
Dada una lista de números devolver el resultado de la multiplicación de todos ellos
"""

lista_numeros=[2,4,5,3,67,98]
resultado=1

for item in lista_numeros:
    resultado*=item

print("El resultado es: {}".format(resultado))