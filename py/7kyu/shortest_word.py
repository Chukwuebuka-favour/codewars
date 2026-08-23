'''

Description:
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

'''

# MY SOLUTION
def find_short(s):
    s = s.split()
    word_length = []
    for l in s:
        word_length.append(len(l))
            
    return min(word_length)

#ALTERNATIVE SOLUTION
lambda s: min(len(l) for l in s.split())