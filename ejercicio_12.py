"""
Dada una lista de enteros y strings, devolver dos listas una con los enteros y otra con las strings
"""

lista=["jajjaj", 3,4,5,"payaso"]
enteros=[]
strings=[]

for item in lista:
    tipo=type(item)
    if tipo==type("a"):
        strings.append(item)
    else:
        enteros.append(item)

print("Los enteros son: {}\nLas strings son: {}".format(enteros,strings))

