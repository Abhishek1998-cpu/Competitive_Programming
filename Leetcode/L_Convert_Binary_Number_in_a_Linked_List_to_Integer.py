# Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def getDecimalValue(self, head):
#         self.head = head
#         head2 = []
#         for i in head:
#             head2.append(str(i))
#         A = int("".join(head2))
#         num = A
#         dec_value = 0
#         base = 1
#         temp = num
#         while(temp):
#             last_digit = temp % 10
#             temp = int(temp/10)
#             dec_value += last_digit * base
#             base = base * 2
#         return dec_value


# X = Solution()
# print(X.getDecimalValue([1, 0, 1]))

# The Above solution was working right but there was a compilation error -> ListNode object is not iterable


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head):
        res = 0
        while head:
            res = (res << 1) | head.val
            head = head.next
        return res

# The Above is a true solution with no error
