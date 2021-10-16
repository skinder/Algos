'''
https://leetcode.com/problems/length-of-last-word/
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''

class Solution:
    def lengthOfLastWord(self, s):
        output = s.split(" ")
        for i in range(len(output)-1, -1,-1):
            if len(output[i]) > 0:
                return len(output[i])

        return 0


result = Solution()
print result.lengthOfLastWord("Hello World")
