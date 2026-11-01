class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Time: O(m*n), Space: O(m*n)
        # define variables
        m, n = len(grid), len(grid[0])
        q = deque([])
        INF = 2**31 - 1
        # append all treasures' coordinates to the q
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        # visit all neighbors of treasure to set as level
        level = 1
        while q:
            # pop a node
            for i in range(len(q)):
                r, c = q.popleft()
                # check validity of 4 neighbors coordinaes to assign the level at that cell
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    curR, curC = r + dr, c + dc
                    if 0 <= curR < m and 0 <= curC < n and grid[curR][curC] == INF:
                        grid[curR][curC] = level
                        q.append((curR, curC))
            level += 1
        