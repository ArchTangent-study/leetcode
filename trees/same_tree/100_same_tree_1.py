# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list = []
        q_list = []
        
        self.traverse(p, p_list)
        self.traverse(q, q_list)
        
        return p_list == q_list
        
    def traverse(self, n: Optional[TreeNode], nodes: list):
        """Traverse a tree, adding its nodes to the node list."""        
        if n is None:
            nodes.append(None)
            return
        
        nodes.append(n.val)
        
        self.traverse(n.left, nodes)
        self.traverse(n.right, nodes)  
        