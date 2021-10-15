'''
https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

'''

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        anagrams.append(strs[0])
        anagram_dict = {''.join(sorted(strs[0])): anagrams}
        output = []

        for i in range(1,len(strs)):
            if ''.join(sorted(strs[i])) in anagram_dict:
                anagram_dict[''.join(sorted(strs[i]))].append(strs[i])
            else:
                anagram_dict[''.join(sorted(strs[i]))] = [strs[i]]

        for key, value in anagram_dict.items():
            output.append(value)

        return output


a =Solution()
print(a.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))