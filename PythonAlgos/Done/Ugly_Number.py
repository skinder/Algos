'''
https://leetcode.com/problems/ugly-number/
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2,3,5

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 x 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 x 2 x 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
'''




class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False

        primes = [2, 3, 5]
        for prime in primes:
            while num % prime == 0:
                num /= prime
            if num == 1:
                return True
        return False


a = Solution()

print a.isUgly(15)