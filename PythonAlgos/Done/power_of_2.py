'''
https://leetcode.com/problems/power-of-two/
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

'''




class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        x = str(bin(n))[2:]
        if x.count("1") > 1:
            return False
        else:
            return True

    def isPowerOfFour(self, num):
        if num > 0:
            binary = str(bin(num))[2:]
            if binary.count('1') == 1:
                if binary.count('0') % 2 == 0:
                    return True
        return False

    def isPowerOfThree(self, n):
        if n <= 0:
            return False

        while n != 1:
            if n % 3 != 0:
                return False
            n = n / 3

        return True



a = Solution()

print a.isPowerOfTwo(16)
print a.isPowerOfFour(16)
print a.isPowerOfThree(9)