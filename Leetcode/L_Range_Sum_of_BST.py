# Range Sum of BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [low, high] -> Square brackets tells us that our range will be inclusive of the low, low to high, and high


class Solution:
    def rangeSumBST(self, root: TreeNode, low, high):
        self.Sum = 0

        def inorder(root):
            if root:
                if root.val > low:
                    inorder(root.left)
                if low <= root.val <= high:
                    self.Sum += root.val
                if root.val < high:
                    inorder(root.right)
        inorder(root)
        return self.Sum


X = Solution()
print(X.rangeSumBST([10, 5, 15, 3, 7, 13, 18, 1, 6], 6, 10))
