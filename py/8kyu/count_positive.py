'''

Description:
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

'''

# MY SOLUTION
def count_positives_sum_negatives(arr):
    positive, negative_sum = 0, 0
    
    if arr:
        for n in arr:
            if n > 0:
                positive += 1
            else:
                negative_sum += n
        return [positive, negative_sum]
    else:
        return []


# ALTERNATIVE SOLUTION(S)
def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

def count_positives_sum_negatives(arr):
    return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []