import collections
from typing import List
# Word Pattern II
def wordPatternMatch(self, pattern: str, s: str) -> bool:
    def backtrack(cur: str, pattern: str, mappings: dict):
        # if the pattern is empty, we've exhausted our search
        if not pattern:
            # if the string is also empty, we've found a bijective mapping
            return not cur
        # if the pattern is already mapped, we must use the provided mapping
        if pattern[0] in mappings:
            # if this isn't a valid mapping, return false
            if cur[:len(mappings[pattern[0]])] != mappings[pattern[0]]:
                return False
            # otherwise continue backtracking
            return backtrack(cur[len(mappings[pattern[0]]):], pattern[1:], mappings)
        # try each subset of the remaining string as a mapping
        for i in range(len(cur)):
            # if the current substring maps to another value, it isn't valid
            if cur[:i + 1] in mappings.values():
                continue
            # map the pattern to the substring
            mappings[pattern[0]] = cur[:i + 1]
            # backtrack
            if backtrack(cur[i + 1:], pattern[1:], mappings):
                return True
            # delete the invalid mapping
            del mappings[pattern[0]]
        # none of the substrings were valid, so there is no valid mapping
        return False

    return backtrack(s, pattern, {})

# Leftmost Column with at Least a One
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        rows, cols = binaryMatrix.dimensions()

        # Set pointers to the top-right corner.
        current_row = 0
        current_col = cols - 1

        # Repeat the search until it goes off the grid.
        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1

        # If we never left the last column, it must have been all 0's.
        return current_col + 1 if current_col != cols - 1 else -1



#Task Scheduler

from collections import deque, Counter
from heapq import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        q = deque()
        time = 0

        max_heap = [-cnt for cnt in count.values()]
        heapify(max_heap)

        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heappush(max_heap, q.popleft()[0])

        return time
'''
The maximum number of tasks is 26. Let's allocate an array frequencies of 26 elements to keep the frequency of each task.
Iterate over the input array and store the frequency of task A at index 0, the frequency of task B at index 1, etc.
Find the maximum frequency: f_max = max(frequencies).
Find the number of tasks which have the max frequency: n_max = frequencies.count(f_max).
If the number of slots to use is defined by the most frequent task, it's equal to (f_max - 1) * (n + 1) + n_max.
Otherwise, the number of slots to use is defined by the overall number of tasks: len(tasks).
Return the maximum of these two: max(len(tasks), (f_max - 1) * (n + 1) + n_max).
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        task_counts = collections.Counter(tasks).values()
        # max frequency
        M = max(task_counts)
        # count the most frequent tasks
        Mct = task_counts.count(M)
        return max(len(tasks), (M - 1) * (N + 1) + Mct)


