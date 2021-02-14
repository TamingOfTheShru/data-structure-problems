# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return
        fast = head.next
        slow = head
        while fast != None and fast.next != None and slow != None:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
            
