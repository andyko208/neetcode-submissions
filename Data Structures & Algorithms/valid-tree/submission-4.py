class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # BFS
        # check the basic condition of tree to return False early
        if len(edges) != n-1:
            return False
        # build adjacency list
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # keep visit hashset and add 0 to it
        visit = set()
        visit.add(0)
        q = deque([(0, -1)])
        # while q
        while q:
            # cur = q.popleft
            cur, par = q.popleft()
            # iterate through nei in neighbors
            for nei in adj[cur]:
                # if nei == par, continue
                if nei == par:
                    continue
                # if nei in visit, return False
                if nei in visit:
                    return False
                # add nei to visit
                visit.add(nei)
                q.append((nei, cur))
        return n == len(visit)
