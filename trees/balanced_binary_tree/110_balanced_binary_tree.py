# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        
        if root is None:
            return True    
    
        self.nodeDepth(root)

        return self.balanced
    

    def nodeDepth(self, n: Optional[TreeNode]) -> int:
        # Early exit
        if not self.balanced:
            return -1
        if n is None:
            return 0
        
        left_depth = self.nodeDepth(n.left)
        right_depth = self.nodeDepth(n.right)
        
        if abs(left_depth - right_depth) < 2:
            # Pass depth to parent for continuation
            return 1 + max(left_depth, right_depth)
        else:
            # Setup early exit
            self.balanced = False
            return -1
