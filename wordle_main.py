""" imports """
import random
import sys
from termcolor import colored
import nltk
from nltk.corpus import words

nltk.download('words')

""" Menu """


def print_menu():
    print("Wordle Practice!")
    print("Let's get started!")
    print("Type a 5 letter word and hit enter!\n")


""" Select random word"""

"""
commenting out original list of words


def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)
"""

""" Create game """

nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]
print(len(words_five))
print_menu()
play_again = ""
while play_again != "q":
    word = random.choice(words_five).lower()
    for attempt in range(1, 7):
        guess = input().lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        print()

        if guess == word:
            print(colored(f"Congratulations! You got the word in {attempt}", 'blue'))
            break
        elif attempt == 6:
            print(f"Sorry the wordle was: {word}")
    play_again = input("Play again? Type q to quit. ")
