# Merge Two Sorted Lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Creating a Dummy Node
        temp = dummmy = ListNode(0)

        # Checking all the Corner test cases
        if(l1 is None):
            return l2
        if(l2 is None):
            return l1
        while(l1 and l2):
            if(l1.val < l2.val):
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
        # Case when length of the Linked List is not equal
        if(l1):
            temp.next = l1
        if(l2):
            temp.next = l2
        return dummmy.next


# X = Solution()
# print(X.mergeTwoLists([1, 2, 4], [1, 3, 4])) # It will not work as this, it is just a representation of the nodes. For example 1->2->4 and 1->3->4
