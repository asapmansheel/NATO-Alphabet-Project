import pandas as pd

data = pd.read_csv('/Users/macintosh/Downloads/NATO-alphabet-start/nato_phonetic_alphabet.csv')

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input('Enter a word: ').upper()
    
    try:
        list = [nato_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
        print(list)

generate_phonetic()
