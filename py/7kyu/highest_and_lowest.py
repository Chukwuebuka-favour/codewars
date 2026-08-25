'''

Description:
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.

'''


# MY SOLUTION
def high_and_low(numbers):
    arr=[]
    for num in numbers.split():
        arr.append(int(num))
    return f"{max(arr)} {min(arr)}"

high_and_low = lambda numbers: f"{max([int(num) for num in numbers.split()])} {min([int(num) for num in numbers.split()])}"

# print(high_and_low("1 2 3 4 5"))

# ALTERNATIVE SOLUTION
def high_and_low(numbers):
  return " ".join(x(numbers.split(), key=int) for x in (max, min))