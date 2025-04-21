import random

def roll():
    minValue = 1
    maxValue = 6
    roll = random.randint(minValue, maxValue)

    return roll

while True:
    players = input("Enter the number of the players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4")

    else:
        print("Invalid, try again!")

maxScore = 50
scores  = [0 for _ in range(players)]
winer = 0
while max(scores) < maxScore:
    for playerIdx in range(players):
        currentScore = 0
        print("\nPlayer ", playerIdx + 1, "turn has just started!\n")
        while True:
            shouldRoll = input("Would you like to roll (y)(n)?")
        
            if shouldRoll.lower() != "y":
                break
            value = roll()
            
            if value == 1:
                print("You rolled a 1! Turn done!")
                currentScore = 0
                break
            else:
                currentScore += value
                print("You rolled a: ", value)
            
            print("Your score is:", currentScore)
        
        scores[playerIdx] += currentScore
        print("Your total scores:", scores[playerIdx])
winner = scores.index(max(scores))
print("Congratulations! Player", winner + 1, "wins with", scores[winner], "points!")

