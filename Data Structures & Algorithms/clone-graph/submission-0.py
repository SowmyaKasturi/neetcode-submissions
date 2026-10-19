"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        visited = {}
        def clone_helper(parent):
            if parent in visited:
                return visited[parent]
            clone = Node(parent.val)
            visited[parent] = clone
            for child in parent.neighbors:
                clone.neighbors.append(clone_helper(child))
            return clone
        
        return clone_helper(node)
