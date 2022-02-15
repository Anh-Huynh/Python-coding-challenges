# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation). Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphabet = set(alphabet)
    words = set(str1.replace(' ', '').lower())
    return words==alphabet