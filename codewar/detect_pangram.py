# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string
def pangram(str):
    alphabet = set(string.ascii_lowercase)
    return set(str.lower()) >= alphabet
