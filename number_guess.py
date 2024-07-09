
import random

def number_guess():
    y = random.randint(1, 100)
    attempts = 10

    print("Guess a number between 1 and 100.")

    while attempts > 0:
        x = int(input("Enter your guess: "))

        if x == y:
            print(f"Congratulations! You've guessed the right number {y}. You won!")
            return
        elif x < y:
            print("The right number is greater. Try again.")
        else:
            print("The right number is smaller. Try again.")

        attempts -= 1
        print(f"Attempts left: {attempts}")

    print(f"Sorry, no more attempts. The correct number was {y}. You lost.")

number_guess()
