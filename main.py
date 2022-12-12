# Hangman from 12 Beginner Python Projects - Coding Course https://www.youtube.com/watch?v=8ext9G7xspg

import random
# Import specific functions from the `function.py` file
from function import char_check, compare_target

#reads an "words" text file into a list and picks a single play word
with open('words.txt', "r") as f:
    words = f.read().splitlines()
word: object = random.choice(words)
#splits the word into letters to check for each letter
word_letters = list(word)
print("Word is", word.upper())
print("Letters are", word_letters)

#creates a placeholder list to input correctly guessed letters
word_continue = list()
for placeholder in word_letters:
    word_continue.append("_") #makes the list same lenght as the word we looking for
#variables to store all used letter guesses
letters_used = list()
#number of lives user has at start
lives_left = 5

#start of the game
print("Hi, this is a game of Hangman! You will be guessing a word that has exactly", len(word_letters), "letters. Let's begin.")

#for loop to iterate each user's life until user runs out of lives or guesses the word correctly
while lives_left > 0:

    print("Target word so far: ", end="")
    i = 0
    for placeholder in word_continue:
        print(word_continue[i].upper()," ", end="")
        i = i+1
    print("")

    #prints used letters so far
    if any(letters_used):
        print("Letters used: ", end="")
        for letter in letters_used:
            print(letter.upper(), " ", end="")
        print("")

    #prompts user to guess a letter
    user_letter = str(input("Guess a letter: ")).lower()

    #allowed character check using written function
    while char_check(user_letter) != True:
        user_letter = str(input("Guess a letter: ")).lower()

    #checks whether the user's inputed letter is already in the list of letters tried
    while user_letter in letters_used:
        print("Sorry, but you've already used a letter ", user_letter.upper(), "- pick another one.")
        user_letter = str(input("Guess a letter: ")).lower()

    #checks whether guessed letters matches any letters in the word and if so, replaces the "_" character with the letter
    if user_letter in word_letters:
        for letter_index in range(len(word_letters)):
            if user_letter == word_letters[letter_index]:
                print("You've guessed the correct letter! GOOD JOB!")
                word_continue[letter_index] = user_letter
                #print("THIS:",word_continue[letter_index])
    #if it doesn't, take away one life from user
    else:
        lives_left = lives_left - 1

    #puts user's letter into the list
    if not user_letter in letters_used:
        letters_used.append(user_letter)
        print("Appended: ", user_letter)

    if compare_target(word_letters, word_continue) == True:
        print("YOU HAVE WON *** The target word was: ", word.upper(), " *** CONGRATULATIONS ***")
        exit()

    #print(word_letters)

    print("You have ", lives_left, " lives left")

#ending
if lives_left == 0:
    print("You've lost. The word was: ", word)
    print("--THE END--")
    exit()

endprint = "\n\n>>>|END OF PROGRAM|<<<"
print(endprint)


