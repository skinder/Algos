'''
https://leetcode.com/problems/single-number-ii/
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''

from collections import Counter
lst = ['A','B','C']
cnt = Counter(lst)
print cnt['A'] + 1

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
dict_1 = {k:v for v, k in enumerate(list1)}
dict_2 = {k:v for v, k in enumerate(list2)}

if "Tapioca Express" in dict_2:
    print 1
else:
    print 0

print dict_1
print dict_2