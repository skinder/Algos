'''
https://leetcode.com/problems/add-strings/
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution(object):
    def addStrings(self, num1, num2):
        return str(self.strToInt(num1) + self.strToInt(num2))


    def multiply(self, num1, num2):
        return str(self.strToInt(num1) * self.strToInt(num2))


    def strToInt(self, num):
        my_dict = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        intNum = 0
        for ele in num:
            intNum = intNum * 10 + my_dict[ele]
        return intNum



a = Solution()

print a.multiply('2','3')
print a.addStrings('2','3')