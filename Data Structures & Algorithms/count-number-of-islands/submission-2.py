class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        # define variables
        m, n = len(grid), len(grid[0])
        visited = set()
        
        # define an iterative function to find all "1"s and add to visited hashset
        def bfs(i, j):
            q = deque([(i, j)])
            # traversal with q
            while q:
                r, c = q.popleft()
                # add the current
                # traverse through 4 neighbors
                dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in dirs:
                    # check for valid bounds
                    curR, curC = r + dr, c + dc
                    if 0 <= curR < m and 0 <= curC < n and (curR, curC) not in visited and grid[curR][curC] == "1":
                        visited.add((curR, curC))
                        q.append((curR, curC))
        
        # define a count to return
        numIslands = 0
        # iterate through the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    numIslands += 1
                    visited.add((i, j))
                    bfs(i, j)
        return numIslands

