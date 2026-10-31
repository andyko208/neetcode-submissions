class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # define variables
        m = len(grid)
        # handle the edge case
        if m == 0:
            return 0
        n = len(grid[0])
        # define a recursive function to iterate through to find all land
        def dfs(i, j):
            # base case to return 0 if out of bounds or not a land
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            # mark current as visited -> need to check with the interviewer first: changing input ok?
            grid[i][j] = 0
            # recurse through all 4 directions and return the total, add 1 since curr is 1
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
    
        # keep a maxArea to update and return
        maxArea = 0
        # iterate through the grid
        for i in range(m):
            for j in range(n):
                # run dfs only if land
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea