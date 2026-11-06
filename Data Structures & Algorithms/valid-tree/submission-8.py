class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # define variables
        m = len(edges)
        # first check the condition of a valid tree
        if n - 1 != m:
            return False

        # create adjacency list
        visited = set()
        adj = [[] for _ in range(n)]
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        # start with 0, -1 as node and par
        q = deque([(0, -1)])
        # iterate through while q isn't empty
        while q:
            # pop a node
            node, par = q.popleft()
            # mark as visited
            visited.add(node)
            # iterate through the neighbors to add nei to q
            for nei in adj[node]:
                # if nei comes from par, ignore
                if nei == par:
                    continue
                # if nei in visited, return False
                if nei in visited:
                    return False
                # append nei to the q
                q.append((nei, node))
        return len(visited) == n