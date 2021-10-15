"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    input an integer other than 1, and make it become 1 in the end
    """
    print('This program computes Hailstone sequence.')
    a_random_integer = int(input('Enter an integer: '))
    count = 0
    while True:
        # see if the input number is equal to 1 ,an even number or an odd number
        if a_random_integer == 1:
            break
        if a_random_integer % 2 == 0:
            count += 1
            if_even = int(a_random_integer/2)
            if if_even == 1:
                print(str(a_random_integer) + ' is even, so I take half: ' + str(if_even))
                break
            else:
                print(str(a_random_integer) + ' is even, so I take half: ' + str(if_even))
                a_random_integer = if_even
        if a_random_integer % 2 == 1:
            count += 1
            if_odd = int(a_random_integer*3 + 1)
            if if_odd == 1:
                print(str(a_random_integer) + ' is odd, so I make 3n+1:  ' + str(if_odd))
            else:
                print(str(a_random_integer) + ' is odd, so I make 3n+1:  ' + str(if_odd))
                a_random_integer = if_odd
    print('It took ' + str(count) + ' steps to reach 1.')




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
