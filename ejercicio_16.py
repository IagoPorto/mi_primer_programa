"""
Hacer el ejercicio de FizzBuzz pero si es multiplo de 3 y de 5 añadir la palabra "Bazinga"
"""

user_list=[1,2,3,4,5,6,50,60,63,80,15,25,9]
final_list=""
cont=0

for character in user_list:
    if character%3==0 and character%5==0:
        final_list+="Bazinga"
    elif character%3==0:
        final_list+="Fizz"
    elif character%5==0:
        final_list+="Buzz"
    final_list+=str(user_list[cont])
    cont+=1

print("{}".format(final_list[cont]))
