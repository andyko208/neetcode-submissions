class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        # build adjacency mapping
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # create a visited hashset to avoid duplicate visit
        visited = set()

        # define a recursive function to traverse through the courses
        def dfs(key):
            # base case to return False if cycle
            if key in visited:
                return False
            # doesn't have any prereqs
            if preMap[key] == []:
                return True
            # mark visited
            visited.add(key)
            for pre in preMap[key]:
                if not dfs(pre):
                    return False
            visited.remove(key)
            preMap[key] = []
            return True
        
        # iterate through numCourses to run dfs
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        