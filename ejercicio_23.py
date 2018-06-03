"""
Crea un programa que al decirle el nombre de un color nos devuelva su traducción en inglés
"""

colors = {"rojo": "red", "azul": "blue", "green": "verde", "rosa": "pink"}
choose = None
choose_2 = 0

while choose != 3:

    while choose != 1 and choose != 2 and choose != 3:
        choose = int(input("¿Qué quieres hacer?: \n\t1) Obtener traducción \n\t2) Añadir color \n\t3) Salir "))

    if choose == 1:
        name_color = input("Dime el color: ")
        keys = colors.keys()
        for item in keys:
            if name_color == item:
                print(colors[name_color])
                choose_2 = 1
                choose = 0
        if choose_2 != 1:
            choose = None
            while choose != 2 and choose != 3:
                choose = int(input("No se ha encontrado el color, ¿quieres añadirlo? (pulsa 2 para añadir o 3 para salir): "))
        choose_2 = 0
    elif choose == 2:
        name_color = input("Dime el nombre del color en español: ")
        keys = colors.keys()
        for item in keys:
            if name_color == item:
                print("El color ya está en la base de datos")
                choose_2 = 1
                choose = 0
        if choose_2 != 1:
            translation = input("Dime la traducción del color : ")
            colors[name_color] = translation
            print("El color ha sido añadido")
            choose = 0
            choose_2 = 0
    else:
        pass



