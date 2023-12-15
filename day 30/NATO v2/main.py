import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}

word_input = input("Enter a word : ").upper()


def generate_phonetic():
    try:
        modified_word = [new_dictionary[letter] for letter in word_input]
    except KeyError:
        print("Sorry , only letters in the alphabets please .")
        generate_phonetic()
    else:
        print(modified_word)


generate_phonetic()
