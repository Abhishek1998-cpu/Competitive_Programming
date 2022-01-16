# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root, minV=float('-inf'), maxV=float('inf')):
        if root is None:
            return True
        if root.val <= minV or root.val >= maxV:
            return False
        return self.isValidBST(root.left, minV, root.val) and self.isValidBST(root.right, root.val, maxV)
