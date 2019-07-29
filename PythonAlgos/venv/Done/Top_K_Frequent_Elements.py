'''
https://leetcode.com/problems/top-k-frequent-elements/
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''



from collections import Counter
from heapq import *

class Solution(object):
    def topKFrequent(self, nums, k):
        dct = Counter(nums).most_common(k)
        return [value[0] for value in dct]

    def topKFrequent_h(self, nums, k):
        dct = Counter(nums)
        lst_frq = [[-frq, nbr] for nbr, frq in dct.items()]
        heapify(lst_frq)
        output = []
        for _ in range(k):
            output.append(heappop(lst_frq)[1])
        return output




a = Solution()

print a.topKFrequent([1,1,1,2,2,3], 2)
print a.topKFrequent_h([1,1,1,2,2,3], 2)