'''
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].


from collections import Counter
class Solution(object):
    def findLength(self, A, B):
        a_dict = Counter(A)
        b_dict = Counter(B)
        output = 0
        for key in a_dict:
            if key in b_dict:
                output = output + min(a_dict[key], b_dict[key])
        return output

'''



class Solution(object):
    def findLength(self, A, B):
        if(A is None or B is None):
            return 0
        n=len(A)
        dp=[0]*n
        n2=len(B)
        temp=[0]*n
        maxlen = 0
        for i in range(n2):
            for j in range(n):
                if(i==0 or j==0):
                    temp[j]= 1 if A[j]==B[i] else 0
                elif(A[j]==B[i]):
                    temp[j]=dp[j-1]+1
                    maxlen=max(temp[j],maxlen)
                else:
                    temp[j]=0
            dp=list(temp)
        return maxlen


a = Solution()

print a.findLength([1,2,3,2,1], [3,2,1,4,7])