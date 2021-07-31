# https://www.geeksforgeeks.org/find-four-numbers-with-sum-equal-to-given-sum/
# https://leetcode.com/problems/4sum/

def fourNumberSum(array, targetSum):
    array.sort()
    print(array)
    result = []
    for i in range(len(array) - 3):
        for j in range(i + 1, len(array) - 2):
            k = j + 1
            l = len(array) - 1
            while k < l:
                sum = array[i] + array[j] + array[k] + array[l]
                if sum == targetSum:
                    result.append([array[i], array[j], array[k], array[l]])
                    k += 1
                    l -= 1
                elif sum < targetSum:
                    k += 1
                else:
                    l -= 1
    print(result)
    return result