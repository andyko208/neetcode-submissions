class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological sort -> keep track of the indegrees of the node to add 1st
        # build adjacency List
        inDegrees = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            # count incoming edge(# of prereqs to the course)
            inDegrees[dst] += 1
            adj[src].append(dst)
        
        # add nodes with indegrees 0 to the q
        q = deque([])
        for i in range(numCourses):
            if inDegrees[i] == 0:
                q.append(i)
        
        total = 0
        # iterate through while q is not empty to pop and count
        while q:
            node = q.popleft()
            total += 1
            # iterate through all prereqs of node
            for nei in adj[node]:
                # decrement the indegrees count and add to q if 0
                inDegrees[nei] -= 1
                if inDegrees[nei] == 0:
                    q.append(nei)
        
        return total == numCourses