'''

Description:
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F

'''

# MY SOLUTION

def initials(names):
    names = names.split(" ")
    initial= ''
    for name in names:
        if initial:
            initial +=  '.' + name[0].upper()
        else:
            initial += name[0].upper()
    return initial

# print(initials("agu chukwuebuka"))
# print(initials("agu chukwuebuka Godsfavour"))

# ALTERNATIVE SOLUTION

initials = lambda names: '.'.join(name[0].upper() for name in names.split())

print(initials("agu chukwuebuka"))
print(initials("agu chukwuebuka Godsfavour"))

