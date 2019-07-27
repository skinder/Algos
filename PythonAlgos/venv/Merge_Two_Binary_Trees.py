'''
https://leetcode.com/problems/merge-two-binary-trees/
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.
'''


# Helper class that allocates a new node
# with the given data and None left and
# right pointers.
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Given a binary tree, prits nodes
# in inorder
def inorder(node):
    if (not node):
        return

    # first recur on left child
    inorder(node.left)

    # then print the data of node
    print node.data

    # now recur on right child
    inorder(node.right)


# Function to merge given two
# binary trees
def MergeTrees(t1, t2):
    if (not t1):
        return t2
    if (not t2):
        return t1
    t1.data += t2.data
    t1.left = MergeTrees(t1.left, t2.left)
    t1.right = MergeTrees(t1.right, t2.right)
    return t1


# Driver code
if __name__ == '__main__':
    # Let us construct the first Binary Tree
    #    1
    #    / \
    #    2   3
    # / \    \
    # 4 5    6
    root1 = newNode(1)
    root1.left = newNode(2)
    root1.right = newNode(3)
    root1.left.left = newNode(4)
    root1.left.right = newNode(5)
    root1.right.right = newNode(6)

    # Let us construct the second Binary Tree
    #    4
    #    / \
    # 1  7
    # /  / \
    # 3  2 6
    root2 = newNode(4)
    root2.left = newNode(1)
    root2.right = newNode(7)
    root2.left.left = newNode(3)
    root2.right.left = newNode(2)
    root2.right.right = newNode(6)

    root3 = MergeTrees(root1, root2)
    print("The Merged Binary Tree is:")
    inorder(root3)