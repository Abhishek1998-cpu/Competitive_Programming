# Since this is the Tree Question -> Solve in the LeetCode Editor

# All Elements in Two Binary Search Trees
# Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1, root2):
        self.NodeList = []
        self.inorder1(root1)
        self.inorder2(root2)
        Ans = sorted(self.NodeList)
        return Ans

    def inorder1(self, root1):
        if root1:
            self.inorder1(root1.left)
            self.NodeList.append(root1.val)
            self.inorder1(root1.right)

    def inorder2(self, root2):
        if root2:
            self.inorder2(root2.left)
            self.NodeList.append(root2.val)
            self.inorder2(root2.right)
