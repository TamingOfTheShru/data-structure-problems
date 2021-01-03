# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = Solution.lowestCommonAncestor(self, root.left, p, q)
        right = Solution.lowestCommonAncestor(self, root.right, p, q)

        if left == None and right == None:
            return None
        if left != None and right != None:
            return root
        return left if left else right
