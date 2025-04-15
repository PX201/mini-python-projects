import random

number = random.randint(0,9)
for i in range(0,3):
    print("Guess the number between [0 - 9], you have", 3 - i,  "tries!")
    try:
        guess = int(input("The number is:"))
        if guess == number :
            print("Congratulations!! you got the right number! Yay")
            break
        elif i < 2 :
            print("Wrong try again!\n")
        else :
            print(f"You consumed all your tries.. you lose -_- the number was {number}")
    except ValueError: 
        print("Please enter a valid number")


