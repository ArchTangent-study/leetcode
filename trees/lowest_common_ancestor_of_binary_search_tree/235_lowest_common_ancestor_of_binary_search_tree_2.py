# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Locally assign all values to avoid repeated access of class variables
        rv, pv, qv = root.val, p.val, q.val
        # Case 1: p, q < root - traverse only left side
        if pv < rv and qv < rv:
            return self.lowestCommonAncestor(root.left, p, q)
        # Case 2: p, q > root - traverse only right side
        if pv > rv and qv > rv:
            return self.lowestCommonAncestor(root.right, p, q)
        # Case 3: p <= root <= q OR q <= root <= p - root must be the LCA
        return root
