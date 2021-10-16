'''
https://leetcode.com/problems/ransom-note/
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransomNote_dict = Counter(ransomNote)
    magazine_dict = Counter(magazine)
    for key, value in ransomNote_dict.items():
        if key not in magazine_dict or value > magazine_dict[key]:
            return False
    return True


print(canConstruct("bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
