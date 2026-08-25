'''

Description

Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

'''

# MY SOLUTION
def solution(s):
    new = ""
    for c in s:
        if c.isupper():
            new += " "
        new += c
    return new

# ALTERNATIVE SOLUTION
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)