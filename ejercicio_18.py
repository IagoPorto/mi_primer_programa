"""
Crea un programa que sea capaz de crear varias listas con los números de una lista del usuario que sean
 multiplos de 3, 5, 2 y 7
"""

user_list=[1,2,3,4,56,15,7,21,3,9,24,50,63,60,12]
multiplos2=[]
multiplos3=[]
multiplos5=[]
multiplos7=[]
cont=0

for item in user_list:
    if item % 2 == 0:
        multiplos2.append(user_list[cont])
    if item % 3 == 0:
        multiplos3.append(user_list[cont])
    if item % 5 == 0:
        multiplos5.append(user_list[cont])
    if item % 7 == 0:
        multiplos7.append(user_list[cont])
    cont+=1

print("Los multiplos de 2 son: {}".format(multiplos2))
print("Los multiplos de 3 son: {}".format(multiplos3))
print("Los multiplos de 5 son: {}".format(multiplos5))
print("Los multiplos de 7 son: {}".format(multiplos7))