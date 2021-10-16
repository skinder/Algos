'''
https://leetcode.com/problems/reverse-vowels-of-a-string/
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

'''


class Solution:
    def reverseVowels(self, s):
        if len(s) == 0: return ""
        vowels = set("aeiouAEIOU")
        if len(s) == 1: return s

        s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] in vowels and s[r] in vowels:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l += 1
                r -= 1
            elif s[l] in vowels and s[r] not in vowels:
                r -= 1
            elif s[l] not in vowels and s[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        s = "".join(s)
        return s


a = Solution()

print a.reverseVowels("hello")