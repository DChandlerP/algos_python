# Find the first repeating element in an array of integers
# Input: arr[] = {1, 2, 3, 3, 2, 1} 
# Output: 3
def firstDuplicate(arr):
    # Write your code here.
    d = {}
    for i in arr:
        if i in d:
            return i
        else:
            d[i] = 1
    return -1