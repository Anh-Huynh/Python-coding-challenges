# Write a Python function that checks whether a word or phrase is palindrome or not. A palindrome is word, phrase, or sequence that reads the same backward as forward

def palindrome(s):
    s = s.replace(' ', '')
    return s == s[::-1]