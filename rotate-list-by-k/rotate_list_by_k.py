# Given the head of a linked list, rotate the list to the right by k places.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        ptr = head
        llen = 1
        while ptr.next:
            llen+=1
            ptr = ptr.next
     
        k %= llen
        if k == 0:
            return head
        
        ptr2 = ptr
        ptr.next = head
        steps = llen - k
        
        while steps !=0:
            steps -= 1
            ptr2 = ptr2.next

        new_head = ptr2.next
        ptr2.next = None
        return new_head
        
              

        
        
