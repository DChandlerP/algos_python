# https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums):
    anchor = 0
    for explorer in range(len(nums)):
        if nums[explorer] != 0:
            nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
            anchor += 1
    return nums