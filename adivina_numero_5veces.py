

number_to_guess = 5
times = 5

while times !=0:
    user_number=int(input("Adivina el numero del 0 al 10: "))
    if number_to_guess == user_number:
        print("Has gando campeón\n")
        times=0
    else:
        times -=1
        if times ==0:
            print("Has perdido imbecil\n")





