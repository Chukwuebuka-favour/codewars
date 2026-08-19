'''
Description:
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
'''

# MY SOLUTION
def is_isogram(string):
    string = string.lower()
    return True if len(string) == len(set(string)) else False


# BEST PRACTICES
is_isogram = lambda s: len(set(s.lower())) == len(s)

def is_isogram(string):
    return len(string) == len(set(string.lower()))

def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True