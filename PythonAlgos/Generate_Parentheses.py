from typing import List

'''
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def isvalid(s):
            res_cnt = 0
            for c in s:
                if c == '(':
                    res_cnt += 1
                else:
                    res_cnt -= 1
                if res_cnt < 0:
                    return False

            return res_cnt == 0

        def helper(s):
            if len(s) == 2 * n:
                if isvalid(s):
                    res.append(s)
                return
            for a in ['(', ')']:
                helper(s + a)

        res = []
        helper("")
        return res


a = Solution()

print(a.generateParenthesis(1))