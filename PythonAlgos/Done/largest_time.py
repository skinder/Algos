'''
https://leetcode.com/problems/largest-time-for-given-digits
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.



Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
'''


class Solution(object):
    def largestTimeFromDigits(self, A):
        from itertools import permutations
        k = list(permutations(sorted(A,reverse=True)))
        for i in k:
            a, b, c, d = i
            h = a * 10 + b
            m = c * 10 + d

            if h < 24 and m < 60:
                return str(a) + str(b) + ':' + str(c) + str(d)

        return ''


a = Solution()

print a.largestTimeFromDigits([1,2,3,4])
print a.largestTimeFromDigits([0,0,0,0])