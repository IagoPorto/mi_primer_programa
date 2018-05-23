"""
Dada una lista de strings devolver una lista con el largo de cada string
"""

lista_strings=["jajajaja", "hola", "payaso"]
largo_strings=[]
contador=0

for item in lista_strings:
    for caracter in item:
        contador+=1
    largo_strings.append(contador)
    contador=0

print("lista_strings: {}".format(largo_strings))
