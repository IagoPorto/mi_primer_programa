"""
crea una programa que sea capaz de guardar el año de nacimiento de tus amigos y su nombre
"""
lista={}
consulta=""

while consulta != "c":
    consulta = ""
    while consulta != "a" and consulta != "b" and consulta != "c":
        consulta=input("¿Qué quieres hacer? [Añadir amig@(a), Consultar amig@(b), Salir (c)]: ")
    if consulta == "a":
        nombre=input("Dime su nombre: ")
        anho=input("Dime su año de nacimiento: ")
        lista[nombre]=anho
    elif consulta == "b":
        nombre = input("Dime su nombre: ")
        print("Su año de nacimiento es: {}".format(lista[nombre]))


