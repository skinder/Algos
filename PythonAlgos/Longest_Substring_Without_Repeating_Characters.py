'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
'''

def lengthOfLongestSubstring(s: str) -> int:
    mp = {}
    start = 0
    end = len(s) - 1
    substr = final_str = ""
    while start <= end:
        if s[start] not in mp or s[start] not in substr:
            substr += s[start]
            mp[s[start]] = start
            start += 1
        else:
            if len(substr) > len(final_str):
                final_str = substr
            if start != end:
                substr = s[mp[s[start]] + 1:start + 1]
            mp[s[start]] = start
            start += 1
    if start >= end and len(substr) > len(final_str):
        final_str = substr
    return len(final_str)

print(lengthOfLongestSubstring('dvdf'))