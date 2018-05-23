"""
Crear un  programa  que le repita al usuario todo lo que dice pero con las vocales cambiadas por 'i'
"""

string_usuario=input("Dime una frase (si es 'FIN' el programa acabará): ")
frase_final=""
contador=0

while string_usuario!="FIN":
    for item in string_usuario :
        if item=="a" or item=="A"or item=="e" or item=="E" or item == "u"or item =="U" or item=="o" or item=="O" :
            frase_final+="i"
        else:
            frase_final+=string_usuario[contador]
        contador+=1
    contador=0
    print("{}".format(frase_final))
    frase_final=""
    string_usuario = input("Dime una frase (si es 'FIN' el programa acabará): ")