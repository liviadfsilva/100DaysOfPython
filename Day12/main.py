from random import randint
from art import logo

random_number = randint(1, 100)


def make_guess(attempts):
    game_over = False

    while not game_over:
        guess = int(input("Make a guess: "))

        if guess < random_number:
            attempts += -1
            if attempts == 0:
                print("You've run out of guesses. Refresh the page to play again.")
                game_over = True
            else:
                print("Too low.\n"
                      "Guess again.\n"
                      f"You have {attempts} attempt(s) remaining to guess the number.")
        elif guess > random_number:
            attempts += -1
            if attempts == 0:
                print("You've run out of guesses. Refresh the page to play again.")
                game_over = True
            else:
                print("Too high.\n"
                      "Guess again."
                      f"You have {attempts} attempt(s) remaining to guess the number.")
        else:
            print(f"You got it! The answer was {random_number}.")
            game_over = True

print(logo)
print("Welcome to the Number Guessing Game!\n"
      "I'm thinking of a number between 1 and 100.")
difficulty = input("Type a difficulty, 'easy' or 'hard': ").lower().strip()

def easy_level():
    easy_attempts = 10
    print(f"You have {easy_attempts} attempt(s) remaining to guess the number.")
    make_guess(easy_attempts)

def hard_level():
    hard_attempts = 5
    print(f"You have {hard_attempts} attempt(s) remaining to guess the number.")
    make_guess(hard_attempts)


if difficulty == "easy":
    easy_level()
else:
    hard_level()