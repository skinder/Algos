'''
Given an array of 0s and 1s, find the position of 0
to be replaced with 1 to get longest continuous sequence of 1s. Expected time complexity is O(n) and auxiliary space is O(1).
https://www.geeksforgeeks.org/find-index-0-replaced-1-get-longest-continuous-sequence-1s-binary-array/
'''



def findMaxConsecutiveOnes(input):
    maxnum = 0
    count = 0
    for item in input:
        if item == '1':
            count = count + 1
            maxnum = max(count, maxnum)
        else:
            count = 0
    return maxnum


print findMaxConsecutiveOnes('010111111')


# Python program to find Index
# of 0 to be replaced with 1 to get
# longest continuous sequence
# of 1s in a binary array

# Returns index of 0 to be
# replaced with 1 to get longest
# continuous sequence of 1s.
#  If there is no 0 in array, then
# it returns -1.

def maxOnesIndex(arr):
    # for maximum number of 1 around a zero
    n = len(arr)
    max_count = 0

    # for storing result
    max_index = 0

    # index of previous zero
    prev_zero = -1

    # index of previous to previous zero
    prev_prev_zero = -1

    # Traverse the input array
    for curr in range(n):

        # If current element is 0,
        # then calculate the difference
        # between curr and prev_prev_zero
        if (arr[curr] == '0'):

            # Update result if count of
            # 1s around prev_zero is more
            if (curr - prev_prev_zero > max_count):
                max_count = curr - prev_prev_zero
                max_index = prev_zero

                # Update for next iteration
            prev_prev_zero = prev_zero
            prev_zero = curr

            # Check for the last encountered zero
    if (n - prev_prev_zero > max_count):
        max_index = prev_zero

    return max_count


# Driver program

arr = '110111111'
n = len(arr)

print("Index of 0 to be replaced is ", maxOnesIndex(arr))


def fnd_max(str):
    lst = [int(x) for x in str]
    if len(lst) == sum(lst):
        return sum(lst)

    result = prev = curr = 0
    for i in lst:
        if i == 1:
            curr += 1
        else:
            prev, curr = curr, 0
        result = max(result, prev + curr + 1)
    return result


print fnd_max('1011011')
print findMaxConsecutiveOnes('1011011')

