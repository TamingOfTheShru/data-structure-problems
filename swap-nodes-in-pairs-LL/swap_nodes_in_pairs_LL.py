# Given a linked list, swap every two adjacent nodes and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return
        ptr = head
        while ptr is not None and ptr.next is not None:
            if ptr.val == ptr.next.val:
                ptr = ptr.next.next
            else:
                ptr.val, ptr.next.val = ptr.next.val, ptr.val
                ptr = ptr.next.next
        return head
            

