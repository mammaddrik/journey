#!/usr/bin/env python
#Hangman Game
#Github: mammaddrik

#::::: Library :::::
import os
import random


def clearScr():
    "A Function TO Clean Up The Command Prompt or Terminal."
    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")
        
clearScr()
someWords = "apple orange cherry banana grape papaya mango strawberry lemon peach lychee coconut"
someWords = someWords.split(" ")
word = random.choice(someWords)
print("Guess the fruit!")

guesses = ""
turns = len(word) + 2
print(f"You have {turns} turns.")
try:
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else: 
                print("_", end=" ")
                failed += 1
        if failed == 0:
            print("\nYou win!")
            print(f"The word is {word}")
            break
        guess = input("\n\nguess a letter: ").lower()
        try:
            if len(guess) > 1:
                clearScr()
                print("Enter only a letter!")
                turns -= 1
                print(f"You have {turns} more guess")
                continue
            elif guess not in word:
                clearScr()
                turns -= 1
                print("Enter only a letter!")
                print(f"You have {turns} more guess")
                if turns == 0:
                    clearScr()
                    print(f"The word was: {word}")
            elif guess in guesses:
                clearScr()
                print("You have already guessed that letter.p")
                print(f"You have {turns} more guess")
            else:
                clearScr()
                print(f"You have {turns} more guess")
            guesses += guess
        except:
            print('Enter only a Letter!')
            continue
except KeyboardInterrupt:
    exit()