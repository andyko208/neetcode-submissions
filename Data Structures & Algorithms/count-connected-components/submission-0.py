class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build adjacency list first
        adj = [[] for _ in range(n)]
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        # define a bfs function that will add the connect components to the visited
        visited = set()
        def bfs(node):
            q = deque([node])
            # iterate through the q while it's not empty
            while q:
                cur = q.popleft()
                # add cur to visited
                visited.add(cur)
                # iterate through the neighbors
                for nei in adj[cur]:
                    if nei not in visited:
                        # add cur to the hashset and the q
                        q.append(nei)
                        visited.add(nei)
                    
        count = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1
        return count