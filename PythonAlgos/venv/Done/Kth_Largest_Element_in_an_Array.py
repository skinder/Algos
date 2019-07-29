'''
https://leetcode.com/problems/kth-largest-element-in-an-array/
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]

    def find3dmax(self, nums):
        st = list(set(nums))
        st.sort()
        if len(st) >= 3:
            return st[-3]
        else:
            return st[-1]

a = Solution()

print a.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print a.findKthLargest([3,2,1,5,6,4], 2)
print a.find3dmax([1,2])
print a.find3dmax([3, 2, 1])
print a.find3dmax([2, 2, 3, 1])


