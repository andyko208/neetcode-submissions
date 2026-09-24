class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check if basic conditon of tree is met
        if len(edges) != n-1:
            return False
        # create an adjacency list off of edges
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # keep a visit hashset to track cycle
        visit = set()
        # create dfs(cur, par)
        def dfs(cur, par):
            # return False if cur in visit
            if cur in visit:
                return False
            # add cur to visit
            visit.add(cur)
            # iterate through neighbors in adj[cur]
            for nei in adj[cur]:
                # if nei == par, continue to avoid counting parent <-> node as cycle
                if nei == par:
                    continue
                if not dfs(nei, cur):
                    return False
                # return dfs(ne, cur)
            return True
        # outside the function, return dfs(0, -1) and n == len(visit)
        return dfs(0, -1) and n == len(visit)
            
