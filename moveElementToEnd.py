# https://leetcode.com/problems/move-zeroes/ but generalized
def moveZeroes(nums, element):
    anchor = 0
    for explorer in range(len(nums)):
        if nums[explorer] != element:
            nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
            anchor += 1
    return nums