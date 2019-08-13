'''
https://leetcode.com/problems/find-the-duplicate-number/
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
'''


class Solution(object):
    def findDuplicate(self, nums):
        from collections import Counter
        input = Counter(nums)
        for key in input.keys():
            if input[key] > 1:
                return key


a = Solution()

print a.findDuplicate([1,3,4,2,2])