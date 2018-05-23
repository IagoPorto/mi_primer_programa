"""
Crea un programa que sea capaz de contar la cantidad de letras mayúsculas y minúsculas de una string introducida por el usuario
"""

frase_usuario=input("Escribe una frase: ")

mayusculas=0
minusculas=0
comprobacion=""

for caracter in frase_usuario:
    comprobacion=caracter.upper()
    if caracter != " " and caracter != "." and caracter != "," and caracter != ";" and caracter != ":" and caracter !="-" and caracter != "?":
        if caracter == comprobacion:
            mayusculas+=1
        else:
            minusculas+=1

print("Has escrito {} mayúscula(s) y {} minúscula(s)".format(mayusculas,minusculas))