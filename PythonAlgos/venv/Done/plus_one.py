'''
https://leetcode.com/problems/plus-one/
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.



addToArrayForm
Add to Array-Form of Integer
https://leetcode.com/problems/add-to-array-form-of-integer/
Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000

A = [9,9,9,9,9,9,9,9,9,9]
st = [str(i) for i in A]
k = int(''.join(st))
print k
print type(k)

'''


class Solution (object):
    def plusOne(self, digits):
        n=len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                break

        # add one digit at the end if all 9th
        if digits[0] == 0:
            digits[0] += 1
            digits.append(0)
        return digits

    def addToArrayForm(self, A, K):
        input = int("".join([str(i) for i in A]))
        calc = input + K
        output = [int(i) for i in str(calc)]
        return output




a = Solution()

print a.plusOne([9,9,9])
print a.addToArrayForm([9,9,9], 2)

