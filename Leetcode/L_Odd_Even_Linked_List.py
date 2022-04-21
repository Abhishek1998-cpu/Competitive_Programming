# Odd Even Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if(head == None):
            return None

        odd = head
        even = head.next
        evenFirst = even

        while(1 == 1):

            if(odd == None or even == None or (even.next) == None):
                odd.next = evenFirst
                break

            odd.next = even.next
            odd = even.next

            if(odd.next == None):
                even.next = None
                odd.next = evenFirst
                break

            even.next = odd.next
            even = odd.next

        return head

    def newNode(self, key):
        temp = key
        self.next = None
        return temp
