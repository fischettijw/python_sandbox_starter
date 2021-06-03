import random

import os
os.system('cls')

number_of_guesses = 0
secret_number = random.randint(0, 100+1)
guess = -1

while guess != secret_number:
    guess = int(input('Guess a number between 0 and 100 '))
    number_of_guesses += 1
    if guess == secret_number:
        print(
            f"You guessed the secret number {secret_number} in {number_of_guesses} guesses !!")
    elif guess > secret_number:
        print(f"Your guess ({guess}) is too HIGH ... guess again.")
    else:
        print(f"Your guess ({guess}) is too LOW ... guess again.")
