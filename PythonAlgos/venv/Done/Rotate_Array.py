'''
https://leetcode.com/problems/rotate-array/
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

def rotate(nums, k):
    k = k % len(nums)
    save = [nums[i] for i in range(len(nums) - k, len(nums))]
    for ix in range(len(nums) - 1, k - 1, -1):
        nums[ix] = nums[ix - k]
    for ix in range(k):
        nums[ix] = save[ix]
    return nums


print rotate([1,2,3,4,5,6,7], 3)


'''

def rot_arr(nums, k):
    ln = len(nums)
    k = k % ln
    print k
    if ln <= 1 & k == 0 & ln <= k:
        return nums
    else:
        return nums[-k:] + nums[:-k]

print rot_arr([1] , 0)
print rot_arr([-1,-100,3,99] , 3)
print rot_arr([1,2,3,4,5,6,7], 3)


# Iterative python program to reverse an array

# Function to reverse A[] from start to end
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)








