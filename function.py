
#defines a function to check for allowed characters
def char_check(user_letter):
    #user can choose only a one single letter
    if len(user_letter) != 1 or user_letter.isalpha() == False:
        print("Please write only one single letter as your guess. Words or numbers are not allowed.")
        return False
    else:
        return True

#compares the target word to the word guessed so far
def compare_target(one, two):
    one.sort()
    two.sort()
    if one == two:
        print("Sorted TRUE")
        return True
    else:
        print("Sorted FALSE")
        return False
