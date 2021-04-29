# Reverse Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # First Corner Case
        if (head == []):
            return []
        current = head
        previous = None
        nextnode = None
        # print(current.next)
        while current:
            nextnode = current.next
            current.next = previous
            previous = current
            current = nextnode
            # print("Hello")
        return previous


# Input ->
# [1,2,3,4,5]
# [1,2]
# []

# Output ->
# [5,4,3,2,1]
# [2,1]
# []
