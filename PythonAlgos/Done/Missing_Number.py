'''
https://leetcode.com/problems/missing-number/
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1] 3*4/2 = 6
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

'''


class Solution(object):
    def missingNumber(self, nums):
        expected_sum = (len(nums)*(len(nums) + 1))/2
        the_sum = sum(nums)
        if the_sum == expected_sum:
            return 0
        return expected_sum - the_sum



a = Solution()

print a.missingNumber([9,6,4,2,3,5,7,0,1])
print a.missingNumber([3,0,1])