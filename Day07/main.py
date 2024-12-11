import random
from hangman_art import logo, stages
from hangman_words import word_list

lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(chosen_word)
print(word_length)

underscores = ""

for number in range(word_length):
    underscores += "_"
print(f"Word to guess: {underscores}")

correct_letters = []

game_over = True

while game_over:

    display = ""

    guess = input("Guess a letter: ")

    if guess in correct_letters:
        print(f"You already guessed {guess}.")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"Word to guess " + display)

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = False

    if "_" not in display:
        game_over = False
        print("You win!")

    print(stages[lives])