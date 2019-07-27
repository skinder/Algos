#Longest Increasing Subarray
# For example, if the input is [1, 2, 3, 4, 8, 7, 9], the output should be 5 because the longest increasing array is [1, 2, 3, 4, 8].
'''
Input : arr[] = {5, 6, 3, 5, 7, 8, 9, 1, 2}
Output : 5
The subarray is {3, 5, 7, 8, 9}

Input : arr[] = {12, 13, 1, 5, 4, 7, 8, 10, 10, 11}
Output : 4
The subarray is {4, 7, 8, 10}
'''



def longest(input):
    longest = 1
    curr = 1
    ind = 0
    if len(input) == 1:
        return longest, input
    if len(input) == 0:
        return None
    for i in range(1,len(input)):
        if input[i] > input[i-1]:
            curr += 1
            if curr > longest:
                longest = curr
                ind = i
        else:
            curr = 1
    return longest, input[(ind+1)-longest:ind+1]

print longest([5, 6, 3, 5, 7, 8, 9, 1, 2])
print longest([12, 13, 1, 5, 4, 7, 8, 10, 10, 11])
print longest([2,2,2,2,2,2,2,2,2])
print longest([2,1])
print longest([2,3])
print longest([2])
print longest([])



