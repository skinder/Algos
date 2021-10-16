'''
https://leetcode.com/problems/group-anagrams/
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution(object):
    def anagram_check(self, str1, str2):
        value = 0
        if len(str1) == len(str2):
            for i in range(len(str1)):
                value = value ^ ord(str1[i])
                value = value ^ ord(str2[i])
        else: return False

        return value == 0


    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return -1
        if len(strs) == 1:
            return [strs]

        output = []
        output.append([strs[0]])

        for i in strs[1:]:
            for j in range(len(output)):
                if sorted(i) == sorted(output[j][0]): #self.anagram_check(i, output[j][0]):
                    output[j].append(i)
                    break
                if j == len(output) - 1:
                    output.append([i])

        return output

    def groupAnagrams2(self, strs):
        sortedchars = [tuple(sorted(list(i))) for i in strs]
        common = dict((i,[]) for i in sortedchars)
        for i, x in enumerate(strs):
            common[sortedchars[i]].append(x)
        return list(common.values())

    def group(self, strs):
        output_list = dict()
        for word in strs:
            key = "".join(sorted(word))
            if key not in output_list:  # [key]:    #{'act':cat,
                output_list[key] = [word]
            else:
                output_list[key].append(word)

        return list(output_list.values())



a = Solution()

print a.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"])
print a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print a.group(['cat', 'bat', 'mit', 'tac', 'tab'])
#print a.groupAnagrams2([""])
