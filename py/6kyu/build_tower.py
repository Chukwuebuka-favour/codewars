'''

Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]

'''

# MY SOLUTION
def tower_builder(n_floors):
    result = [] #Create an empty array
    
    '''
    Loop through a range of value starting from 1 to the sum of int value 
    provided as param(n_floors) and 1
    ''' 
    for i in range(1, n_floors+1):
        
        '''
        Stores a string '*' in the variable row, this build the bricks on each
        row
        '''
        row = "*" * (2 * i - 1)
        
        #Add the row to result, centering it based on the width of the final row.
        result.append(row.center(2 * n_floors - 1))
    return result

# ALTERNATIVE SOLUTION
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

# def tower_builder(n_floors):
#     if n_floors == 0:
#         return []
    
#     # count = 1
#     result = []

#     for i in range(1, n_floors + 1):
#     	stars = '*' * (2 * i - 1)
#         space = ' ' * (n_floors - i)
#         result.append(space + stars + space)
#     return result