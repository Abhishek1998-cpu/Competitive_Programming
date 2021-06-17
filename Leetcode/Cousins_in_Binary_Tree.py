import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isCousins(self, root, x, y):

        if root == None:
            return False

        # find a cousin - level by level, find its pair

        queue = collections.deque()
        queue.append((root, TreeNode(-1), 0))
        depth = 0
        result = []

        x_found = False
        y_found = False

        while (len(queue) > 0):
            length = len(queue)
            level = []
            depth += 1
            for i in range(0, len(queue), 1):
                popped = queue.popleft()
                popped_node = popped[0]
                popped_parent = popped[1]
                popped_level = popped[2]
                level.append(popped_node.val)

                # cousins if they have the same depth, but have different parents.

                if popped_node.val == x:
                    x_found = True
                    x_parent = popped[1].val
                    x_depth = popped_level
                if popped_node.val == y:
                    y_found = True
                    y_parent = popped[1].val
                    y_depth = popped_level
                if x_found and y_found:
                    if x_depth == y_depth and x_parent != y_parent:
                        return True
                    else:
                        return False

                if popped_node.left != None:
                    queue.append((popped_node.left, popped_node, depth))
                if popped_node.right != None:
                    queue.append((popped_node.right, popped_node, depth))

            #result.append([level, depth])

        # print(result)
        return False
