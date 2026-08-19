'''Description:
You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"
'''

# MY SOLUTION
def get_middle(s):
    return s[len(s) // 2] if len(s) % 2 == 1 else s[len(s) // 2 - 1: len(s) // 2 + 1]


# BEST PRACTICE
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]