class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time: O(V + E)
        # Space: O(V + E)
        # micro-optimization 
        if len(edges) != n-1:
            return False
        # build adjacency mapping
        adj = [[] for _ in range(n)]
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()
        # define a recursive function to check the cycle
        def dfs(node, par):
            # base case to return False
            if node in visited:
                return False

            # mark node as visited
            visited.add(node)
            # iterate through neighbors and check if they form a cycle
            for nei in adj[node]:
                # skip the parent
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n