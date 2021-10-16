'''
https://leetcode.com/problems/reverse-string-ii/
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string.
If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
'''


class Solution:
    def reverseStr(self, s, k):
        return s[::-1] if k > len(s) else s[:k][::-1] + s[k:2*k]+self.reverseStr(s[2*k:], k)

    def reverseStr2(self, s, k):
        i, ans = 0, ""
        while (i < len(s)):
            if i + k >= len(s):
                ans += s[i:][::-1]
            elif i + 2 * k >= len(s):
                ans += s[i:i + k][::-1] + s[i + k:]
            else:
                ans += s[i:i + k][::-1] + s[i + k:i + 2 * k]
            i += 2 * k
        return ans




a = Solution()

print a.reverseStr("abcdefg", 2)
print a.reverseStr2("abcdefg", 2)