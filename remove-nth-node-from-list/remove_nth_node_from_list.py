# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        if head.next is None:
            return
        for i in range(n):
            fast = fast.next
            
        # if fast is None, it means the first element is to be deleted from the list    
        if fast == None:
            head = head.next
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return head
#         size = 1
#         cur = p = head
#         while cur.next:
#             size += 1
#             cur = cur.next
#             if size > n + 1:
#                 p = p.next
#         if size == n:
#             return head.next
#         else:
#             p.next = p.next.next
#             return head
        
        
