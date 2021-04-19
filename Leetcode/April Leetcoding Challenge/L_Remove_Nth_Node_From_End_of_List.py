# Remove Nth Node From End of List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


X = Solution()
print(X.removeNthFromEnd([1, 2, 3, 4, 5],  2))
