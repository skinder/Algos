'''
https://leetcode.com/problems/plus-one/
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:

Input: digits = [0]
Output: [1]
'''


def plusOne(digits):
    b = int(''.join(str(elem) for elem in digits)) + 1
    return ([int(num) for num in str(b)])


def plusOne2(digits):
    n = len(digits)

    # move along the input array starting from the end
    for idx in range(n-1,-1,-1):
        # idx = n - 1 - i
        # set all the nines at the end of array to zeros
        if digits[idx] == 9:
            digits[idx] = 0
        # here we have the rightmost not-nine
        else:
            # increase this rightmost not-nine by 1
            digits[idx] += 1
            # and the job is done
            return digits

    # we're here because all the digits are nines
    return [1] + digits



print(plusOne2([9]))