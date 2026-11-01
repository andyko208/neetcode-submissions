"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # BFS - Time: O(V + E), Space: O(V)
        # define a hashmap to map old node to copy
        oldToNew = {}
        # edge case to return an empty list if node is None
        if node is None:
            return None
        # initialize a queue with the node
        q = deque([node])
        # iterate through the node in the q while it's valid
        while q:
            # pop a node
            cur = q.popleft()
            # create a new copy 
            copy = Node(cur.val) if cur not in oldToNew else oldToNew[cur]
            oldToNew[cur] = copy
            # iterate through the neighbors in the current node's
            for nei in cur.neighbors:
                # append the old neighbor to append its neighbor after
                if nei not in oldToNew:
                    q.append(nei)
                # create a new copy of the neighbors if it doesn't exist or lookup
                nei_copy = Node(val=nei.val) if nei not in oldToNew else oldToNew[nei]
                # append the copy of the neighbor to copy's neighbor list
                copy.neighbors.append(nei_copy)
                # map the copied neighbor to neighbor hashmap
                oldToNew[nei] = nei_copy
        return oldToNew[node]

    