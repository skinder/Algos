'''
https://leetcode.com/problems/arranging-coins/
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
*
* *
* *

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
*
* *
* * *
* *

Because the 4th row is incomplete, we return 3.


'''

import math
class Solution(object):
    def arrangeCoins(self, n):
        return int ( (-1 + math.sqrt ( 1 + 8 * n )) // 2 )

    ('\n'
     '    The sum of the first n natural numbers is given by n*(n+1)/2. Let the given number of coins be S and n be the number of staircases. \n'
     '    So we solve for the maximum n that satisfies the equation n*(n+1)/2 <= S, \n'
     '    which leads to the quadratic equation n^2 + n - 2S <= 0. \n'
     '    Now we can use the quadratic formula to find the solution that satisfies the equation.\n'
     '    ')
    # Sum of the n Natural Numbers: x(x+1)/2 = n
    # => x**2 + x - 2n = 0
    # => d = 1 - 4*(-2n) = 1 + 8n
    # x = ( -1 + sqrt(d) ) // 2



a = Solution()

print a.arrangeCoins(8)