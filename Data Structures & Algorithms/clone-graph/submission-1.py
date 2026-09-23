"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # # create a entire new graph where each node is copy of the original
        # if not node:
        #     return None
        # # create a hashmap that maps org: cloned
        # oldToNew = {}
        # # assign the head to a new Node
        # oldToNew[node] = Node(node.val)
        # # append old node to q
        # q = deque([node])
        # while q:
        #     # pop from q
        #     cur = q.popleft()
        #     # iterate through each neighbors
        #     for ne in cur.neighbors:
        #         # only clone the ones that aren't seen yet
        #         if ne not in oldToNew:
        #             oldToNew[ne] = Node(ne.val)
        #             q.append(ne)
        #         oldToNew[cur].neighbors.append(oldToNew[ne])
        # return oldToNew[node]
        
        # DFS
        # create hashmap
        oldToNew = {}
        if not node:
            return None
        def dfs(cur):
            # base case: return the clone if clone exists
            if cur in oldToNew:
                return oldToNew[cur]
            # assign clone to org
            oldToNew[cur] = Node(cur.val)
            # iterate through ne in neighbors
            for ne in cur.neighbors:
                # recurse on to create clones
                oldToNew[cur].neighbors.append(dfs(ne))
            return oldToNew[cur]

        return dfs(node)

