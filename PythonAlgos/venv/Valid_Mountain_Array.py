'''
https://leetcode.com/problems/valid-mountain-array/
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]


Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true

'''


class Solution(object):
    def validMountainArray(self, A):
        if len(A) < 3 or A[0] == A[1]:
            return False

        if A[0] < A[1]:
            for i in range(1,len(A)-1):
                if A[i] < A[i+1]:
                    return True
                else:
                    return False
        else:
            for i in range(1,len(A)-1):
                if A[i] > A[i+1]:
                    return True
                else:
                    return False


a = Solution()

print a.validMountainArray([3,5,5])
print a.validMountainArray([2,1])
print a.validMountainArray([0,3,2,1])



