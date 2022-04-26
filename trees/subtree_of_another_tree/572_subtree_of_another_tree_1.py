# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_nodes = []
        sub_nodes = []
        
        self.collectNodes(root, root_nodes)
        self.collectNodes(subRoot, sub_nodes)
        
        return self.rootContainsSub(root_nodes, sub_nodes)
        
    def collectNodes(self, n: Optional[TreeNode], nodes: List):
        """Traverse a tree from node n, adding its nodes to `nodes` list."""
        if n is None:
            nodes.append(None)
            return
        
        nodes.append(n.val)
        
        self.collectNodes(n.left, nodes)
        self.collectNodes(n.right, nodes)
                
    def rootContainsSub(self, r_nodes: List, s_nodes: List):
        # Note:  Python allows OOB slicing -- will simply truncate at end of list
        sub_len = len(s_nodes)
        
        for i, _ in enumerate(r_nodes):
            if r_nodes[i:i+sub_len] == s_nodes:
                return True
        
        return False           
