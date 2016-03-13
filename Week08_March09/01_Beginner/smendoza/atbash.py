#!/usr/bin/env python

'''
atbash.py

Author: Stefan Mendoza
Date: 12 March 2016

Implementation of the Atbash cipher.
'''

import string

###############################################################################

#############################
# Creation of Atbash Cipher #
#############################

reversed_alphabet = list(string.ascii_lowercase)
reversed_alphabet.reverse()

MAPPING = {}

for i in range(0, 26):
    MAPPING[string.ascii_lowercase[i]] = reversed_alphabet[i]

###############################################################################

def cipher(plain_text):
    c = ""
    for i in range(0, len(plain_text)):
        if MAPPING.get(plain_text[i]) is None:
            c += plain_text[i]
        else:
            c += MAPPING[plain_text[i]]
    return(c)

if __name__ == "__main__":
    plain = ""

    while True:
        plain = input("\nEnter a phrase to be encrypted: ").lower()

        if plain == "#quit":
            print("\nExiting.")
            break
        else:
            print("Encoded: " + cipher(plain))
