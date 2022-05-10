# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # A null subRoot is a sub-tree of *any* tree
        if subRoot is None:
            return True
        # A non-null subRoot can't be a sub-tree of a null root
        if root is None:
            return False        
        # If top-level root is same as subRoot, stop
        if self.isSameTree(root, subRoot):
            return True
        # Otherwise, recursively check root's child nodes vs subRoot.
        # only ONE needs to match, so use OR logic.
        return (self.isSubtree(root.left, subRoot)
             or self.isSubtree(root.right, subRoot))
        
        
    def isSameTree(self, node: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Returns True if node and subRoot are the same and have same children."""
        if node is None and subRoot is None:
            return True
        if node is not None and subRoot is not None:
            if node.val == subRoot.val:
                # All must match, so use AND logic
                return (self.isSameTree(node.left, subRoot.left) 
                    and self.isSameTree(node.right, subRoot.right))
        
        return False
