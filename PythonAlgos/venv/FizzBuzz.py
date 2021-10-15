'''
https://leetcode.com/problems/fizz-buzz/
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.

'''


def fizzBuzz(n):
    res = []

    for i in range(1, n+1):
        div_by_3 = (i % 3 == 0)
        div_by_5 = (i % 5 == 0)

        res_str = ""

        if div_by_3:
            res_str += "Fizz"
        if div_by_5:
            res_str += "Buzz"
        if res_str == "":
            res_str = str(i)

        res.append(res_str)

    return res

print(fizzBuzz(15))