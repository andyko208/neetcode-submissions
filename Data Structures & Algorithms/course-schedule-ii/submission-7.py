class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Time: O(V + E), Space: O(V + E)
        # build adjacency list
        indegrees = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegrees[src] += 1
            adj[dst].append(src)

        # add all courses with no prereqs to q
        q = deque([])
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        # iterate through the q and append ones to the res
        res, total = [], 0
        while q:
            node = q.popleft()
            res.append(node)
            total += 1
            # find all courses that node is a prerequisite to
            for nei in adj[node]:
                indegrees[nei] -= 1
                # add to the queue if prereqs are finished
                if indegrees[nei] == 0:
                    q.append(nei)
        
        return res if total == numCourses else []

# adj[0] = [1]
# indegrees[0] = 1