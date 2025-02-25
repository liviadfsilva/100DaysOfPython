import pandas

data = "nato_phonetic_alphabet.csv"
alphabet = pandas.read_csv(data)
alphabet_dictionary = {row.letter:row.code for (index, row) in alphabet.iterrows()}

no_word = True

while no_word:
    user_word = input("Enter a word: ").upper()
    try:
        result = [alphabet_dictionary[letter] for letter in user_word]
        no_word = False
    except KeyError:
        print("Only one word is allowed. Try again.")
    else:
        print(result)