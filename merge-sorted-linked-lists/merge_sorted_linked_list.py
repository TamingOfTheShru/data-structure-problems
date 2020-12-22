# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#approach 1 (recursion)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1 
        if l1.val < l2.val:
            l1.next = Solution.mergeTwoLists(self, l1.next, l2)
            return l1
        else:
            l2.next = Solution.mergeTwoLists(self, l1, l2.next)
            return l2
#approach 2
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1 
        p = l1
        q = l2
        s = None
        
        if p.val <= q.val:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        new_head = s
        print(p, q, new_head)
        
        
        while p and q:
            if p.val <= q.val:
                s.next = p
                s=p
                p = s.next
               
            else:
                s.next = q
                s = q
                q = s.next
                
        #once one lists exhausts, just append the other sorted list to the current list
        if not p:
            s.next =q
        else:
            s.next =p
        return new_head
        
        
