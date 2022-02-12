#!/usr/bin/env python3

from random import randint


if __name__ == "__main__":
    count = 0
    rand = randint(1, 99)
    print("This is an interactive guessing game!\
\nYou have to enter a number between 1 and 99 to find out the secret number.\
\nType 'exit' to end the game.\
\nGood luck!\
\n")
    while (True):
        guess = input("What's your guess between 1 and 99?\
\n>> ")
        if (guess == 'exit'):
            print("Goodbye!")
            exit()
        if (not guess.isnumeric()):
            print("That's not a number.")
            count += 1
        else:
            if (int(guess) == rand and not count):
                if (rand == 42):
                    print('The answer to the ultimate question of life\
, the universe and everything is 42.')
                print("Congratulations! You got it on your first try!")
                exit()
            elif (int(guess) == rand):
                if (rand == 42):
                    print('The answer to the ultimate question of life\
, the universe and everything is 42.')
                print(f"Congratulations, you've got it!\n\
You won in {count + 1} attempts!")
                exit()
            elif (int(guess) > rand):
                print("Too high!")
            else:
                print("Too low!")
            count += 1
