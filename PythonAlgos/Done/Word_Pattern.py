'''
https://leetcode.com/problems/word-pattern/
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.


class Solution(object):
    def wordPattern(self, pattern, str):

'''


class Solution(object):
    def wordPattern(self, pattern, str):
        d = {}
        str = str.split()
        if len(str) <> len(pattern):
            return False
        added_words = []
        zip_str = zip(pattern, str)
        for p, s in zip_str:
            if p in d and d[p] == s:
                continue
            elif s in added_words:
                return False
            elif p in d:
                return False
            else:
                d[p] = s
                added_words.append(s)
        return True

a = Solution()
print a.wordPattern("abba", "dog cat dog cat")