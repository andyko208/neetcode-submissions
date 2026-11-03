class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        # build adjacency mapping
        for a, b in prerequisites:
            preMap[b].append(a)
        
        # create a visited hashset to avoid duplicate visit
        visited = set()
        curPath = set()

        # define a recursive function to traverse through the courses
        def dfs(key):
            # base case to return False if cycle
            if key in curPath:
                return False
            if key in visited:
                return True
            # mark visited
            curPath.add(key)
            for adj in preMap[key]:
                if not dfs(adj):
                    return False
            curPath.remove(key)
            visited.add(key)
            return True
        
        # iterate through numCourses to run dfs
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        