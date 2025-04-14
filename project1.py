import random

def getRan():
    return random.randint(0,9)

for i in range(0,3):
    number = getRan()
    print("Guess the number between [0 - 9], you have", 3 - i,  "traies!")
    guess = input("The number is:")
    if guess == number:
        print("Congratulations!! you got the right number Yay..")
        break
    else:
        print("Wrong try again!\n")
print("You consumed all your tries.. you lose -_-")
