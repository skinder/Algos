'''
https://leetcode.com/problems/product-of-array-except-self/
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up:

Could you solve it in O(n) time complexity and without using division?
Could you solve it with O(1) constant space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
from typing import List
import numpy

class Solution:
    def productExceptSelf_num(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(numpy.prod(nums[i+1:]))
            elif i == len(nums) - 1:
                output.append(numpy.prod(nums[0:i]))
            else:
                output.append(numpy.prod(nums[0:i] + nums[i+1:]))
        return output

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(self.mltArray(nums[i+1:]))
            elif i == len(nums) - 1:
                output.append(self.mltArray(nums[0:i]))
            else:
                output.append(self.mltArray(nums[0:i] + nums[i+1:]))
        return output

    def mltArray(self, input_list: List[int]):
        result = 1
        for i in input_list:
            result = result * i
        return result


a = Solution()
print(a.productExceptSelf([1,2,3,4]))



