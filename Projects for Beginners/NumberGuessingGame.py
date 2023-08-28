#!/usr/bin/env python
#Number Guessing Game
#Github: mammaddrik

#::::: Library :::::
import random
import os

def clearScr():
    "A Function To Clean Up The Command Prompt or Terminal."
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

clearScr()
number = random.randint(0,100)
guess = random.randint(1,10)

print(f"You've only {guess} chances to guess the number.")

count = 0

while (count < guess):
    count += 1
    numbers = int(input("\nGuess a Number: "))
    if (numbers > number):
        print("Your guessed too high!")
    elif (numbers < number):
        print("You guessed too small!")
    elif (numbers == number):
        print(f"Congratulations you did it in {count} try.\n")
        break

if count >= guess:
    print(f"\nThe number is {number}")