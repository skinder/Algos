'''
https://leetcode.com/problems/intersection-of-two-arrays/
Given two arrays, write a function to compute their intersection.

Discussed 3 ways of solving this problem (HashSet, Two Pointers and Binary Search), time and space complexity clarification then choose one to code

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.


Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


'''

from collections import Counter

class Solution(object):
    def intersection(self, nums1, nums2):
        return set(nums1) & set(nums2)




a = Solution()
print a.intersection([1,2,2,1], [2,2])
print a.intersection([4,9,5], [9,4,9,8,4])


class Solution2(object):
    def intersection(self, nums1, nums2):
        res = []
        for i in nums2:
            if i in nums1:
                res.append(i)
                nums1.remove(i)
        return res

a = Solution2()
print a.intersection([1,2,2,1], [2,2])
print a.intersection([4,9,5], [9,4,9,8,4])