# Same Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p and q or not q and p or q.val != p.val:
            return False
        else:
            return Solution.isSameTree(self, p.left, q.left) and Solution.isSameTree(self, p.right, q.right)
