class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Time: O(m*n), Space: O(m*n)
        # define variables
        m = len(grid)
        # handle the edge case
        if m == 0:
            return 0
        n = len(grid[0])
        # define a recursive function to iterate through to find all land
        def bfs(i, j):
            # area to return 
            area = 0 
            q = deque([(i, j)])
            while q:
                # pop an element
                r, c = q.popleft() 
                # mark as visited and increment area by 1
                area += 1
                grid[r][c] = 0
                # find land from all 4 neighbors and add to queue
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in dirs:
                    curR, curC = r + dr, c + dc
                    if 0 <= curR < m and 0 <= curC < n and grid[curR][curC] == 1:
                        q.append((curR, curC))
                        grid[curR][curC] = 0
            return area
    
        # keep a maxArea to update and return
        maxArea = 0
        # iterate through the grid
        for i in range(m):
            for j in range(n):
                # run dfs only if land
                if grid[i][j] == 1:
                    maxArea = max(maxArea, bfs(i, j))
        return maxArea

        # [[1,1,0,0,0],
        #  [1,1,0,0,0],
        #  [0,0,0,1,1],
        #  [0,0,0,1,1]]