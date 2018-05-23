"""
Crea un programa que muestre una string por pantalla con todas las vocales introducidas por una frase del usuario
"""

frase_usuario=input("Escribe una frase: ")

vocales=""

for caracter in frase_usuario:
    caracter=caracter.lower()
    if caracter == "a" or caracter == "e" or caracter == "o" or caracter == "i" or caracter == "u":
        vocales+=caracter+", "

print("Tus vocales son: {}".format(vocales))