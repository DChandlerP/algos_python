import sys


import sys

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()     # Sort the array                
    arrayTwo.sort()     # Sort the array
    idx1 = 0   # Index of arrayOne                     
    idx2 = 0   # Index of arrayTwo
    diff = sys.maxsize   # Initialize the diff
    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
        if arrayOne[idx1] < arrayTwo[idx2]: # If the first number is smaller
            diff = min(diff, arrayTwo[idx2] - arrayOne[idx1])
            idx1 += 1   # Move the index of arrayOne
        else:   
            diff = min(diff, arrayOne[idx1] - arrayTwo[idx2])
            idx2 += 1   # Move the index of arrayTwo
    return diff
                                                      