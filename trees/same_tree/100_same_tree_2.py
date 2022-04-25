# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True
        self.p_index = -1
        p_list = []       
        
        self.traverse_p(p, p_list)
        self.traverse_q(q, p_list, len(p_list) - 1)
        
        return self.same
        
    def traverse_p(self, n: Optional[TreeNode], nodes: list):
        """Traverse p tree, adding its nodes to the node list."""        
        if n is None:
            nodes.append(None)
            return
        
        nodes.append(n.val)
        
        self.traverse_p(n.left, nodes)
        self.traverse_p(n.right, nodes)            
  

    def traverse_q(self, n: Optional[TreeNode], nodes: list, max_ix: int):
        """Traverse q tree, comparing values vs those of p."""  
        # Early exit
        if not self.same:
            return
        if self.p_index == max_ix:
            self.same = False
            return        
        
        self.p_index += 1
        
        if n is None:
            if nodes[self.p_index] is not None:
                self.same = False
            return           
        if n.val != nodes[self.p_index]:
            self.same = False
            return       

        self.traverse_q(n.left, nodes, max_ix)
        self.traverse_q(n.right, nodes, max_ix)
