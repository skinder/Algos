from __future__ import print_function

'''
https://leetcode.com/problems/buddy-strings/
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false

'''


def buddyStrings(A, B) :
        from collections import Counter
        if len(A) != len(B):
            return False
        if A == B:
            count = Counter(A)
            if len(count.keys()) > 1:
                return False
            else:
                return True
        l = []
        for i in range(len(A)):
            if A[i] != B[i]:
                l.append([A[i],B[i]])
                if len(l) > 2:
                    return False
        return l[0][0] == l[1][1] and l[0][1] == l[1][0]


A = "aaaaaaacb"
B = "aaaaaaabc"
print(buddyStrings(A,B))
