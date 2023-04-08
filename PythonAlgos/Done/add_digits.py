'''
https://leetcode.com/problems/add-digits/
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.


class Solution(object):
    def addDigits(self, num):
        num_lst = [int(x) for x in str(num)]
        num_sum = sum(num_lst)
        if num_sum <= 9 and num_sum >= -9:
            return num_sum
        else:
            self.addDigits(num_sum)





a = Solution()
print type(a.addDigits(38))
'''

class Solution(object):
    def addDigits(self, num):
        num_lst = [int(x) for x in str(num)]
        num_sum = sum(num_lst)
        if num_sum <= 9:
            return num_sum
        return self.addDigits(num_sum)

    def addDigits2(self, num):
        return num % 9



a = Solution()

print (a.addDigits(35555))
print (a.addDigits2(38))
print (a.addDigits2(35555))
