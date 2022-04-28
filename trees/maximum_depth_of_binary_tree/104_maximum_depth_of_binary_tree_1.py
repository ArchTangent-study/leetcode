# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            depths: List[int] = []
            self.nextDepth(root, depths, 0)
            return max(depths)
            
        return 0
            
    def nextDepth(self, root: Optional[TreeNode], d: List[int], lvl: int):
        if root is not None:
            lv = lvl + 1
            d.append(lv)
            self.nextDepth(root.left, d, lv)
            self.nextDepth(root.right, d, lv)
            