'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1], 0) + nums[i]

        return max(nums)


a = Solution()

print a.maxSubArray([1,2,3,4])
print a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print a.maxSubArray([-3,-2])