# https://www.geeksforgeeks.org/find-smallest-value-represented-sum-subset-given-array/
# https://lei-d.gitbook.io/leetcode/math/smallest-non-constructible-value

def findSmallest(array):
    # linear search
    max_constructible = 0
    for a in sorted(array):
        if a > max_constructible + 1:
            break
        max_constructible += a
    return max_constructible + 1

