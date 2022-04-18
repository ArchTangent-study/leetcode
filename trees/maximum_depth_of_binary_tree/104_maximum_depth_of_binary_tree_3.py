# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Limiter:
    __slots__ = "depth"
    def __init__(self):
        self.depth = 0

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            lim = Limiter()
            self.nextDepth(root, lim, 0)
            return lim.depth
            
        return 0
            
    def nextDepth(self, root: Optional[TreeNode], lim: Limiter, lvl: int):
        if root is not None:
            lv = lvl + 1
            if lv > lim.depth:
                lim.depth = lv
            self.nextDepth(root.left, lim, lv)
            self.nextDepth(root.right, lim, lv)
  