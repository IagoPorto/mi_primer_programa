

number_to_guess=int(input("Dime el número a adivinar: "))
try_number=-23

while number_to_guess != try_number:
    try_number=int(input("Adivina el número: "))
    if try_number==number_to_guess:
        print("Has ganado")
