'''Description:
Very simple, given a number, find its opposite (additive inverse).

Examples:

1: -1
14: -14
-34: 34'''

# MY SOLUTION
def opposite(number):
  # your solution here
    return abs(number) if number <=0 else -(number)

# BEST PRACTICE
def opposite(number):
    return -number