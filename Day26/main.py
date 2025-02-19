import pandas

data = "nato_phonetic_alphabet.csv"
alphabet = pandas.read_csv(data)
alphabet_dictionary = {row.letter:row.code for (index, row) in alphabet.iterrows()}

user_word = input("Enter a word: ").upper()
result = [alphabet_dictionary[letter] for letter in user_word if letter in alphabet_dictionary]
print(result)