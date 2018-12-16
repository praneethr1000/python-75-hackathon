'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
'''
from collections import Counter

def scramble(s1, s2):
    letters = Counter(s1)
    word = Counter(s2)
    diff = word - letters
    return len(diff) == 0