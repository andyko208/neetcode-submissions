class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # define variables
        m, n = len(grid), len(grid[0])
        visited = set()
        q = deque()
        # append all coordinates of treasures into q and visited hashset
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
        m, n = len(grid), len(grid[0])
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                # iterate through all four directions to add to q and visited
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in dirs:
                    curR, curC = r + dr, c + dc
                    if 0 <= curR < m and 0 <= curC < n and grid[curR][curC] != -1 and (curR, curC) not in visited:
                        visited.add((curR, curC))
                        q.append([curR, curC])
            dist += 1