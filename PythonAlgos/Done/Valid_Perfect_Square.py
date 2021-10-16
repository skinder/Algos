'''
https://leetcode.com/problems/valid-perfect-square/
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''


class Solution(object):
    def isPerfectSquare(self, num):
        if num is None:
            return False
        if num in (0, 1, 2):
            return True

        left, right = 1, (num // 2) + 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid
            else:
                right = mid

        return False


a = Solution()

print a.isPerfectSquare(0)