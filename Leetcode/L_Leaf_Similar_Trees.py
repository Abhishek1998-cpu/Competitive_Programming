# Leaf Similar Trees

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        X = []
        Y = []

        def printLeafNodes1(root1):
            if (not root1):
                return
            if (not root1.left and not root1.right):
                X.append(root1.val)
                return
            if root1.left:
                printLeafNodes1(root1.left)
            if root1.right:
                printLeafNodes1(root1.right)

        def printLeafNodes2(root2):
            if (not root2):
                return
            if (not root2.left and not root2.right):
                Y.append(root2.val)
                return
            if root2.left:
                printLeafNodes2(root2.left)
            if root2.right:
                printLeafNodes2(root2.right)

        printLeafNodes1(root1)
        printLeafNodes2(root2)

        if (X == Y):
            return True
        return False
