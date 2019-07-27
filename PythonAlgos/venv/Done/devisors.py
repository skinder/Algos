# A Better (than Naive) Solution to find all divisiors
import math


# method to print the divisors
def printDivisors(n):
    # Note that this loop runs till square root
    i = 1
    calc = 0
    while i <= math.sqrt(n):

        if (n % i == 0):

            # If divisors are equal, print only one
            if (n / i == i) or (n / i == n):
                calc = calc + i
            else:
                calc = calc + i + (n / i)
        i = i + 1
    return n == calc


# Driver method
print "The divisors of 100 are: "
print printDivisors(100)


import math
class Solution(object):
    def checkPerfectNumber(self, num):
        # Note that this loop runs till square root
        if num <= 1:
            return False
        i = 1
        calc = 0
        while i <= math.sqrt(num):

            if (num % i == 0):

                # If divisors are equal, print only one
                if (num / i == i) or (num / i == num):
                    calc = calc + i
                else:
                    calc = calc + i + (num / i)
            i = i + 1
        return num == calc


a = Solution()

print a.checkPerfectNumber(-6)