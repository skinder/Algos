'''
https://leetcode.com/problems/keyboard-row/
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

'''


class Solution(object):
    def findWords(self, words):
        s1 = 'qwertyuiopQWERTYUIOP'
        s2 = 'asdfghjklASDFGHJKL'
        s3 = 'zxcvbnmZXCVBNM'

        dict1 = {i:1 for i in s1}
        dict2 = {i:1 for i in s2}
        dict3 = {i:1 for i in s3}

        L1 = []
        for word in words:
            if all(char in dict1 for char in word):
                L1.append(word)
            elif all(char in dict2 for char in word):
                L1.append(word)
            elif all(char in dict3 for char in word):
                L1.append(word)
        return L1

    def findWords2(self, words):
        ll = []
        a = set(['Q','W','E','R','T','Y','U','I','O','P'])
        b = set(['A','S','D','F','G','H','J','K','L'])
        c = set(['Z','X','C','V','B','N','M'])
        for i in words:
            ii = set(i.upper())
            if ii.intersection(a)==ii or ii.intersection(b)==ii or ii.intersection(c)==ii:
                ll.append(i)
        return ll


a = Solution()

print a.findWords(["Hello", "Alaska", "Dad", "Peace"])
print a.findWords2(["Hello", "Alaska", "Dad", "Peace"])