'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        s_ln = len(s)
        if s_ln == 0:
            return False

        for i in range(s_ln):
            if s_ln % (i+1) != 0:
                continue
            if (i + 1) * 2 > s_ln:
                return False
            if (s.count(s[0:i+1]) * len(s[0:i+1])) == s_ln:
                return True

a = Solution()

print a.repeatedSubstringPattern('abcabcabcabc')