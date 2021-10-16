'''
https://leetcode.com/problems/path-sum/
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # Starting with root = 5
        # Goal is to search L and R subtrees with (root.val - sum) value

        # Return Condition: When we reach a leaf node
        # and leaf node value == sum

        if not root: return False
        if root.val == sum and not root.left and not root.right: return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right,
                                                                             sum - root.val)  # Return true if either subtree has an answer


a = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.right = TreeNode(2)
root.left.left.left = TreeNode(7)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print a.hasPathSum(root,261)