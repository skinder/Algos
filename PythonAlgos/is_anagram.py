'''
https://leetcode.com/problems/valid-anagram/submissions/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''

from collections import Counter
def isAnagram(s: str, t: str):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

print(isAnagram("rat", "car"))
