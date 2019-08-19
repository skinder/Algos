'''
https://leetcode.com/problems/search-in-rotated-sorted-array/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)/2
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[l] > target and nums[l] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[r] < target and nums[r] >= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1



a = Solution()

print a.search([4,5,6,7,0,1,2], 0)