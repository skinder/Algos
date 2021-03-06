'''
https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

'''


class Solution(object):
    def firstUniqChar(self, s):
        from collections import Counter
        dc = Counter(s)
        for i in range(len(s)):
            if dc[s[i]] == 1:
                return i
        return -1





a = Solution()

print a.firstUniqChar("leetcode")
print a.firstUniqChar("loveleetcode")
print a.firstUniqChar("aaaaaa")