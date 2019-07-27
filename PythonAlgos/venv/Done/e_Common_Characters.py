'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
'''

class Solution(object):
    def commonChars(self, A):
        check = list(A[0])
        for word in A[1:]:
            newCheck = []
            for c in word:
                if c in check:
                    newCheck.append(c)
                    check.remove(c)
            check = newCheck

        return check





a = Solution()

print a.commonChars(["bella","label","roller"])


