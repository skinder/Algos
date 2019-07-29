'''
https://leetcode.com/problems/two-sum/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''


class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for ind, i in enumerate(nums):
            if i not in d:
                d[target - i] = ind
            else:
                return [d[i], ind]


a = Solution()

print a.twoSum([-3,4,3,90], 0)
print a.twoSum([0,4,3,0], 0)
print a.twoSum([2, 7, 11, 15], 9)
print "------"
