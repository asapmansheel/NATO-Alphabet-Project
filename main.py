import pandas as pd

data = pd.read_csv('/Users/macintosh/Downloads/NATO-alphabet-start/nato_phonetic_alphabet.csv')

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a word: ').upper()

list = [nato_dict[letter] for letter in word]
print(list)
