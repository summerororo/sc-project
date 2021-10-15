"""
File: similarity.py
Name:
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    find the best match of the long DNA strand to the short dna strand
    """
    dna_long = input('Please give me a DNA sequence to search: ')
    dna_long = dna_long.upper()
    dna_short = input('What DNA sequence would you like to match? ')
    dna_short = dna_short.upper()
    maximum = 0
    # the maximum count of the similarity
    for i in range(len(dna_long) - len(dna_short) + 1):
        # loop over long dna
        count = 0
        # count the same base between long and short dna
        the_match = ''
        for j in range(len(dna_short)):
            # loop over short dna
            base_long = dna_long[i+j]
            base_short = dna_short[j]
            the_match += base_long
            if base_short == base_long:
                count += 1
        if count > maximum:
            maximum = count
            the_best_match = the_match
    print('The best match is ' + str(the_best_match))



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
