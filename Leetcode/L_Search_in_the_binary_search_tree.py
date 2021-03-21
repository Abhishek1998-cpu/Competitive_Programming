# Search in a Binary Search Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cur_node = root
        while cur_node:
            if cur_node.val == val:
                return cur_node
            elif val > cur_node.val:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left
        return None


# X = Solution()
# print(X.searchBST([4, 2, 7, 1, 3], 2))
