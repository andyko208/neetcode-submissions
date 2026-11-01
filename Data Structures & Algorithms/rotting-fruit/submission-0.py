class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # define variable
        m, n = len(grid), len(grid[0])
        q = deque([])
        freshCount = 0

        # iterate through the grid to append rotten fruits to q and count fresh fruits
        for i in range(m):
            for j in range(n):
                # increment fresh count by 1
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        # print(freshCount, q)
        # iterate through q
        level = 0
        while q and freshCount > 0:
            rotted = 0
            # iterate through current elements in the queue by level
            for i in range(len(q)):
                r, c = q.popleft()
                # check four neighbors
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    curR, curC = r + dr, c + dc
                    # if neighbors coordinates are valid
                    if 0 <= curR < m and 0 <= curC < n and grid[curR][curC] == 1:
                        # rot the fruit
                        grid[curR][curC] = 2
                        q.append((curR, curC))
                        freshCount -= 1
            level += 1
        return level if freshCount == 0 else -1