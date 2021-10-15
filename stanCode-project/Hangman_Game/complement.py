"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    find the complement of the DNA strand
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    dna_up_low = dna.upper()
    new_dna = build_complement(dna_up_low)
    print('The complement of is ' + str(dna_up_low) + ' is ' + str(new_dna))


def build_complement(dna_up_low):
    """
    :param dna_up_low: upper case dna strand
    :return: the complement of the dna strand
    """
    ans = ''
    for base in dna_up_low:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans






###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
