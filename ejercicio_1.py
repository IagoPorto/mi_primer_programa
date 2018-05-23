"""
Crea un programa que sea capaz de contar espacios, puntos y comas de ina string introducida por el usuario
"""

frase_usuario = input("Escribe una frase: ")

comas=0
espacios=0
puntos=0

for caracter in frase_usuario:
    if caracter == "," or caracter == " " or caracter == ".":
        if caracter == ",":
            comas+=1
        elif caracter ==" ":
            espacios+=1
        elif caracter ==".":
            puntos+=1

print("Has escrito {} punto(s), {} coma(s) y {} espacio(s)".format(puntos,comas,espacios))
