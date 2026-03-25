import art
import random

print(art.logo)
print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100\n")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
computer_guess = random.randint(1,100)

if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5 
else:
    print("Invalid input. Defaulting to 'easy'.")
    lives = 10

print(f"You have {lives} attempts to guess the number.")

while lives > 0 :
    human_guess = int(input("Make a guess: "))

    if human_guess > computer_guess :
        lives -= 1
        print(f"Too high. Guess again. {lives} lives remaining.")


    elif human_guess < computer_guess :
        lives -= 1
        print(f"Too low. Guess again. {lives} lives remaining.")

    else:
        print(f"You're right! The number was {computer_guess}. You had {lives} lives left.")
        break

    if lives == 0:
        print(f"You've run out of lives. The number was {computer_guess}")
