"""
Localiza el número mas pequeño de una serie de números introducidos por el usuario
"""

numeros_usuario = []
comprobacion= ""

while len(numeros_usuario) < 10:
    while not comprobacion.isdigit():
        comprobacion=(input("Dime un número: "))
    numeros_usuario.append(comprobacion)
    comprobacion=""

numero_pequeño=numeros_usuario[0]

for num in numeros_usuario:
    if num<numero_pequeño:
        numero_pequeño=num

print("El número más pequeño es: {}".format(numero_pequeño))
