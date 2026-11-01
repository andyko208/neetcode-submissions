class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # define variables
        m, n = len(grid), len(grid[0])
        maxArea = 0

        # define recursive function to return the max area
        def dfs(i, j):
            # # base case: index out of bounds, if has been visited
            # if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            #     return 0
            # # mark visited
            # grid[i][j] = 0
            # # recurse through and return the sum
            # return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

            stack = [(i, j)]
            area = 1
            while stack:
                # for i in range(len(stack)):
                # pop a node
                r, c = stack.pop()
                # mark as visited
                grid[r][c] = 0
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    # check for valid coordinate
                    curR, curC = r + dr, c + dc
                    if 0 <= curR < m and 0 <= curC < n and grid[curR][curC] == 1:
                        # push to stack
                        stack.append((curR, curC))
                        # increment level by 1
                        grid[curR][curC] = 0
                        area += 1
            return area
        # [
        #     [0,0,1,0,0,0,0,1,0,0,0,0,0],
        #     [0,0,0,0,0,0,0,1,1,1,0,0,0],
        #     [0,1,1,0,1,0,0,0,0,0,0,0,0],
        #     [0,1,0,0,1,1,0,0,1,0,1,0,0],
        #     [0,1,0,0,1,1,0,0,1,1,1,0,0],
        #     [0,0,0,0,0,0,0,0,0,0,1,0,0],
        #     [0,0,0,0,0,0,0,1,1,1,0,0,0],
        #     [0,0,0,0,0,0,0,1,1,0,0,0,0]
        # ]
        # iterate through the grid
        for i in range(m):
            for j in range(n):
                # check if valid to run dfs
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea