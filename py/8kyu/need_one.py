'''
Description:
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

a can contain numbers or strings. x can be either.

Return true if the array contains the value, false if not.
'''

# MY SOLUTION
check = lambda seq, elem: elem in seq

# ALTERNATIVE SOLUTION
def check(seq, elem):
    return elem in seq