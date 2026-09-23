"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create a entire new graph where each node is copy of the original
        if not node:
            return None
        # create a hashmap
        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])
        while q:
            cur = q.popleft()
            for ne in cur.neighbors:
                if ne not in oldToNew:
                    oldToNew[ne] = Node(ne.val)
                    q.append(ne)
                oldToNew[cur].neighbors.append(oldToNew[ne])
        return oldToNew[node]


