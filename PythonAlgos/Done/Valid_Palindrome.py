'''
https://leetcode.com/problems/valid-palindrome/
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''


class Solution(object):
    def isPalindrome(self, s):
        import re
        tmp = re.sub('[\W_]+', '', s).lower()
        if tmp == tmp[::-1]:
            return True
        else:
            return False

    def validPalindrome(self, s):

        if s == s[::-1]: return True

        l, r = 0, len(s) - 1

        while l <= r:

            if s[l] == s[r]:
                l += 1
                r -= 1

            else:
                temp1 = s[:l] + s[l + 1:]
                temp2 = s[:r] + s[r + 1:]
                if temp1 == temp1[::-1] or temp2 == temp2[::-1]:
                    return True
                else:
                    return False

        return True




object = Solution()

print object.isPalindrome("A man, a plan, a canal: Panama")
print object.isPalindrome("race a car")
print '-----------'
print object.validPalindrome("aba")
print object.validPalindrome("abca")
