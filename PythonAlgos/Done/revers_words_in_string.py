'''
https://leetcode.com/problems/reverse-words-in-a-string-iii/
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''

class Solution(object):
    def rvr(self, elm):
        reverted = []
        for i in range(len(elm)-1,-1,-1):
            reverted.append(elm[i])
        s = ''.join(reverted)
        return s


    def reverseWords(self, s):
        output = []
        lst = s.split(" ")
        for i in lst:
            output.append(self.rvr(i))
        return ' '.join(output)



a = Solution()
print a.rvr("abc")
print a.reverseWords("Let's take LeetCode contest")