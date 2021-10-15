'''
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
'''

from typing import List


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True

        if len(A) != len(B):
            return False
        new_str = A
        for i in A:
            new_str = new_str[1:] + new_str[:1]
            if new_str == B:
                return True
        return False



a = Solution()
print(a.rotateString('abcde', 'cdeab'))
print(a.rotateString('abcde', 'abced'))
print(a.rotateString('ab', 'ba'))
print(a.rotateString('', ''))