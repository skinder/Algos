'''
https://leetcode.com/problems/1-bit-and-2-bit-characters/

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
'''


class Solution(object):
    def isOneBitCharacter(self, bits):
        if not bits:
            return False

        i, n = 0, len(bits) - 1
        while i < n:
            if bits[i]:
                i += 2
            else:
                i += 1
        if i == n:
            return True
        return False

    def isOneBitCharacter2(self, bits):
        return len(bits) % 2 != 0




a = Solution()

print a.isOneBitCharacter([1, 0, 0])
print a.isOneBitCharacter2([1, 0, 0])
print a.isOneBitCharacter([1, 1, 1, 0])
print a.isOneBitCharacter2([1, 1, 1, 0])