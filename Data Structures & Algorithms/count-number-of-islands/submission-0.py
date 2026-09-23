class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS and increment count by 1
        m, n = len(grid), len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dy, dx in dirs:
                    ny, nx = dy + row, dx + col
                    if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] != "0":
                        q.append((ny, nx))
                        grid[ny][nx] = "0"

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        return count
