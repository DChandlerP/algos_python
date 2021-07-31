
def longestConsecutiveSequence(nums):
    nums = set(nums)
    max_len = 0
    while nums:
        n = nums.pop()
        i = n + 1
        while i in nums:
            nums.remove(i)
            i += 1
        max_len = max(max_len, i - n)
    return max_len