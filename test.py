from random import *

aRandomNumber = randint(1, 20)

#print(aRandomNumber)

tries = 1

while tries <= 3:
    tries += 1
    guess = input("Guess a number between 1 and 20 (inclusive): ")

    if not guess.isnumeric():
        print("That's not a positive whole number, try again!")
    else:
        guess = int(guess)
        if (guess < aRandomNumber):
            print("You should guess higher!")
            continue

        if (guess > aRandomNumber):
            print("You should guess lower!")
            continue

        if (guess == aRandomNumber):
            print("You got it, the number was " + str(aRandomNumber))
            break
