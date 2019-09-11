'''
https://leetcode.com/problems/binary-tree-paths/
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        if not root: return 0
        self.res = []
        self.helper(root, '')
        #self.helper2(root, 0)
        return self.res

    def binaryTreeSum(self, root):
        if not root: return 0
        self.res = []
        self.helper2(root, 0)
        return sum(self.res)

    def helper(self, root, ls):
        if not root.left and not root.right:
            self.res.append(ls + str(root.val))
        if root.left:
            self.helper(root.left, ls + str(root.val) + '->')
        if root.right:
            self.helper(root.right, ls + str(root.val) + '->')

    def helper2(self, root, ls):
        # sum all numbers
        if not root.left and not root.right:
            self.res.append(ls + root.val)
        if root.left:
            self.helper2(root.left, ls + root.val)
        if root.right:
            self.helper2(root.right, ls + root.val)


a = Solution()

root = TreeNode(0)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print a.binaryTreePaths(root)
print a.binaryTreeSum(root)

