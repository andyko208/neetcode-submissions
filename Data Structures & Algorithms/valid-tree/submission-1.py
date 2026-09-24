class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree is a graph with no cycle
        # detect a cycle from the adjacency list

        # create a Node class with val and neighbor nodes
        
        if len(edges) > n-1:
            return False
        # build adjacency list first
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        visit.add(0)
        # current node, parent node
        q = deque([(0, -1)])
        while q:
            cur, par = q.popleft()
            # visit the neighbors of cur
            for nei in adj[cur]:
                # avoid treating traversal as cycle
                if nei == par:
                    continue
                # cycle detected
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, cur))
        return len(visit) == n

        