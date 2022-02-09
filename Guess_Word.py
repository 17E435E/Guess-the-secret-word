import random
from nltk.corpus import words

def dashes(secret_word):

    dash = ""
    for letter in secret_word:
        dash = dash + "-"

    return dash

def update_dashes(secret_word, dash, guess):

    updated_dash = ""
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            updated_dash = updated_dash + secret_word[i]
        else:
            updated_dash = updated_dash + dash[i]

    return updated_dash

def guess(secret_word, word):

    attemp = 5
    while attemp > 0 and word != secret_word:

        print(word)

        guess = input("Guess : ")
        if len(guess) == 1:
            try:
                secret_word.index(guess)
                word = update_dashes(secret_word, word, guess)

            except ValueError:
                attemp -= 1
                print(f"{attemp} attemp left")

        else:
            if guess == secret_word:
                word = guess

            else:
                attemp -= 1
                print(f"{attemp} attemp left")

    return attemp

def main():
    
    rand = random.randint(0,len(words.words('en')))
    secret_word = words.words()[rand]
    word = dashes(secret_word)
    attemp = guess(secret_word, word)
    if attemp > 0:
        print("There is a winner")

    else:
        print(f"LOOSER. It was {secret_word}")

main()