'''
https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem_cnt = Counter(nums)
        for elem in elem_cnt:
            if elem_cnt[elem] > len(nums) / 2:
                output = elem
        return output

    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        elem_cnt = Counter(nums)
        for elem in elem_cnt:
            if elem_cnt[elem] > len(nums) / 2 and elem == target:
                return True

        return False

    def majorityElements(self, nums: List[int]) -> List[int]:
        elem_cnt = Counter(nums)
        output=[]
        for elem in elem_cnt:
            if elem_cnt[elem] > len(nums) / 3:
                output.append(elem)
        return output






a = Solution()

print(a.majorityElement([3,2,3]))

print(a.isMajorityElement([2,4,5,5,5,5,5,6,6], 5))

print(a.majorityElements([1]))