"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    unfold the secret message
    """
    secret_number = int(input('Secret number? '))
    new_a = new_alphabet(secret_number)
    ciphered_string = input("What's the ciphered string?")
    ciphered_string = ciphered_string.upper()
    the_secret = ''
    for i in range(len(ciphered_string)):
        # loop over the ciphered message
        if ciphered_string[i] != ' ':
            the_secret += ALPHABET[new_a.find(ciphered_string[i])]
        else:
            the_secret += ' '
    print('The deciphered string is: ' + the_secret)


def new_alphabet(secret_number):
    """
    :param secret_number: how far the alphabet move horizontally
    :return: the modified alphabet
    """
    ans = ''
    ans = ALPHABET[26 - secret_number:] + ALPHABET[:(26 - secret_number)]
    return ans












#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
