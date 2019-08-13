'''
https://leetcode.com/problems/reverse-string/
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''



class Solution(object):
    def reverseString(self, s):
        # return s[::-1]
        output = []
        for i in range(len(s) -1, -1, -1):
            output.append(s[i])
        return output

    def reverseString2(self, s):
        for i in range(int(len(s) / 2)):
            temp = str(s[i])
            s[i], s[-i-1] = (s[-i-1]), temp
        return s






a = Solution()

print a.reverseString(["h","e","l","l","o"])
print a.reverseString2(["h","e","l","l","o"])