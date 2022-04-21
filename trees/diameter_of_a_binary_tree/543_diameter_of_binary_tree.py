# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.D = 0
            
        def maxDepth(n: Optional[TreeNode]) -> int:
            if n is None:
                return 0
            
            left_depth = maxDepth(n.left)
            right_depth = maxDepth(n.right)
            
            self.D = max(self.D, left_depth + right_depth)
            
            return 1 + max(left_depth, right_depth)
            
        maxDepth(root)
                
        return self.D
        