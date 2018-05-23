"""
Crear un programa que cambie todas las 'A' o 'a' por la strin 'VACA' de una string introducida por el usuario
"""

string_usuario=input("Escribe una frase: ")
mi_string="VACA"
frase_final=""
contador=0

for caracter in string_usuario:
    if caracter == "a" or caracter == "A":
        frase_final+=mi_string
    else:
        frase_final+=string_usuario[contador]
    contador+=1

print("{}".format(frase_final))