'''
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.



Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]

'''

class Solution(object):
    def largeGroupPositions(self, S):
        #S += '#'
        ans = []
        start, prev = 0, S[0]
        for i in range(len(S)):
            if S[i] != prev:
                if i - start >= 3:
                    ans.append([start, i-1])
                start = i
                prev = S[start]
        return ans





a = Solution()

print a.largeGroupPositions("abbxxxxzzy")
print a.largeGroupPositions("abc")
print a.largeGroupPositions("abcdddeeeeaabbbcd")