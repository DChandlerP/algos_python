# https://leetcode.com/problems/candy/

def candy(array):
    # Initialize the number of candies
    # Condition-1 Fulfilled as we gave 1 candy to everyone
    candies = [1] * len(array)
        
    # Calculate the candies needed to fulfill left condition     
    # We drop the 0th element as nothing is located left to it
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            candies[i] = candies[i-1] + 1
        
    # Calculate the candies needed to fulfill right condition  
    # We drop the last element as nothing is located right to it
    for i in range(len(array)-2, -1, -1):
        if array[i] > array[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
        
    # Take the summation --> Minimum candies
    return sum(candies)