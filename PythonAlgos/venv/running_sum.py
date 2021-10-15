from typing import List

'''
https://leetcode.com/problems/running-sum-of-1d-array/

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.


Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

'''



class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        result_list = []
        running_sum = 0
        for i in nums:
            running_sum = running_sum + i
            result_list.append(running_sum)

        return result_list

a = Solution()

print(a.runningSum([3,1,2,10,1]))