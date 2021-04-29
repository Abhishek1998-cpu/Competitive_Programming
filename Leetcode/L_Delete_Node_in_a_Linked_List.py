# Delete Node in a Linked List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # print(node.val)
        # print(node.next.val)
        node.val = node.next.val
        node.next = node.next.next
        # print(node)


# Input ->
# [4,5,1,9]
# 5
# Linked List representation -> 4->5->1->9

# Output ->
# [4,1,9]
# Linked List representation -> 4->1->9
