'''
This is a demo task.
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2021 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''


def solution(A):
    set_A = set(A)
    for i in sorted(A):
        if i <= 0 and 1 not in set_A:
            return 1
        if i > 0 and i+1 not in set_A:
            return i+1
    return 1

print(solution([5, 8, 10]))
