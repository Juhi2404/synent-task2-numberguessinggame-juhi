# Number Guessing Game (CLI)

import random

print("Welcome to Number Guessing Game!")

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed the number.")
            print("Total attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid number!")