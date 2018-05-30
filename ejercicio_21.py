"""
Crea una función que reciba una lista y devuelva otra con los números pares
"""

def pares (lista):
    lista_pares=[]
    cont=0

    for item in lista:
        if item % 2 == 0:
            lista_pares.append(lista[cont])
        cont+=1
    return lista_pares

mi_lista=[1,2,3,4,5,6,7,8,34,21,765,432]
mis_pares=pares(mi_lista)

print("{}".format(mis_pares))
