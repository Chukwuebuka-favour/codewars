'''

DESCRIPTION

Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

Square all numbers k (0 <= k <= n) between 0 and n.

Count the numbers of digits d used in the writing of all the k**2.

Implement the function taking n and d as parameters and returning this count.

Examples:
n = 10, d = 1 
the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

The function, when given n = 25 and d = 1 as argument, should return 11 since
the k*k that contain the digit 1 are:
1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
So there are 11 digits 1 for the squares of numbers between 0 and 25.
Note that 121 has twice the digit 1.

'''

# MY SOLUTION
def nb_dig(n, d):
    #n is greater than or equal to 0
    #d is greater than or equal to 0 and less than or equal to 9
    counts = 0
    if (n >= 0) and (0 <= d <= 9):
        for num in range(n+1):
            sq = num * num
            current_number = str(sq)
            counts += current_number.count(str(d))
        return counts


# ALTERNATIVE SOLUTION
def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))

def nb_dig(n, d):
   return ''.join(str(n * n) for n in range(n + 1)).count(str(d))

print(nb_dig(4,1))