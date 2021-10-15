'''
https://leetcode.com/problems/isomorphic-strings/
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''

from collections import Counter
def isIsomorphic(s: str, t: str):
    if len(s) != len(t):
        return False
    s_dict = Counter(s)
    t_dict = Counter(t)
    s_cnt = []
    t_cnt = []
    for k, v in s_dict.items():
        s_cnt.append(v)

    for k, v in t_dict.items():
        t_cnt.append(v)

    return sorted(s_cnt) == sorted(t_cnt)

print(isIsomorphic("fffcccfc", "aaabbbba"))
# "bbbaaaba", "aaabbbba"