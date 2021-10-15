'''
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
'''

from typing import List

def findDisappearedNumbers(nums: List[int]) -> List[int]:
    check_set = set()
    result = []
    nums_set = set(nums)
    for i in range(len(nums)):
        check_set.add(i+1)
    for i in check_set:
        if i not in nums_set:
            result.append(i)
    return result

print(findDisappearedNumbers([1,1]))