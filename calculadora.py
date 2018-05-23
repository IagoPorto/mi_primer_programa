

operation=input("Dime la operación (multiplicacion, suma, resta, division):")
first_number=float(input("Primer número: "))
second_number=float(input("segundo número: "))

if operation == "multiplicacion":
    result=first_number*second_number
    print("el resultado es: {}".format(result))
elif operation == "suma":
    result=first_number+second_number
    print("el resultado es: {}".format(result))
elif operation=="resta":
    result=first_number-second_number
    print("el resultado es: {}".format(result))
elif operation=="division":
    result=first_number/second_number
    print("el resultado es: {}".format(result))
else:
    print("La operación está mal introducida")

