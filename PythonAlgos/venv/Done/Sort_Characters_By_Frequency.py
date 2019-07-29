'''
https://leetcode.com/problems/sort-characters-by-frequency/
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        from collections import Counter
        lst = list(s)
        lst_frq = Counter(lst)

        def check(enum):
            return lst_frq[enum]

        lst.sort()
        lst.sort(key=check, reverse = True)
        output = "".join(lst)

        return output

    def frq2(self, s):
        return ''.join([c * n for c, n in Counter(s).most_common()])


a = Solution()
print a.frequencySort('tree')
print a.frequencySort("loveleetcode")
print a.frq2("loveleetcode")
