class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # BFS
        # check the basic condition of tree to return False early
        if len(edges) > n-1:
            return False
        adj = [[] for _ in range(n)]
        for u, v, in edges:
            adj[u].append(v)
            adj[v].append(u)

        # keep visit hashset and add 0 to it
        visit = set()
        q = deque([(0, -1)])
        visit.add(0)
        while q:
            cur, par = q.popleft()
            for nei in adj[cur]:
                if nei == par:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, cur))
        return len(visit) == n
