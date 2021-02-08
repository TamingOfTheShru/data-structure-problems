# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        mid = Solution.find_middle(self, head)
        root = TreeNode(mid.val)
        if head == mid:
            return root
        root.left = Solution.sortedListToBST(self, head)
        root.right = Solution.sortedListToBST(self, mid.next)
        return root
       
    def find_middle(self, head):
        prev= None
        sp = head
        fp = head
        
        while fp is not None and fp.next is not None:
            prev=sp
            sp= sp.next
            fp=fp.next.next
        if prev:
            prev.next = None
        return sp
   
        
