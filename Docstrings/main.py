def number_of_letters(word):
    """Takes the word the user typed, counts
    how many letter it has and returns
    whether it's a long word or short word."""
    word_length = len(word)
    if word_length > 10:
        return f"{word} has {word_length} letters. It's a long word."
    else:
        return f"{word} has {word_length} letters. It's a short word."

print("Greetings, word explorer!\n"
      "Let’s dive into the world of words and find out: long or short?")
print(number_of_letters(input("What word would you like to check?\n")))