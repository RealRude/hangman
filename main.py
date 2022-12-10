# Hangman from 12 Beginner Python Projects - Coding Course https://www.youtube.com/watch?v=8ext9G7xspg

import random


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
print("Target word so far: ", end="")
for placeholder in word_continue:
    print("_ ", end="")
print("")

#for loop to iterate each user's life until user runs out of lives or guesses the word correctly
for i in range(lives_left):

    user_letter = str(input("Guess a letter: ")).lower()

    while len(user_letter) != 1 or user_letter.isalpha() == False:
        print("Please write only one single letter as your guess. Words or numbers are not allowed.")
        user_letter = str(input("Guess a letter: "))

    #checks whether the user's inputed letter is already in the list of letters tried
    if user_letter in letters_used:
        print("You've already used a letter ", user_letter.upper(), ", pick another one.")
    else:
        #puts user's letter into the list
        letters_used.append(user_letter)


    #checks whether guessed letters match the word
    #while

    print("Valid input")


    lives_left = lives_left - 1
    print("You have ", lives_left, " lives left")
    if lives_left == 0:
        print("You've lost. The word was: ", word)


exit()






endprint = "\n\n>>>|END OF PROGRAM|<<<"
print(endprint)


