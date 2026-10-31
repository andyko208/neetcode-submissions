"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # define a hashmap to map old node to new copy of that node
        oldToNew = {}
        # define a recursive function to connect neighbors and return the node
        def dfs(node):
            # base case to return the copy of the old node
            if node in oldToNew:
                return oldToNew[node]
            # base case to return None if node doesn't exist
            if node is None:
                return None
            # create a copy of the current node
            copy = Node(node.val)
            # map the node to copy to the hashmap
            oldToNew[node] = copy
            # iterate through all the neighbors and append them to copy's neighbors list
            for nei in node.neighbors:
                # recursively connect all node's neighbors to the copy's
                copy.neighbors.append(dfs(nei))
            # return the copy node
            return copy
        
        # edge case
        # if node is None:
        #     return [None]
        return dfs(node)
            
    