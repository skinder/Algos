'''
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'
'''

class Solution:
    def isValid(self, s: str) -> bool:
        opening_par = ["(", "[", "{"]
        closing_par = [")", "]", "}"]
        par_dict = {"(": ")", "{": "}", "[": "]"}
        if len(s) < 2 or s[0] not in opening_par:
            return False

        mem_list = []
        for i in s:
            if i in opening_par:
                mem_list.append(i)
            elif i in closing_par and len(mem_list) > 0:
                if par_dict[mem_list[-1]] == i:
                    mem_list.pop()
                else:
                    return False
            else:
                return False

        return len(mem_list) == 0



a = Solution()

print(a.isValid("[])"))
print(a.isValid("(]"))
print(a.isValid("()"))
print(a.isValid("()[]{}"))
print(a.isValid("([)]"))

