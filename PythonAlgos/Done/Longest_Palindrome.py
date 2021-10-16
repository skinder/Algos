'''
\https://leetcode.com/problems/longest-palindrome/
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''


from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        count = Counter(s)
        n = 0
        for key in count:
            n += count[key]/2 *2
        return n if n == len(s) else n+1






a = Solution()

print a.longestPalindrome("abc")
print a.longestPalindrome("ccc")
print a.longestPalindrome("cccbbb")
print a.longestPalindrome("abccccdd")


