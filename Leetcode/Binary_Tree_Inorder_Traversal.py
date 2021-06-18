# Leetcode
# Binary Tree Inorder Traversal
# Best Question for Understanding the Implementation of Postorder, InOrder, and PreOrder Tree Traversal.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        self.X = []
        # Below was the base case of checking the empty Tree but No empty tree will be passed as an Input in this Question
        # if(root.val == None):
        #     print("Tree is Empty")
        # else:
        self._inorder(root)
        return self.X

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            self.X.append(root.val)
            self._inorder(root.right)
