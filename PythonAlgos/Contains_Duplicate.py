'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for ind, i in enumerate(nums):
            if i not in d:
                d[i] = ind
            else:
                if ind - d[i] <= k:
                    return True
                d[i] = ind
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for i in nums:
            if i not in d:
                d.add(i)
            else:
                return True
        return False



a = Solution()

print(a.containsNearbyDuplicate([1,0,1,1], 1))

print(a.containsDuplicate([1,2,3,4]))

