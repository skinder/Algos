'''
https://leetcode.com/problems/move-zeroes/
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pivot],nums[i] = nums[i], nums[pivot]
                pivot += 1
        return nums


a = Solution()

print a.moveZeroes([0,1,0,3,12])