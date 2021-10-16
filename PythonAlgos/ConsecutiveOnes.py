'''
https://leetcode.com/problems/max-consecutive-ones/
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''

from typing import List
def findMaxConsecutiveOnes(nums: List[int]) -> int:
    result = current_max = 0
    for i in nums:
        if i == 1:
            current_max += 1
            result = max(result, current_max)
        else:
            current_max = 0
    return result


def сonsecutiveCharacters(s):
    result = current_max = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            current_max += 1
            result = max(result, current_max)
        else:
            current_max = 1
    return result


def longest(s):
    one_cnt = zero_cnt = zero_cur_max = one_curr_max = 0
    for i in s:
        if i == '1':
            one_curr_max += 1
            one_cnt = max(one_cnt, one_curr_max)
            zero_cur_max = 0
        else:
            zero_cur_max += 1
            zero_cnt = max(zero_cur_max, zero_cnt)
            one_curr_max = 0

    return one_cnt > zero_cnt

def mostOne(s):
    i = 0
    while i < len(s) and s[i] == '1':
        i += 1
    while i < len(s) and s[i] != '1':
        i += 1
    return i == len(s)

# print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
# print(сonsecutiveCharacters("tourist"))

# print(longest("111000"))
print(mostOne("1001"))
