"""
Crear un programa que sustituya las vocales de string introducida por el usuario por su número de aparición
"""

string=input("Escribe una frase: ")
frase_final=""
aparicion_vocal=1
contador=0

for caracter in string:
    caracter=caracter.lower()
    if caracter=="a" or caracter=="e" or caracter =="i" or caracter=="u" or caracter =="o":
        frase_final+=str(aparicion_vocal)
        aparicion_vocal+=1
    else:
        frase_final+=string[contador]
    contador+=1

print("{}".format(frase_final))