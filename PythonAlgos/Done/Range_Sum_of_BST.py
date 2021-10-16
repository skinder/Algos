'''
https://leetcode.com/problems/range-sum-of-bst/
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.



Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23






'''


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):

        if not root :
            return 0
        l = self.rangeSumBST (root.left, L, R)
        r = self.rangeSumBST (root.right, L, R)

        # check if it satisfies [L, R] else it's 0
        val = root.val if root.val >= L and root.val <= R else 0

        return val + l + r




a = Solution()

print a.rangeSumBST(TreeNode([10,5,15,3,7,18]),7,15)