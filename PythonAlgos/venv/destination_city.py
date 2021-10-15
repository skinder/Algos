'''
https://leetcode.com/problems/destination-city/
Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".
'''

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        output = ""
        dest = set()
        air_from = set()
        for path in paths:
            dest.add(path[1])
            air_from.add(path[0])

        for i in dest:
            if i not in air_from:
                return i

        return output




a = Solution()
print(a.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))