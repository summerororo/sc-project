"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7

# Global variable
guesses_left = N_TURNS


def main():
    """
    a word guessing game
    """
    global guesses_left
    word = random_word()
    # guesses_left = 7
    new_word = ''
    for i in range(len(word)):
        # make the word into dashes
        new_word += '-'
    # print the icon
    print_the_icon()
    print('The word looks like: ' + str(new_word))
    print('You have ' + str(guesses_left) + ' guesses left.')
    while True:
        input_ch = input('Your guess: ')
        input_ch = input_ch.upper()
        if not input_ch.isalpha():
            print('illegal format')
        elif len(input_ch) > 1:
            print('illegal format')
        elif word.find(input_ch) == -1:
            guesses_left -= 1
            print('There is no ' + input_ch + "\'s in the word.")
            print_the_icon()
            print('The word looks like: ' + str(new_word))
            if guesses_left > 0:
                # to tell if still having guesses
                print('You have ' + str(guesses_left) + ' guesses left.')
            else:
                print('You are completely hung : (')
                print('The word was: ' + str(word))
                break
        else:
            print('You are correct!')
            print_the_icon()
            ans = ''
            for i in range(len(word)):
                ch = word[i]
                ch1 = new_word[i]
                if ch == input_ch:
                    ans += input_ch
                else:
                    ans += ch1
            new_word = ans
            if new_word.isalpha():
                # to tell if the word guessing is completed
                print('You win!!')
                print('The word was: ' + str(new_word))
                break
            else:
                print('The word looks like:' + str(new_word))
                print('You have ' + str(guesses_left) + ' guesses left.')


def icon_0():
    for i in range(8):
        print('=', end='')
    print('')
    for i in range(6):
        print('|')


def icon_1():
    for i in range(8):
        print('=', end='')
    print('')
    print('|    |')
    for i in range(5):
        print('|')


def icon_2():
    for i in range(8):
        print('=', end='')
    print('')
    print('|    |')
    print('|   ( )')
    for i in range(4):
        print('|')


def icon_3():
    for i in range(8):
        print('=', end='')
    print('')
    print('|    |')
    print('|   ( )')
    print('|    #')
    print('|    #')
    print('|')
    print('|')


def icon_4():
    for i in range(8):
        print('=', end='')
    print('')
    print('|    |')
    print('|   ( )')
    print('|  ~ # ~')
    print('|    #')
    print('|')
    print('|')


def icon_5():
    for i in range(8):
        print('=', end='')
    print('')
    print('|    |')
    print('|   ( )')
    print('|  ~ # ~')
    print('|    #')
    print('|   / \ ')
    print('|')


def icon_6():
    for i in range(8):
        print('=', end='')
    print('')
    print('|    |')
    print('|  (0.0)')
    print('|  ~ # ~')
    print('|    #')
    print('|   / \ ')
    print('|')


def icon_7():
    for i in range(8):
        print('=', end='')
    print('')
    print('|    |')
    print('|   (X)')
    print('|  ~ # ~')
    print('|    #')
    print('|   / \ ')
    print('|   Lose')


def print_the_icon():
    if guesses_left == N_TURNS:
        icon_0()
    elif guesses_left == N_TURNS-1:
        icon_1()
    elif guesses_left == N_TURNS-2:
        icon_2()
    elif guesses_left == N_TURNS-3:
        icon_3()
    elif guesses_left == N_TURNS-4:
        icon_4()
    elif guesses_left == N_TURNS-5:
        icon_5()
    elif guesses_left == N_TURNS-6:
        icon_6()
    elif guesses_left == N_TURNS-7:
        icon_7()


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
