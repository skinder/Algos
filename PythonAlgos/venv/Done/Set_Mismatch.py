'''
https://leetcode.com/problems/set-mismatch/
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then
find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
'''

class Solution(object):
    def findErrorNums(self, nums):
        output= []
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                output.append(nums[i-1])
                if i < len(nums) - 1:
                    output.append(nums[i]+1)
                    break
                else:
                    output.append(nums[i]-1)
                    break

        return output







a = Solution()

print a.findErrorNums([1,2,2,4])
print a.findErrorNums([2,2])
print a.findErrorNums([1,1])
print a.findErrorNums([3,3])
