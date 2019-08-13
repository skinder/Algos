'''
https://leetcode.com/problems/longest-harmonious-subsequence/
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

'''


class Solution(object):
    def findLHS(self, nums):
        from collections import Counter
        d = Counter(nums)
        m = 0
        for i in d:
            if i + 1 in d:
                t = d[i] + d[i + 1]
                if t > m:
                    m = t
        return m


a = Solution()

print a.findLHS([1,3,2,2,5,2,3,7])