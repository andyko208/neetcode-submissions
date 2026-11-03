class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Time: O(n), Space: O(n)
        # build a mapping of crs: pre
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # detect cycle
        visited = set()
        cycle = set()
        ordering = []
        # define a recursive function to return False for a cycle given crs
        def dfs(crs):
            # base case to return False
            if crs in cycle:
                return False
            if crs in visited:
                return True
            # mark visited
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # reset to avoid redundant cycle for the next run
            cycle.remove(crs)
            # optimization to avoid repeat visiting what's already safe
            ordering.append(crs)
            visited.add(crs)
            # no cycle found
            return True
        
        # iterate through pres to append in order
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ordering
# visited = {0, 1, 2}
# preMap = {
#     0: [1],
#     1: [2],
#     2: [0]
# }