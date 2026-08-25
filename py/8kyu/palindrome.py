'''

Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.

'''

# MY SOLUTION
'''
''.join(list(s.lower()).reverse()) returns none
''.join(reversed(s.lower())) returns a merged string
'''
is_palindrome = lambda s: True if ''.join(reversed(s.lower())) == s.lower() else False

# ALTERNATIVE SOLUTION
def is_palindrome(s):
    #The return is evaluating a condition
    # It will return True if lowercase of the s is equal to the slice(no start, no
    #  stop indicated and step is -1 meaning move backward) of the lowercase of the s 
    # if that ain"t the case it returns False
    return s.lower() == s.lower()[::-1] 