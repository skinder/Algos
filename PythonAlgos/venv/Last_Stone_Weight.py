'''
https://leetcode.com/problems/last-stone-weight/
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)



Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

'''
import bisect
import heapq
from typing import List

def lastStoneWeight(stones: List[int]) -> int:
    stones.sort()
    while len(stones) > 1:
        stone_1 = stones.pop()
        stone_2 = stones.pop()
        if stone_1 != stone_2:
            bisect.insort(stones, stone_1 - stone_2)
    return stones[0] if stones else 0


def lastStoneWeightH(stones: List[int]) -> int:

        # Make all the stones negative. We want to do this *in place*, to keep the
        # space complexity of this algorithm at O(1). :-)
        for i in range(len(stones)):
            stones[i] *= -1

        # Heapify all the stones.
        heapq.heapify(stones)

        # While there is more than one stone left, remove the two
        # largest, smash them together, and insert the result
        # back into the heap if it is non-zero.
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)

        # Check if there is a stone left to return. Convert it back
        # to positive.
        return -heapq.heappop(stones) if stones else 0

print(lastStoneWeightH([2,7,4,1,8,1]))