'''
Input:
   arr[] =  {1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1}
Output:
  Index 9
Assuming array index starts from 0, replacing 0 with 1 at index 9 causes
the maximum continuous sequence of 1s.

Input:
   arr[] =  {1, 1, 1, 1, 0}
Output:
  Index 4


Using an Efficient Solution, the problem can solved in O(n) time.
The idea is to keep track of three indexes, current index (curr), previous zero index (prev_zero) and previous to previous zero index (prev_prev_zero).
Traverse the array, if current element is 0, calculate the difference between curr and prev_prev_zero
(This difference minus one is the number of 1s around the prev_zero). If the difference between curr and prev_prev_zero is more than maximum so far,
then update the maximum. Finally return index of the prev_zero with maximum difference.

'''


# Python program to find Index
# of 0 to be replaced with 1 to get
# longest continuous sequence
# of 1s in a binary array

# Returns index of 0 to be
# replaced with 1 to get longest
# continuous sequence of 1s.
#  If there is no 0 in array, then
# it returns -1.
def maxOnesIndex(arr, n):
    # for maximum number of 1 around a zero
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
        if (arr[curr] == 0):

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

    return max_index


# Driver program

#arr = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
arr = [0]
n = len(arr)

print("Index of 0 to be replaced is ",
      maxOnesIndex(arr, n))