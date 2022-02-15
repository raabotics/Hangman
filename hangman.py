# A game of "Hangman"

# Import modules
import os

import pandas as pd
import numpy as np
import random

# Define a clear "function"
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Load data from common_words_engl.csv
## Load data, drop irrelevant data and arrange in Numpy array
data = pd.read_csv("common_words_engl.csv", sep=",")
data = data[["Word"]]
data = np.array(data)

# Create a list that only contains words with a length > 4
list_data = []

for i in data:
    if len((i[0])) > 4:
        # print(i[0])
        list_data.append(i[0])
    else:
        continue

# print(len(list_data))
data = list_data


# Define possible input as the alphabet
possible_input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']


# Function that returns a random word from list
def generate_word():
    data_length = len(data)
    rand_index = random.randint(0, data_length)
    word = data[rand_index]
    return word

# Start a new round
def start_again():
    pass


# Generates a board and displays it
def generate_board(secret_word):
    space = len(secret_word)
    board = ["_"] * space
    print(" ".join(board))
    return board


# Function that lets the player interact with the game
def handle_turn():
    guess = input("Enter a guess:").lower()

    if guess in possible_input and len(guess) == 1:
        return guess
    else:
        while guess not in possible_input:
            print("Invalid input. Try again")
            guess = input("Enter a letter: ").lower()
            if guess in possible_input:
                return guess


# Function that checks if the input of the player matches a letter in the wanted word
def check_hit(guess, secret_word):

    if guess in secret_word:
        guess_position = [i for i, n in enumerate(secret_word) if n == guess]
        # print(guess_position)
        return guess_position

    else:
        print("\nWrong letter. Try again")
        return None


# Function that returns true as long as word has NOT been solved. Else returns false
def game_state(secret_list, hit_list):
    # Hit list contains all hits
    # the function compares the hit_list with the secret word
    if hit_list != secret_list:
        return True
    else:
        print("Congratulations! You won the game!")
        return False


# This is the main function
def play_game():
    fails = 0
    max_fails = 9
    used_letters = []

    game_still_going = True
    secret_word = generate_word()
    board = generate_board(secret_word)
    secret_list = list(secret_word)

    while game_still_going:  #
        guess = handle_turn()
        # prints a list with all used letters
        used_letters.append(guess)
        used_letters.sort()
        used_letters = list(dict.fromkeys(used_letters))
        print("Already used letters: {}".format(used_letters))

        position = check_hit(guess, secret_word)
        # print(position)

        if position is None:
            fails += 1
            print("Fails: {}/{}".format(fails, max_fails))
            print(" ".join(board))

            if fails == max_fails:
                print("\nSorry, you lost the game :(")
                print("The word we were looking for is {}".format(secret_word))
                game_still_going = False

        else:
            i = 0
            while i < len(position):
                board[position[i]] = guess
                # print(position[i]) # for verification only
                game_still_going = game_state(secret_list, board)
                i += 1
            print(" ".join(board))


# CALL MAIN FUNCTION and start the game
play_game()

# TODO: Add option to start a new game
# TODO: Add possibility to select and change game difficulty
# TODO: Do not count letters, that have already been used, as fail

