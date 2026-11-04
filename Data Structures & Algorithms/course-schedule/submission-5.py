class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS cycle detection
        # Time: O(V + E), Space: O(V + E)
        # build adjacency mapping 
        preMap = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            preMap[src].append(dst)
        # recurse through each mapping and return True if mapping is empty
        cycle = set()
        def dfs(node):
            # base case to detect a cycle
            if node in cycle:
                return False
            # no neighbors means a safe node
            if preMap[node] == []:
                return True
            # mark as visited
            cycle.add(node)
            for nei in preMap[node]:
                # if any neighbors form a cycle, return False
                if not dfs(nei):
                    return False
            # if was able to traverse through, call it safe
            cycle.remove(node)
            preMap[node] = []
            return True
        # iterate i through numCourses and return False if any fails
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True