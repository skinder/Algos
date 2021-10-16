'''
https://leetcode.com/problems/count-primes/
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''


class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, n):
            if isPrime[i]:
                j = 2
                while i * j < n:
                    isPrime[i * j] = False
                    j += 1
            else:
                continue
        return sum(isPrime)


a = Solution()

print a.countPrimes(10)
