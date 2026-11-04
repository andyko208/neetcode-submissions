class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # define variables
        m, n = len(grid), len(grid[0])
        # define a recursive function that marks the grid to visited -> 0
        def bfs(i, j):
            # define a q
            q = deque([(i, j)])
            # print(grid, q)
            # iterate through while q isn't empty
            while q:
                r, c = q.popleft()
                # mark visited
                grid[r][c] = '0'
                # iterate through all 4 neighbors
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    curR, curC = dr + r, dc + c
                    # check for valid coordinate
                    if 0 <= curR < m and 0 <= curC < n and grid[curR][curC] == '1':
                        # mark visited
                        grid[curR][curC] = '0'
                        q.append((curR, curC))

        # iterate through all the cells to call dfs
        count = 0
        for i in range(m):
            for j in range(n):
                # call dfs only current board is a land
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1
        return count