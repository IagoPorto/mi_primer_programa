"""
Crea una función que sea capaz de encontrar el número más grande entre 3 números
"""

def numero_grande(numb1, numb2, numb3):
    resultado = 0
    if numb1 > numb2:
        if numb1 > numb3:
            resultado = numb1
        else:
            resultado = numb3
    elif numb2 > numb3:
        resultado = numb2
    else:
        resultado = numb3
    return resultado

mi_numero = numero_grande(-3, 94, 5)

print("{}".format(mi_numero))
