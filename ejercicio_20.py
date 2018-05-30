"""
Crea una función que dado un número y un rango diga si el número está dentro del rango o no
"""

def rango (numero, rango1, rango2):
    if numero >= rango1 and numero <= rango2:
        resultado = True
    else:
        resultado = False
    return resultado

mi_numero = rango(3, 3, 9)

print("{}".format(mi_numero))