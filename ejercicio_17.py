"""
Crear un programa que sea capaz de encontrar el número más grande de una lista sin usar el max()
"""

list=[1,2,56,4,56,90,45,67,89]
biggest_number=0

for character in list:
    if character > biggest_number:
        biggest_number=character

print("{}".format(biggest_number))