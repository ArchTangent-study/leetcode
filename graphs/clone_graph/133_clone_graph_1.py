#type: ignore

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Account for empty Node
        if node is None:
            return None
        # Store all cloned nodes by { Node.val: Node }
        cloned = { node.val: Node(node.val) }
        # Queue of Node.val data to be cloned and connected
        nodes_to_clone = deque([ n for n in node.neighbors ])

        while nodes_to_clone:
            current = nodes_to_clone.popleft()
            # Create clone if not present in `cloned` (ignore if present)
            if current.val not in cloned:
                clone = Node(current.val)
                cloned[current.val] = clone
                # Connect any cloned neighbors to this clone
                for neighbor in current.neighbors:
                    neighbor_val = neighbor.val
                    if neighbor_val in cloned:
                        # Create undirected connection between each
                        cloned[neighbor_val].neighbors.append(clone)
                        cloned[clone.val].neighbors.append(cloned[neighbor_val])
                    else:
                        # Add neighbor to queue to be cloned later
                        nodes_to_clone.append(neighbor)

        # Finish by returning the first Node (one with val = 1)
        return cloned[node.val]