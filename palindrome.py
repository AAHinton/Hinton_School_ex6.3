import sys
import os

def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def first_equals_last(a):
    if first(a) == last(a):
        return True
    else:
        return False

def is_odd_char(word):
    if len(word) %2 ==1:
        return True
    else:
        return False

def is_palindrome(word):
    if not first_equals_last(word) or not is_odd_char(word):
        return False
    else:
        if len(word) > 3:
            word=middle(word)
            return is_palindrome(word)
        elif len(word) ==3:
            return True
        else:
            return False
