'''
https://leetcode.com/problems/backspace-string-compare/
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
'''



class Solution(object):
    def cnv(self,s):
        output = []
        input = [str(i) for i in s]
        for i in input:
            if i != '#':
                output.append(i)
            else:
                if len(output) > 0:
                    output.pop()
        return output

    def backspaceCompare(self,S,T):
        return self.cnv(S) == self.cnv(T)


a = Solution()

print a.backspaceCompare("a#c", "b")
print a.backspaceCompare("ab#c", "ad#c")
print a.backspaceCompare("a##c", "#a#c")