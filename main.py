# Guess a number (computer)
import random


def guess(x):
    random_num = random.randint(1, x)
    myGuess = 0
    while myGuess != random_num:
        myGuess = int(input(f"Guess a number beween 1 and {x}: "))
        if myGuess < random_num:
            print("Sorry, guess again. Too low!")
        elif myGuess > random_num:
            print("Sorry, guess again. Too high!")

    print(f"You got it! You have guessed the number {random_num} correctly!!")


guess(10)
